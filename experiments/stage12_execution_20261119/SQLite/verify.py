"""Verify immutable SQL, build identity, repeatability, and the wrong-count result."""
from collections import Counter
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GENERATED = ROOT.parents[1] / "stage12_generation_20261119/run_20261119_124816/cases/SQLite"
COUNT_CASE = "d1ba200234f40b84"
SCRIPTS = {f"T{i}" for i in range(1, 6)}
INTERVALS = [
    ("intro-parent", "intro"),
    ("fix-parent", "fix"),
    ("default-parent", "default-enabled"),
    ("optin-intro-parent", "optin-intro"),
]
COUNT_PAIRS = {
    "intro-parent": [5, 5],
    "intro": [5, 5],
    "optin-intro-parent": [5, 5],
    "optin-intro": [7, 5],
    "default-parent": [3, 5],
    "default-enabled": [7, 5],
    "fix-parent": [7, 5],
    "fix": [5, 5],
}


def read_json(path):
    return json.loads(path.read_text(encoding="utf8"))


def result_sets(trial):
    return [statement["rows"] for statement in trial["statements"] if statement["columns"]]


def verify_role(case, role, revision, hashes, totals):
    record = read_json(ROOT / "evidence" / case / (role + ".json"))
    build = record["build"]
    assert (record["case"], record["role"]) == (case, role)
    assert record["git"] == build["revision"] == revision["git"]
    assert build["manifest"][:36] in record["source_id"]
    assert build["host_arch"] == "x86_64"
    assert ("-DSQLITE_COUNTOFVIEW_OPTIMIZATION" in build["cflags"].split()) == bool(
        revision.get("count_of_view_optin")
    )
    if revision["fossil"]:
        assert build["manifest"].startswith(revision["fossil"])

    assert set(record["tests"]) == SCRIPTS
    totals["role_runs"] += 1
    for script, test in record["tests"].items():
        file_name = script + ".sql"
        original = (GENERATED / case / "sql" / file_name).read_bytes()
        assert hashlib.sha256(original).hexdigest() == hashes[case + "/" + file_name] == test["input_sha256"]
        assert len(test["trials"]) == 3
        for trial in test["trials"]:
            totals["script_error" if trial["error"] else "script_success"] += 1
    return record["tests"]


def compare(before, after):
    if any(trial["error"] for trial in before + after):
        return "execution_error"
    for repeats in (before, after):
        if any(result_sets(trial) != result_sets(repeats[0]) for trial in repeats[1:]):
            return "unstable"
    return "same" if result_sets(before[0]) == result_sets(after[0]) else "different"


def read_counts(trials):
    pairs = []
    for trial in trials:
        values = []
        for rows in result_sets(trial):
            assert len(rows) == 1 and len(rows[0]) == 1
            kind, value = rows[0][0]
            assert kind == "integer"
            values.append(value)
        pairs.append(values)
    return pairs


def main():
    plan = read_json(ROOT / "plan.json")
    hashes = read_json(ROOT / "input-hashes.json")
    totals = Counter()
    intervals = {}
    count_pairs = {}
    for case in plan:
        name = case["case"]
        roles = {}
        for role, revision in case["versions"].items():
            tests = verify_role(name, role, revision, hashes, totals)
            roles[role] = tests
            if name == COUNT_CASE:
                count_pairs[role] = read_counts(tests["T2"]["trials"])
        for before, after in INTERVALS:
            if before in roles:
                intervals[f"{name}/{before}..{after}"] = {
                    script: compare(roles[before][script]["trials"], roles[after][script]["trials"])
                    for script in sorted(SCRIPTS)
                }

    assert totals == {"role_runs": 20, "script_success": 276, "script_error": 24}
    assert count_pairs == {role: [pair] * 3 for role, pair in COUNT_PAIRS.items()}
    fix_differences = [
        (interval, script)
        for interval, scripts in intervals.items() if interval.endswith("/fix-parent..fix")
        for script, outcome in scripts.items() if outcome == "different"
    ]
    assert fix_differences == [(COUNT_CASE + "/fix-parent..fix", "T2")]
    summary = {
        "totals": dict(totals),
        "comparator": "per-statement result rows in returned order, including types, with three independent in-memory databases per revision and script",
        "intervals": intervals,
        "count_case_T2_target_and_control": count_pairs,
        "confirmed_known_cases": {COUNT_CASE: ["T2"]},
    }
    (ROOT / "summary.json").write_bytes((json.dumps(summary, ensure_ascii=False, indent=2) + "\n").encode())
    print(dict(totals))


if __name__ == "__main__":
    main()
