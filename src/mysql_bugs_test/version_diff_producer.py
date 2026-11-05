#!/usr/bin/env python3
"""Version-differential target detector for the MySQL introduce-commit pipeline.

For each candidate, run the complete SQL against a mysqld built at the commit's
parent revision and against a mysqld built at the target revision, both compiled
identically (Debug + ENABLE_GCOV), then compare observable behavior. Sessions run
serially in the declared session_order; each session includes its configuration,
setup, operations, and cleanup. Concurrent schedules and server-level configuration
are unsupported and are recorded as not_run, never as no_difference. A candidate
is selected as interesting when the two sides differ observably:

  * result_set_diff : both sides succeed but the result rows differ
                      (compared order-insensitively, since candidates may omit
                      ORDER BY; an order-only difference is recorded but is not
                      itself a hit),
  * status_diff     : exactly one side succeeds and the other errors/crashes
                      (success/error outcome differs),
  * crash_diff      : the server crashes on exactly one side,
  * error_diff      : both sides error (client returncode != 0, no crash) but
                      their stderr differs exactly.

Startup / connection failures are excluded (they are not a SQL version
difference). A timeout is recorded as pending review and is not a hit. Version
differences select candidates for further study; they are not bugs by
themselves, and a difference can come from an intended fix or feature change.

Design contract (frozen producer_sha256):
  * self-contained, Python standard library only;
  * runs inside a Docker container whose workspace is mounted at /work so the
    runtime_<label> and runtime_parent_<label> trees line up;
  * emits observations/ + evidence/ consumed by commit_pipeline.classify_feedback.

The measurement is a boolean version-difference flag, so the target contract
method is "version_differential" and the pointer is
/measurements/version_diff_observed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

WORK = Path("/work")

# Frozen after the script is finalised; must equal the value frozen in the
# pipeline contracts file passed to ``commit_pipeline init --contracts``.
PRODUCER_SHA256 = "da1c83cab2c7b2081e661a259c3475f000890087c255fa3b02e69dfbf3ce9363"

# Commit short label -> full 40-char target (child) revision, and its parent.
FULL_REVISIONS = {
    "4d2da251cb53": "4d2da251cb536340d19438cc0039bb2846f9a634",
    "248c7f7c227e": "248c7f7c227e76f3422378ca3b9e10d141dcfc86",
    "c296cddb93ff": "c296cddb93ffc631f9b43d3b1ff769604e7469d7",
}
PARENT_REVISIONS = {
    "4d2da251cb53": "e248166db3c95b4fc998ca14cff914f1fdafbe7b",
    "248c7f7c227e": "15980860ac2639f41dfbda2f7fffb7aeeab32921",
    "c296cddb93ff": "74c7ccfa27f482576412300e5f92fd3dbeb54cfa",
}
CONNECTION_ERROR = re.compile(r"(?m)^ERROR (?:1045|2002|2003|2006|2013) \(")


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def file_sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def producer_identity_hash():
    """Hash of this file with the PRODUCER_SHA256 value normalized, so the
    frozen hash does not depend on its own string representation."""
    text = Path(__file__).read_text(encoding="utf-8")
    text = re.sub(r'PRODUCER_SHA256 = "[^"]*"', 'PRODUCER_SHA256 = "<frozen>"', text, count=1)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def log(message):
    print(message, flush=True)


def run(args, input_text=None, timeout=300):
    started = time.monotonic()
    try:
        proc = subprocess.run(args, input=input_text.encode("utf-8") if input_text is not None else None,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
        return {"returncode": proc.returncode,
                "stdout": proc.stdout.decode("utf-8", errors="replace"),
                "stderr": proc.stderr.decode("utf-8", errors="replace"),
                "timed_out": False, "elapsed": round(time.monotonic() - started, 3)}
    except subprocess.TimeoutExpired as exc:
        return {"returncode": None,
                "stdout": (exc.stdout or b"").decode("utf-8", errors="replace"),
                "stderr": (exc.stderr or b"").decode("utf-8", errors="replace"),
                "timed_out": True, "elapsed": round(time.monotonic() - started, 3)}
    except OSError as exc:
        return {"returncode": None, "stdout": "", "stderr": str(exc),
                "timed_out": False, "transport_error": True,
                "elapsed": round(time.monotonic() - started, 3)}


class UnsupportedCandidate(ValueError):
    """The producer cannot faithfully execute this candidate's semantics."""


def build_session_sqls(candidate, db):
    """Build one complete script per session in the declared serial order."""
    if candidate.get("execution_mode", "serial") != "serial":
        raise UnsupportedCandidate("concurrent session semantics are unsupported")
    sessions = candidate.get("session_order")
    if (not isinstance(sessions, list) or not sessions
            or any(not isinstance(session, str) or not session for session in sessions)
            or len(sessions) != len(set(sessions))):
        raise ValueError("session_order must contain unique nonempty session IDs")

    per_session = {session: [] for session in sessions}

    def add(item, field):
        if not isinstance(item, dict) or item.get("session") not in per_session:
            raise ValueError("%s item references an undeclared session" % field)
        sql = item.get("sql")
        if not isinstance(sql, str) or not sql.strip():
            raise ValueError("%s item requires SQL" % field)
        sql = sql.strip()
        if field == "configuration":
            supported = re.match(
                r"(?is)^\s*SET\s+(?:SESSION\b|@@SESSION\.|NAMES\b|CHARACTER\s+SET\b|TRANSACTION\b)", sql)
            if not supported or ";" in sql.rstrip().rstrip(";"):
                raise UnsupportedCandidate("only one session-scoped SET configuration statement is supported")
        if not sql.endswith(";"):
            sql += ";"
        per_session[item["session"]].append(sql)

    for item in candidate.get("configuration", []):
        add(item, "configuration")
    for field in ("setup", "operations", "cleanup"):
        for item in candidate.get(field, []):
            add(item, field)

    scripts = {}
    for session in sessions:
        prelude = ["USE `%s`;" % db, "SET time_zone='+00:00';"]
        scripts[session] = "\n".join(prelude + per_session[session]) + "\n"
    return scripts


def init_datadir(mysqld, base, datadir):
    if (datadir / "mysql").exists():
        return {"returncode": 0, "stdout": "existing", "stderr": ""}
    return run([str(mysqld), "--no-defaults", "--initialize-insecure",
                "--user=root", "--basedir=%s" % base, "--datadir=%s" % datadir,
                "--lc-messages-dir=%s" % (base / "share"),
                "--innodb-buffer-pool-size=64M", "--innodb-redo-log-capacity=64M"],
               timeout=300)


def run_side(rt_dir, datadir, revision, side, cid, db, session_sqls, sql_timeout, mysqld_timeout, folder):
    """Run complete serial sessions in order against one build."""
    mysqld = rt_dir / "bin" / "mysqld"
    mysql = rt_dir / "bin" / "mysql"
    mysqladmin = rt_dir / "bin" / "mysqladmin"
    socket = datadir / "mysql.sock"

    init = init_datadir(mysqld, rt_dir, datadir)
    if init["returncode"] != 0:
        return {"side": side, "revision": revision, "startup_failed": True,
                "returncode": None, "stdout": "", "stderr": "datadir init failed: " + init["stderr"],
                "timed_out": False, "server_crashed": False, "init_stderr": init["stderr"]}

    server_log = folder / f"{side}.server.log"
    pid_file = folder / f"{side}.mysqld.pid"
    with pid_file.open("w") as pf:
        pf.write("")
    start = subprocess.Popen(
        [str(mysqld), "--no-defaults", "--user=root",
         "--basedir=%s" % rt_dir, "--datadir=%s" % datadir,
         "--socket=%s" % socket, "--pid-file=%s" % pid_file,
         "--log-error=%s" % server_log,
         "--skip-networking", "--lc-messages-dir=%s" % (rt_dir / "share"),
         "--innodb-buffer-pool-size=64M", "--innodb-redo-log-capacity=64M"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    ready = False
    deadline = time.monotonic() + mysqld_timeout
    while time.monotonic() < deadline:
        ping = run([str(mysqladmin), "--socket=%s" % socket, "--user=root",
                    "ping", "--silent"], timeout=15)
        if ping["returncode"] == 0:
            ready = True
            break
        if start.poll() is not None:
            break
        time.sleep(1)

    if not ready:
        if start.poll() is None:
            start.kill()
        try:
            start.wait(timeout=30)
        except subprocess.TimeoutExpired:
            pass
        return {"side": side, "revision": revision, "startup_failed": True,
                "returncode": None, "stdout": "", "stderr": "mysqld not ready",
                "timed_out": False, "server_crashed": False,
                "server_log_tail": tail(server_log)}

    stdout_parts, stderr_parts = [], []
    returncode, timed_out, connection_failed = 0, False, False
    reset = run([str(mysql), "--socket=%s" % socket, "--user=root",
                 "--default-character-set=utf8mb4", "--batch", "--raw"],
                input_text="DROP DATABASE IF EXISTS `%s`; CREATE DATABASE `%s`;" % (db, db),
                timeout=sql_timeout)
    reset_error = bool(re.search(r"(?m)^ERROR [0-9]+ ", reset["stderr"]))
    preparation_failed = (reset.get("transport_error", False) or reset["timed_out"]
                          or reset["returncode"] != 0 or reset_error)
    connection_failed = bool(reset.get("transport_error", False)
                              or CONNECTION_ERROR.search(reset["stderr"]))
    if preparation_failed:
        returncode = 1
        stderr_parts.append("database preparation\n" + reset["stderr"])
    for session, sql_text in (() if preparation_failed else session_sqls.items()):
        exec_result = run([str(mysql), "--socket=%s" % socket, "--user=root",
                           "--default-character-set=utf8mb4", "--batch", "--raw", "--force"],
                          input_text=sql_text, timeout=sql_timeout)
        stdout_parts.append("-- session %s --\n%s" % (session, exec_result["stdout"]))
        stderr_parts.append("-- session %s --\n%s" % (session, exec_result["stderr"]))
        timed_out = timed_out or exec_result["timed_out"]
        sql_error = bool(re.search(r"(?m)^ERROR [0-9]+ ", exec_result["stderr"]))
        connection_failed = connection_failed or exec_result.get("transport_error", False) or bool(
            CONNECTION_ERROR.search(exec_result["stderr"]))
        if exec_result["returncode"] not in (0, None) or sql_error:
            returncode = 1
        if exec_result["timed_out"] or connection_failed:
            break

    shutdown = run([str(mysqladmin), "--socket=%s" % socket, "--user=root",
                    "shutdown"], timeout=120)
    server_crashed = (shutdown["returncode"] != 0 and not Path(socket).exists())
    cleanup_failed = shutdown["timed_out"] or (shutdown["returncode"] != 0 and not server_crashed)

    if start.poll() is None:
        try:
            start.wait(timeout=600)
        except subprocess.TimeoutExpired:
            cleanup_failed = True
            start.kill()
            try:
                start.wait(timeout=60)
            except subprocess.TimeoutExpired:
                pass
    if not cleanup_failed and start.returncode not in (0, None):
        server_crashed = True
    if server_crashed:
        connection_failed = False

    return {"side": side, "revision": revision, "startup_failed": False,
            "connection_failed": connection_failed, "preparation_failed": preparation_failed,
            "cleanup_failed": cleanup_failed,
            "returncode": returncode,
            "stdout": "".join(stdout_parts), "stderr": "".join(stderr_parts),
            "timed_out": timed_out, "server_crashed": server_crashed}


def tail(path, n=2000):
    try:
        return "\n".join(Path(path).read_text(encoding="utf-8", errors="replace").splitlines()[-n:])
    except OSError:
        return ""


def sorted_lines(text):
    return sorted(text.splitlines())


def classify_diff(parent, target):
    """Compare parent vs target results; return the diff classification."""
    if parent.get("preparation_failed") or target.get("preparation_failed"):
        side = "parent" if parent.get("preparation_failed") else "target"
        if parent.get("preparation_failed") and target.get("preparation_failed"):
            side = "both"
        return {"version_diff_observed": False, "diff_types": ["database_preparation_failure"],
                "excluded": "database_preparation_failure:%s" % side,
                "row_order_differs": False}
    if parent["startup_failed"] or target["startup_failed"]:
        side = "parent" if parent["startup_failed"] else "target"
        if parent["startup_failed"] and target["startup_failed"]:
            side = "both"
        return {"version_diff_observed": False, "diff_types": ["startup_or_connection_failure"],
                "excluded": "startup_failure:%s" % side,
                "row_order_differs": False}
    if parent.get("connection_failed") or target.get("connection_failed"):
        side = "parent" if parent.get("connection_failed") else "target"
        if parent.get("connection_failed") and target.get("connection_failed"):
            side = "both"
        return {"version_diff_observed": False, "diff_types": ["connection_failure"],
                "excluded": "connection_failure:%s" % side,
                "row_order_differs": False}
    if parent["timed_out"] or target["timed_out"]:
        side = "parent" if parent["timed_out"] else "target"
        if parent["timed_out"] and target["timed_out"]:
            side = "both"
        return {"version_diff_observed": False, "diff_types": ["timeout_pending"],
                "excluded": "timeout:%s" % side,
                "row_order_differs": False}
    if parent.get("cleanup_failed") or target.get("cleanup_failed"):
        side = "parent" if parent.get("cleanup_failed") else "target"
        if parent.get("cleanup_failed") and target.get("cleanup_failed"):
            side = "both"
        return {"version_diff_observed": False, "diff_types": ["cleanup_pending"],
                "excluded": "cleanup_pending:%s" % side,
                "row_order_differs": False}

    p_ok = parent["returncode"] == 0 and not parent["server_crashed"]
    t_ok = target["returncode"] == 0 and not target["server_crashed"]
    crash_diff = (parent["server_crashed"] != target["server_crashed"])
    status_diff = (p_ok != t_ok)

    result_set_diff = False
    row_order_differs = False
    error_diff = False
    if p_ok and t_ok:
        result_set_diff = (sorted_lines(parent["stdout"]) != sorted_lines(target["stdout"]))
        row_order_differs = (not result_set_diff
                             and parent["stdout"].splitlines() != target["stdout"].splitlines())
    elif (not p_ok) and (not t_ok) and not parent["server_crashed"] and not target["server_crashed"]:
        error_diff = (parent["stderr"].strip() != target["stderr"].strip())

    types = []
    if crash_diff:
        types.append("crash_diff")
    if status_diff:
        types.append("status_diff")
    if result_set_diff:
        types.append("result_set_diff")
    if error_diff:
        types.append("error_diff")

    return {"version_diff_observed": bool(types), "diff_types": types,
            "excluded": None, "row_order_differs": row_order_differs,
            "result_set_diff": result_set_diff, "status_diff": status_diff,
            "crash_diff": crash_diff, "error_diff": error_diff}


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", required=True, type=Path)
    parser.add_argument("--commit", required=True, choices=sorted(FULL_REVISIONS))
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--round", required=True, type=int)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--contract-id", default="target_1")
    parser.add_argument("--method", default="version_differential")
    parser.add_argument("--mysqld-timeout", type=int, default=60)
    parser.add_argument("--sql-timeout", type=int, default=60)
    args = parser.parse_args(argv)

    if producer_identity_hash() != PRODUCER_SHA256:
        raise SystemExit("producer source drifted from frozen hash: expected %s got %s"
                         % (PRODUCER_SHA256, producer_identity_hash()))

    label = args.commit
    target_revision = FULL_REVISIONS[label]
    parent_revision = PARENT_REVISIONS[label]
    if args.round < 1 or args.round > 10:
        raise SystemExit("round out of budget")

    candidates = json.loads(Path(args.candidates).read_text(encoding="utf-8"))
    seeds = candidates.get("candidates", [])
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    if not seeds:
        write_json(out / "observations.json",
                   {"run_id": args.run_id, "round": args.round, "observations": []})
        return 0

    sides = {
        "parent": (WORK / f"runtime_parent_{label}", WORK / f"diffdata_parent_{label}"),
        "target": (WORK / f"runtime_{label}", WORK / f"diffdata_{label}"),
    }

    evidence_base = out / "evidence"
    observations = []

    for index, seed in enumerate(seeds):
        cid = seed["candidate_id"]
        fingerprint = digest(seed)
        folder = evidence_base / cid
        folder.mkdir(parents=True, exist_ok=True)
        log("[round %d][%d/%d] candidate %s" % (args.round, index + 1, len(seeds), cid))

        try:
            session_sqls = build_session_sqls(seed, "cand_" + re.sub(r"[^A-Za-z0-9_]", "_", cid))
        except UnsupportedCandidate as exc:
            observations.append({
                "candidate_id": cid,
                "candidate_sha256": fingerprint,
                "reason": str(exc),
                "validity": "unknown",
                "execution": {"status": "not_run"},
            })
            continue

        db = "cand_" + re.sub(r"[^A-Za-z0-9_]", "_", cid)
        sql_text = ("-- database bootstrap runs before candidate sessions\n"
                    "DROP DATABASE IF EXISTS `%s`;\nCREATE DATABASE `%s`;\n" % (db, db)
                    + "".join("-- session %s --\n%s" % (session, script)
                             for session, script in session_sqls.items()))
        sql_file = folder / "sql.sql"
        sql_file.write_text(sql_text, encoding="utf-8")

        results = {}
        for side, (rt_dir, datadir) in sides.items():
            results[side] = run_side(rt_dir, datadir,
                                     parent_revision if side == "parent" else target_revision,
                                     side, cid, db, session_sqls, args.sql_timeout, args.mysqld_timeout, folder)

        diff = classify_diff(results["parent"], results["target"])

        for side, res in results.items():
            (folder / f"{side}.stdout.txt").write_text(res["stdout"], encoding="utf-8")
            (folder / f"{side}.stderr.txt").write_text(res["stderr"], encoding="utf-8")
        write_json(folder / "diff.json", {
            "parent_revision": parent_revision, "target_revision": target_revision,
            "parent": summarize(results["parent"]), "target": summarize(results["target"]),
            "diff": diff,
        })

        version_diff = diff["version_diff_observed"]
        valid = (diff["excluded"] is None)
        status = "completed" if all(not result["startup_failed"]
                                     and not result.get("connection_failed")
                                     and not result.get("preparation_failed")
                                     and not result.get("cleanup_failed")
                                     for result in results.values()) else "failed"
        reason = describe(results, diff, version_diff)

        env = {
            "parent_mysqld_path": str(sides["parent"][0] / "bin" / "mysqld"),
            "target_mysqld_path": str(sides["target"][0] / "bin" / "mysqld"),
            "parent_mysqld_version": mysqld_version(sides["parent"][0]),
            "target_mysqld_version": mysqld_version(sides["target"][0]),
            "build_type": "Debug + ENABLE_GCOV (both sides, identical flags)",
            "label": label,
            "parent_revision": parent_revision,
            "actual_revision": target_revision,
            "isolated_database": db,
            "execution_mode": seed.get("execution_mode", "serial"),
            "session_order": seed["session_order"],
            "configuration": seed["configuration"],
            "network": "none (socket only)",
        }

        raw_evidence = [
            {"path": "evidence/%s/sql.sql" % cid, "sha256": file_sha256(sql_file)},
            {"path": "evidence/%s/diff.json" % cid, "sha256": file_sha256(folder / "diff.json")},
            {"path": "evidence/%s/parent.stdout.txt" % cid, "sha256": file_sha256(folder / "parent.stdout.txt")},
            {"path": "evidence/%s/target.stdout.txt" % cid, "sha256": file_sha256(folder / "target.stdout.txt")},
            {"path": "evidence/%s/parent.stderr.txt" % cid, "sha256": file_sha256(folder / "parent.stderr.txt")},
            {"path": "evidence/%s/target.stderr.txt" % cid, "sha256": file_sha256(folder / "target.stderr.txt")},
        ]

        execution = {
            "candidate_id": cid,
            "actual_revision": target_revision,
            "parent_revision": parent_revision,
            "label": label,
            "environment": env,
            "command": "bootstrap database, then mysql --batch --raw --force once per session in session_order (both builds)",
            "sql_sha256": file_sha256(sql_file),
            "parent": summarize(results["parent"]),
            "target": summarize(results["target"]),
            "diff": diff,
        }
        execution_path = folder / "execution.json"
        write_json(execution_path, execution)

        measurement = {
            "run_id": args.run_id,
            "round": args.round,
            "candidate_id": cid,
            "candidate_sha256": fingerprint,
            "actual_revision": target_revision,
            "contract_id": args.contract_id,
            "producer_sha256": PRODUCER_SHA256,
            "method": args.method,
            "observed_at": now(),
            "raw_evidence": raw_evidence,
            "measurements": {
                "version_diff_observed": version_diff,
                "diff_types": diff["diff_types"],
                "excluded": diff["excluded"],
                "row_order_differs": diff["row_order_differs"],
                "parent_revision": parent_revision,
                "target_revision": target_revision,
            },
        }
        measurement_path = folder / "measurement_target.json"
        write_json(measurement_path, measurement)

        observation = {
            "candidate_id": cid,
            "candidate_sha256": fingerprint,
            "reason": reason,
            "validity": "valid" if valid else "unknown",
            "execution": {
                "status": status,
                "actual_revision": target_revision,
                "environment": env,
                "observed_at": now(),
                "command": execution["command"],
                "runner_sha256": PRODUCER_SHA256,
                "evidence": {"path": "evidence/%s/execution.json" % cid,
                             "sha256": file_sha256(execution_path)},
            },
            "target": {
                "contract_id": args.contract_id,
                "evidence": {"path": "evidence/%s/measurement_target.json" % cid,
                             "sha256": file_sha256(measurement_path)},
            },
        }
        observations.append(observation)

    write_json(out / "observations.json",
               {"run_id": args.run_id, "round": args.round,
                "observations": observations})
    log("wrote %d observations to %s" % (len(observations), out / "observations.json"))
    return 0


def mysqld_version(rt_dir):
    result = run([str(rt_dir / "bin" / "mysqld"), "--version"])
    return result.get("stdout", "").strip()


def summarize(res):
    return {"side": res["side"], "revision": res["revision"],
            "startup_failed": res["startup_failed"], "timed_out": res["timed_out"],
            "server_crashed": res["server_crashed"],
            "cleanup_failed": res.get("cleanup_failed", False), "returncode": res["returncode"],
            "stdout_lines": len(res["stdout"].splitlines()),
            "stderr": res["stderr"].strip()[:4000]}


def describe(results, diff, version_diff):
    if diff["excluded"]:
        if diff["excluded"].startswith("database_preparation_failure"):
            return "database preparation failure (%s); excluded from version-difference" % diff["excluded"]
        if diff["excluded"].startswith("connection_failure"):
            return "connection failure (%s); excluded from version-difference" % diff["excluded"]
        if diff["excluded"].startswith("cleanup_pending"):
            return "server cleanup incomplete (%s); pending review" % diff["excluded"]
        if diff["excluded"].startswith("startup_failure"):
            return "startup/connection failure (%s); excluded from version-difference" % diff["excluded"]
        return "timeout (%s); pending review, not a version difference" % diff["excluded"]
    if version_diff:
        return "version difference observed: %s" % ", ".join(diff["diff_types"])
    return "no version difference observed (parent and target consistent)"


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit as exc:
        raise
    except Exception as exc:  # noqa: BLE001 - surface any failure loudly
        log("PRODUCER ERROR: %r" % exc)
        raise
