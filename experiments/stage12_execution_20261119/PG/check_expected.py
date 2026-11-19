"""Independent hand calculation for the 15 non-ICU PostgreSQL scripts."""
import json
from pathlib import Path

root = Path(__file__).parent
def both(rows):
    return [rows, rows]
expected = {
    "16dc2703c541": {
        "T1": both(["3|30", "4|<NULL>"]),
        "T2": [[], ["2|20", "3|30"]],
        "T3": both([]),
        "T4": both(["3|30", "4|40"]),
        "T5": both(["1|3|30", "2|3|30"]),
    },
    "8edd0e79460b": {
        "T1": both(["b", "d", "c", "a"]),
        "T2": both(["1|31", "2|12"]),
        "T3": both(["10", "20", "30"]),
        "T4": [["10", "20"], ["10"], [], ["40"], ["30"]]*2,
        "T5": both(["y", "z", "x"]),
    },
    "9d9c02ccd1ae": {
        "T1": both(["1|1", "2|2", "3|3"]),
        "T2": both(["1|1|1", "1|2|2", "2|1|1", "2|2|2"]),
        "T3": both(["1|5", "2|4", "3|3"]),
        "T4": both([f"{a}|5" for a in range(1, 6)]),
        "T5": both(["3|3|3", "4|4|2", "5|5|1"]),
    },
}
checks = []
for item in json.loads((root/"observations.json").read_text(encoding="utf-8")):
    case, test = item["case"], item["script"].split(".")[0]
    if case not in expected:
        continue
    rows = expected[case][test]
    for role, obs in item["observed"].items():
        actual = [rs["rows"] for rs in obs["resultsets"]]
        checks.append({"case": case, "test": test, "role": role, "observed_repeat_count": obs["repeats"],
                       "all_repeats_identical": obs["stable"], "expected_rows": rows,
                       "matches": actual==rows and obs["client_exit"]==0 and not obs["sql_errors"]})
(root/"expected_check.json").write_text(json.dumps(checks, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

case = root/"9d9c02ccd1ae"
supplement = {}
for role in ["secondary_fix_parent", "secondary_fixed"]:
    result = case/role
    if not (result/"complete.json").exists():
        continue
    runs = []
    for path in sorted((result/"runs"/"T4").glob("r*")):
        status = json.loads((path/"status.json").read_text(encoding="utf-8"))
        runs.append({"repeat": status["repeat"], "client_exit": status["client_exit"],
                     "errors": status["sql_errors"], "script_sha256": status["source_sha256"],
                     "output": (path/"stdout.txt").read_text(encoding="utf-8")})
    supplement[role] = {"sha": status["sha"], "runs": runs}
if len(supplement) == 2:
    supplement["fix_reference"] = "https://github.com/postgres/postgres/commit/53823a06be6f40d88d8e3ba45045ecee1a21fc5e"
    (root/"secondary_check.json").write_text(json.dumps(supplement, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
