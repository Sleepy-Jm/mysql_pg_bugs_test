"""Build each pinned PostgreSQL source tree and run the original generated scripts."""
import csv
import hashlib
import json
import os
import pwd
import re
import shutil
import subprocess
import sys
import tarfile
import time
from pathlib import Path

OUT = Path("/out")
WORK = Path("/var/tmp/stage12pg")
SOURCE = WORK / "source"
INSTALL = Path("/opt/stage12pg")
RUNTIME = WORK / "runtime"
BIN = INSTALL / "bin"
ADMIN = "run_admin"
USER = "test_runner"
SOCKET = RUNTIME / "socket"
CHILD_ENV = {**os.environ, "LC_ALL": "C", "TZ": "UTC"}
PORT = "57439"

def sha256(path):
    with path.open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()

def record(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")

def run(cmd, log, *, cwd=None, user=False, timeout=None, check=True, environment=None):
    args = [str(x) for x in cmd]
    if user:
        args = ["/usr/sbin/runuser", "-u", "nobody", "--", *args]
    with log.open("ab") as f:
        return subprocess.run(args, check=check, env=environment or CHILD_ENV, cwd=cwd,
                              stdout=f, stderr=subprocess.STDOUT, timeout=timeout)

def build(row, dest):
    archive = Path("/handoff") / (row["sha"] + ".tar.gz")
    while not archive.exists():
        time.sleep(4)
    if SOURCE.exists():
        shutil.rmtree(SOURCE)
    if INSTALL.exists():
        shutil.rmtree(INSTALL)
    SOURCE.mkdir()
    with tarfile.open(archive) as f:
        root = f.next().name.split("/")[0]
    if root != "postgres-" + row["sha"]:
        raise ValueError(f"Archive identity {root}")
    run(["tar", "xf", archive, "--strip-components=1", "-C", SOURCE], dest/"build.log")
    env = {**CHILD_ENV, "CC": "ccache gcc", "CCACHE_DIR": "/var/tmp/stage12pg/ccache",
           "CFLAGS": "-O1 -g0"}
    if row["case"] == "8edd0e79460b":
        env["CPPFLAGS"] = "-DU_DEFINE_FALSE_AND_TRUE=1"
    cfg = ["./configure", "--prefix=" + str(INSTALL), "--with-icu",
           "--without-readline", "--without-zlib"]
    run(cfg, dest/"build.log", cwd=SOURCE, environment=env)
    run(["make", "-s", "-j4"], dest/"build.log", cwd=SOURCE, environment=env)
    run(["make", "-s", "-j4", "install"], dest/"build.log", cwd=SOURCE, environment=env)
    run(["make", "-s", "-j4", "-C", "contrib/auto_explain", "install"], dest/"build.log", cwd=SOURCE, environment=env)
    record(dest/"build.json", {**row, "source_url":
           "https://codeload.github.com/postgres/postgres/tar.gz/" + row["sha"],
           "sha256_archive": sha256(archive), "source_root": root, "configure": cfg,
           "CFLAGS": env["CFLAGS"], "CPPFLAGS": env.get("CPPFLAGS", ""), "icu": subprocess.check_output(
               ["pkg-config", "--modversion", "icu-i18n"], text=True).strip(),
           "postgres_version": subprocess.check_output([BIN/"postgres", "--version"], text=True).strip(),
           "binary_sha256": {n: sha256(BIN/n) for n in ["postgres", "psql"]}})

def psql(user, db, *args):
    return [BIN/"psql", "-X", "-h", SOCKET, "-p", PORT, "-U", user, "-d", db, *args]

def pgctl(datadir, action, log, serverlog=None, plans=False):
    args = [BIN/"pg_ctl", "-D", datadir, "-w"]
    if action == "start":
        args += ["-l", serverlog, "-o", f"-p {PORT} -k {SOCKET} -c listen_addresses='' -c unix_socket_permissions=0700 -c fsync=off -c synchronous_commit=off -c full_page_writes=off"]
        if plans:
            args[-1] += " -c session_preload_libraries=auto_explain -c auto_explain.log_min_duration=0 -c auto_explain.log_format=text"
    else:
        args += ["-m", "fast"]
    run([*args, action], log, user=True, timeout=65)

def execute(row, dest):
    if RUNTIME.exists():
        shutil.rmtree(RUNTIME)
    SOCKET.mkdir(parents=True)
    identity = pwd.getpwnam("nobody")
    for path in [RUNTIME, SOCKET]:
        os.chown(path, identity.pw_uid, identity.pw_gid)
        path.chmod(0o700)
    base = RUNTIME/"template"
    params = ["--no-locale", "--encoding=UTF8", "--auth=trust", "-U", ADMIN, "-D", base]
    run([BIN/"initdb", *params], dest/"setup.log", user=True)
    pgctl(base, "start", dest/"setup.log", RUNTIME/"base.log")
    try:
        run(psql(ADMIN, "postgres", "-v", "ON_ERROR_STOP=1", "-c",
                 f"CREATE ROLE {USER} LOGIN CREATEDB NOSUPERUSER NOCREATEROLE", "-c",
                 f"CREATE DATABASE casework OWNER {USER}"), dest/"setup.log", user=True)
        run(psql(USER, "casework", "-c",
                 "SELECT version(), current_user, current_setting('server_version_num'), current_setting('listen_addresses'), rolsuper, rolcreatedb FROM pg_roles WHERE rolname=current_user"),
            dest/"runtime-version.txt", user=True)
    finally:
        pgctl(base, "stop", dest/"setup.log")
    inputs = Path("/inputs")/row["case"]/"sql"
    for repeat in [1, 2, 3]:
        for script in sorted(inputs.glob(row.get("script_glob", "T*.sql"))):
            result_dir = dest/"runs"/script.stem/f"r{repeat}"
            result_dir.mkdir(parents=True, exist_ok=True)
            d = RUNTIME/"data"
            run(["cp", "-a", base, d], dest/"setup.log", user=True)
            serverlog = RUNTIME/"server.log"
            serverlog.unlink(missing_ok=True)
            pgctl(d, "start", dest/"setup.log", serverlog, plans=(repeat == 1))
            try:
                args = psql(USER, "casework", "-q", "-A", "-F", "|", "-P", "null=<NULL>",
                            "-P", "footer=on", "-v", "ON_ERROR_STOP=0", "-f", script)
                with (result_dir/"stdout.txt").open("wb") as out, (result_dir/"stderr.txt").open("wb") as err:
                    finished = subprocess.run(["/usr/sbin/runuser", "-u", "nobody", "--", *args],
                        env=CHILD_ENV, stdout=out, stderr=err, timeout=45)
                errors = (result_dir/"stderr.txt").read_text().splitlines()
                record(result_dir/"status.json", {
                    **row, "script": script.name, "source_sha256": sha256(script),
                    "repeat": repeat, "client_exit": finished.returncode, "sql_errors": [
                        s for s in errors if re.search(r"\b(?:ERROR|FATAL|PANIC):", s)],
                    "warnings": [s for s in errors if "WARNING:" in s],
                    "stdout_sha256": sha256(result_dir/"stdout.txt"), "stderr_sha256": sha256(result_dir/"stderr.txt")})
            finally:
                pgctl(d, "stop", dest/"setup.log")
                if repeat == 1:
                    shutil.copyfile(serverlog, result_dir/"server-plans.log")
                shutil.rmtree(d)

if __name__ == "__main__":
    WORK.mkdir(exist_ok=True)
    manifest = "secondary_versions.csv" if "--secondary" in sys.argv else "versions.csv"
    with (OUT/manifest).open(encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        dest = OUT/row["case"]/row["role"]
        if (dest/"complete.json").exists():
            continue
        dest.mkdir(parents=True, exist_ok=True)
        print("building", row, flush=True)
        build(row, dest)
        print("running", row, flush=True)
        execute(row, dest)
        record(dest/"complete.json", {**row, "run_count": len(list((dest/"runs").glob("*/r*/status.json")))})
        print("complete", row, flush=True)
