"""Offline verification of the four-boundary MySQL experiment. Never connects to a DB."""
import argparse
from collections import Counter
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path
import re
import sys
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
GENERATED = ROOT.parents[1] / "stage12_generation_20261119/run_20261119_124816/cases/MySQL"
ROLES = ("intro-parent", "intro", "fix-parent", "fix")
TESTS = tuple(f"T{i}" for i in range(1, 6))
CASES = {"396c83fd995b", "410f5267d414", "75bbe1b984ad", "e48f7df66539"}
DECLARATION = re.compile(rb"<\?xml[^?]*\?>")
CONTROL = re.compile(rb"[\x00-\x08\x0b\x0c\x0e-\x1f]")
NIL = "{http://www.w3.org/2001/XMLSchema-instance}nil"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def parse_xml(raw):
    """mysql emits separate XML documents per SELECT. BIT may contain XML-illegal bytes."""
    body = DECLARATION.sub(b"", raw)
    try:
        tree = ET.fromstring(b"<all>" + body + b"</all>")
        recovered = False
    except ET.ParseError:
        # The only binary result in these scripts is BIT(4). Substitute invalid bytes
        # in field *contents* with temporary private-use characters, then restore.
        def field(match):
            data = CONTROL.sub(lambda c: chr(0xE000 + c[0][0]).encode(), match[2])
            return match[1] + data + b"</field>"

        require(not re.search("[\ue000-\ue01f]", body.decode("utf-8")),
                "XML contains the characters reserved for reversible control-byte decoding")
        repaired = re.sub(rb"(<field\b[^>]*>)([^<>]*)</field>", field, body)
        if repaired == body:
            raise
        tree = ET.fromstring(b"<all>" + repaired + b"</all>")
        recovered = True
    require(not (tree.text or "").strip(), "unexpected text outside resultsets")
    sets = []
    for result in tree:
        require(result.tag == "resultset" and result.get("statement") is not None,
                "unexpected XML result element")
        require(not (result.tail or "").strip(), "unexpected text after resultset")
        rows, columns = [], []
        for row in result:
            require(row.tag == "row" and all(c.tag == "field" and "name" in c.attrib for c in row),
                    "unexpected XML row or field")
            names = [c.get("name") for c in row]
            require(not columns or names == columns[0], "field names change within one resultset")
            columns = [names]
            values = [None if c.get(NIL) == "true" else c.text or "" for c in row]
            if recovered:
                values = [re.sub("[\ue000-\ue01f]", lambda m: chr(ord(m[0]) - 0xE000), v)
                          if v is not None else None for v in values]
            rows.append(values)
        sets.append({"sql": result.get("statement"), "columns": columns, "rows": rows})
    return sets, recovered


def typed(text, numeric):
    if text is None or not numeric:
        return text
    try:
        return Decimal(text)
    except InvalidOperation:
        return text


def numeric_fields(case, test, index, width):
    # Only the runtime's XML text is available. Keep all textual columns literal,
    # including explicitly cast CHAR output in the DECIMAL case's second SELECT.
    if case == "410f5267d414" and index == 1:
        return {1}
    if case == "e48f7df66539":
        if test == "T1":
            return {0}
        if test == "T3":
            return {0, 1}
        if test == "T5":
            return {2, 3} if index == 0 else {0, 2, 3}
    return set(range(width))


def signatures(case, test, sets):
    ordered, display, schema = [], [], []
    for index, result in enumerate(sets):
        rows = result["rows"]
        display.append(tuple(map(tuple, rows)))
        fields = numeric_fields(case, test, index, len(rows[0]) if rows else 0)
        ordered.append(tuple(tuple(typed(v, i in fields) for i, v in enumerate(row)) for row in rows))
        schema.append((result["sql"], tuple(result["columns"][0]) if result["columns"] else ()))
    return {"bags": [Counter(rows) for rows in ordered], "order": ordered, "display": display, "schema": schema}


def same(rows):
    return all(row == rows[0] for row in rows[1:])


def oracle(case, test, sets):
    """Only check projections with independent, deterministic expectations."""
    alias, subq, temp, decimal = "396c83fd995b", "75bbe1b984ad", "e48f7df66539", "410f5267d414"
    matching = [(1, 10), (3, 30)]
    windows = [(1, 1, 10, None, None), (2, 1, 20, 20, 10), (3, 1, 30, 20, 20),
               (4, 2, 40, None, None), (5, 2, 50, 50, 40)]
    equal_queries = {
        (alias, "T1"): [(x, 1) for x in range(3, 9)],
        (alias, "T3"): [(1, 10, 11), (2, 20, 22)],
        (alias, "T4"): [(1, 30), (2, 70), (3, 50)],
        (alias, "T5"): [(2, 70, 100), (3, 50, 150), (1, 30, 30)],
        (subq, "T2"): matching,
        (temp, "T1"): [(3, " 3"), (5, "04"), (1, "10")],
        (temp, "T2"): [(Decimal(n), 1) for n in ("1", "1.50", "2", "2.25", "3", "3.75")],
    }
    expected = None
    fields = None
    key = case, test
    if key in equal_queries:
        expected = [equal_queries[key]] * 2
    elif key == (subq, "T4"):
        expected = [matching] * 4
    elif key == (subq, "T5"):
        expected = [matching + [(5, 50)], [(3, 90)]]
    elif key == (temp, "T3"):
        # NO PAD collation, four non-NULL classes, distinct byte lengths 1 and 2.
        # Derived SELECT DISTINCT retains one NULL. GROUP_CONCAT representatives may vary.
        fields, expected = [(0, 1), (0, 1)], [[(4, 3)], [(5, 6)]]
    elif key == (temp, "T4"):
        expected = [[r + (r[2] * 2,) for r in windows], windows]
    elif key == (temp, "T5"):
        # The first column is the binary BIT result or the client's hexadecimal display.
        first = []
        for row in sets[0]:
            value = row[0]
            if isinstance(value, str) and len(value) == 1 and ord(value) <= 15:
                value = ord(value)
            elif isinstance(value, str) and re.fullmatch("0x[0-9a-fA-F]+", value):
                value = int(value, 16)
            first.append((value,) + row[1:])
        sets = [tuple(first)] + list(sets[1:])
        groups = [(None, "x", 1, 60), (1, "x", 2, 30), (1, "z", 1, 50), (2, "y", 2, 70)]
        expected = [groups, groups]
    elif key in {(decimal, "T2"), (decimal, "T3")}:
        # The first SELECT provides the operands. Check the quotients numerically
        # in both SELECTs, allowing six fractional digits for exact-value division
        # (scale 2 and default div_precision_increment 4), or binary64 display error.
        if len(sets) != 2 or len(sets[0]) != 3 or len(sets[1]) != 3:
            return "mismatch"
        tolerance = Decimal("0.0000005") if test == "T2" else Decimal("0.00000000000001")
        for n, first, second in zip((1, 2, 5), *sets):
            if len(first) != 3 or len(second) != 2 or first[:2] != (n, 3):
                return "mismatch"
            for cell in (first[2], *second):
                try:
                    value = Decimal(cell)
                    if not value.is_finite() or abs(value - Decimal(n) / 3) > tolerance:
                        return "mismatch"
                except (InvalidOperation, TypeError):
                    return "mismatch"
        return "match_tolerance"
    elif key in {(decimal, "T1"), (decimal, "T4")}:
        stored = ("0.33", "0.67", "3.33") if test == "T1" else ("0", "1", "3")
        fields = [(0, 1, 3) if test == "T1" else (0, 1), (1,)]
        operands = [(1, 3), (2, 3), (10, 3)]
        first = [pair + (Decimal(n),) for pair, n in zip(operands, stored)] if test == "T1" else operands
        expected = [first, [(Decimal(n),) for n in stored]]
    elif key == (decimal, "T5"):
        fields = [(0, 1, 2), (1,)]
        expected = [[(Decimal(n), 1, Decimal(n)) for n in ("1.005", "1.234", "2.005")],
                    [(Decimal(n),) for n in ("1.01", "1.23", "2.01")]]
    if expected is None:
        return "not_checked"
    if len(expected) != len(sets):
        return "mismatch"
    for i, (got, want) in enumerate(zip(sets, expected)):
        if fields:
            if any(max(fields[i]) >= len(row) for row in got):
                return "mismatch"
            got = tuple(tuple(row[j] for j in fields[i]) for row in got)
        if list(got) != want:
            return "mismatch"
    return "match_projection" if fields else "match"


def result_statements(path):
    # These 20 frozen inputs have only full-line comments, no delimiters inside strings.
    sql = "\n".join(line for line in path.read_text(encoding="utf-8").splitlines()
                    if not line.lstrip().startswith("--"))
    statements = [" ".join(stmt.split()) for stmt in sql.split(";")]
    return [stmt for stmt in statements if re.match(r"^(SELECT|EXECUTE)\b", stmt, re.I)]


def verify_version(directory, case, role, commit, hashes, statements, build_record):
    record = read_json(directory / "results.json")
    require((record["case"], record["role"], record["git"]) == (case, role, commit), "commit/role mismatch")
    require(record.get("server_version") and record.get("session_environment"), "missing environment")
    require(build_record["source_commit"] == commit and build_record["status"] == "built"
            and build_record["build_exit_code"] == 0, "source commit or completed build record mismatch")
    build = (directory / "build-sha256.txt").read_text(encoding="utf-8")
    entries = {name.rsplit("/", 1)[-1]: h for h, name in re.findall(r"(?m)^([a-f0-9]{64})\s+\*?(.+?)\s*$", build)}
    for binary in ("mysql", "mysqld"):
        require(binary in entries and record["bin_sha256"][binary] == entries[binary]
                and build_record["binary_sha256"]["bin/" + binary] == entries[binary],
                f"{binary} build fingerprint mismatch")
    require(set(record["tests"]) == set(TESTS), "expected five scripts")
    observed = {}
    detail = {}
    for test in TESTS:
        sample = record["tests"][test]
        require(sample["input_sha256"] == hashes[f"{case}/{test}.sql"], f"{test} input SHA mismatch")
        require([t["round"] for t in sample["trials"]] == [1, 2, 3], f"{test} round identity")
        trials = []
        for trial in sample["trials"]:
            stem = f"{test}-{trial['round']}"
            raw = (directory / (stem + ".xml")).read_bytes()
            diag = (directory / (stem + ".stderr.txt")).read_bytes().decode("utf-8", errors="replace")
            require(sha(raw) == trial["stdout_sha256"] and diag == trial["stderr"], f"{stem} raw evidence mismatch")
            sets, repaired = parse_xml(raw)
            if repaired:
                require(trial.get("parse_error") and "sets" not in trial, f"{stem} expected XML parse diagnostic")
            else:
                require(trial.get("sets") == sets and "parse_error" not in trial, f"{stem} serialized rows mismatch")
            exit_code = trial["exit"]
            require(type(exit_code) is int, f"{stem} invalid client exit")
            actual_sql = [" ".join(result["sql"].split()) for result in sets]
            expected_sql = statements[test]
            require(actual_sql == expected_sql[:len(sets)], f"{stem} XML statements differ from input")
            require(exit_code != 0 or len(sets) == len(expected_sql), f"{stem} missing successful resultset")
            facts = signatures(case, test, sets)
            facts.update(exit=exit_code, error_codes=re.findall(r"(?m)^ERROR (\d+)(?: \(([0-9A-Z]+)\))?", diag),
                         diagnostics=re.sub(rf"\bs12_{test.lower()}_r[123]\b", "s12_schema", diag),
                         xml_control_bytes=sorted({f"0x{byte[0]:02x}" for byte in CONTROL.findall(raw)}) if repaired else [],
                         oracle="execution_error" if exit_code else oracle(case, test, facts["order"]))
            trials.append(facts)
        observed[test] = trials
        detail[test] = {
            "exits": [t["exit"] for t in trials], "error_codes": [t["error_codes"] for t in trials],
            "oracle": [t["oracle"] for t in trials],
            "xml_control_bytes_by_round": [t["xml_control_bytes"] for t in trials],
            "stable": {key: same([t[key] for t in trials]) for key in
                       ("exit", "error_codes", "bags", "order", "display", "schema", "diagnostics")},
        }
    return observed, detail


def compare(before, after):
    if before is None or after is None:
        return {"status": "missing_or_invalid_evidence"}
    samples = before + after
    stable = {key: same([x[key] for x in before]) and same([x[key] for x in after]) for key in
              ("exit", "error_codes", "diagnostics", "bags", "order", "display", "schema")}
    delta = {key: (before[0][key] != after[0][key]) if value else None for key, value in stable.items()}
    # Different row values cannot establish a change in row ordering; different
    # ordered values cannot isolate a change of textual representation either.
    if delta["bags"] is not False:
        delta["order"] = None
    if delta["order"] is not False:
        delta["display"] = None
    if not stable["exit"] or not stable["bags"]:
        status = "repeat_variation"
    elif any(t["exit"] != 0 for t in samples):
        status = "execution_error"
    elif delta["bags"]:
        status = "value_or_multiplicity_difference"
    elif not stable["order"]:
        status = "repeat_order_variation"
    elif delta["order"]:
        status = "order_only"
    elif delta["display"]:
        status = "representation_only"
    else:
        status = "same_values_and_order"
    return {"status": status, "changed": delta}


def audit(root, sources):
    plan, hashes = read_json(root / "plan.json"), read_json(root / "input-hashes.json")
    builds = {(r["case"], r["role"]): r for r in read_json(root / "build-records.json")["records"]}
    require(len(plan) == 4 and {p["case"] for p in plan} == CASES, "expected four named MySQL cases")
    require(set(hashes) == {f"{case}/{test}.sql" for case in CASES for test in TESTS}, "input manifest keys")
    report = {"planned_versions": 16, "planned_trials": 240, "versions": {}, "boundaries": {},
              "script_coverage": {}, "pending": [], "invalid": {}}
    for entry in plan:
        case = entry["case"]
        require(set(entry["versions"]) == set(ROLES), f"{case} role identities")
        require(all(re.fullmatch("[0-9a-f]{40}", h) for h in entry["versions"].values())
                and entry["versions"]["intro"].startswith(case), f"{case} commit records")
        statements = {}
        for test in TESTS:
            name = f"{test}.sql"
            expected = hashes[f"{case}/{name}"]
            source = sources / case / "sql" / name
            require(sha(source.read_bytes()) == expected, f"frozen SQL mismatch: {case}/{name}")
            statements[test] = result_statements(source)
            if (root / "inputs").exists():
                require(sha((root / "inputs" / case / name).read_bytes()) == expected, f"staged SQL mismatch: {case}/{name}")
        versions = {}
        for role, commit in entry["versions"].items():
            key = case + "/" + role
            directory = root / "evidence" / case / role
            if not (directory / "results.json").exists():
                report["pending"].append(key)
                continue
            try:
                versions[role], report["versions"][key] = verify_version(
                    directory, case, role, commit, hashes, statements, builds[case, role])
            except (ValueError, OSError, KeyError, TypeError, ET.ParseError) as error:
                report["invalid"][key] = str(error)
        for test in TESTS:
            trials = [trial for version in versions.values() for trial in version[test]]
            exits = [t["exit"] for t in trials]
            coverage = "pending"
            if len(exits) == len(ROLES) * 3:
                if not any(exits):
                    coverage = "success_all"
                elif 0 not in exits:
                    coverage = "error_all"
                else:
                    coverage = "mixed"
            report["script_coverage"][case + "/" + test] = coverage
            report["boundaries"][case + "/" + test] = {
                side: compare(versions.get(side + "-parent", {}).get(test), versions.get(side, {}).get(test))
                for side in ("intro", "fix")}
    tests = [x for v in report["versions"].values() for x in v.values()]
    exits = [code for x in tests for code in x["exits"]]
    report["counts"] = {"verified_versions": len(report["versions"]), "verified_trials": len(exits),
                        "successful_trials": exits.count(0), "error_trials": len(exits) - exits.count(0),
                        "script_coverage": dict(Counter(report["script_coverage"].values())),
                        "oracle_rounds": dict(Counter(outcome for x in tests for outcome in x["oracle"])),
                        "comparisons": dict(Counter(v["status"] for s in report["boundaries"].values() for v in s.values()))}
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="execution directory containing plan and evidence")
    parser.add_argument("--sources", type=Path, default=GENERATED, help="original generation's MySQL case directory")
    parser.add_argument("--output", type=Path, help="write complete JSON report here")
    parser.add_argument("--partial", action="store_true", help="allow pending result files during collection")
    options = parser.parse_args()
    report = audit(options.root, options.sources)
    if options.output:
        options.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"counts": report["counts"], "invalid": report["invalid"], "pending": report["pending"]}))
    return 1 if report["invalid"] or (report["pending"] and not options.partial) else 0


if __name__ == "__main__":
    sys.exit(main())
