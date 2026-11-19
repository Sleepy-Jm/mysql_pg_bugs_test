"""Summarize observed rows, SQL diagnostics and both exact revision boundaries."""
import csv
import hashlib
import json
import re
from pathlib import Path

base = Path(__file__).resolve().parent
roles = ["parent", "introducing", "fix_parent", "fixed"]
result = []
summaries = []
for case in sorted((p for p in base.iterdir() if re.fullmatch(r"[0-9a-f]{12}", p.name))):
    for script in sorted((case / "sql").glob("T*.sql")):
        observed = {}
        for role in roles:
            runs = []
            for where in sorted((case / role / "runs" / script.stem).glob("r*")):
                if not (where/"status.json").exists():
                    continue
                status = json.loads((where / "status.json").read_text(encoding="utf-8"))
                if any(status[f"{stream}_sha256"] != hashlib.sha256((where/f"{stream}.txt").read_bytes()).hexdigest() for stream in ("stdout", "stderr")):
                    raise ValueError(f"Original result hash mismatch in {where}")
                if status["source_sha256"] != hashlib.sha256(script.read_bytes()).hexdigest():
                    raise ValueError(f"Original input mismatch in {where}")
                out = (where/"stdout.txt").read_text(encoding="utf-8")
                sets = []
                pending = []
                for line in out.splitlines():
                    match = re.fullmatch(r"\((\d+) rows?\)", line)
                    if match:
                        if not pending or len(pending[1:]) != int(match.group(1)):
                            raise RuntimeError(f"Unrecognized psql output at {where}: {pending}")
                        sets.append({"columns": pending[0], "rows": pending[1:]})
                        pending = []
                    else:
                        pending.append(line)
                if pending:
                    raise RuntimeError(f"Unparsed psql output at {where}: {pending}")
                runs.append((status, sets))
            if not runs:
                continue
            samples = [{k:v for k,v in s.items() if k in {
                "client_exit", "sql_errors", "warnings", "stdout_sha256", "stderr_sha256"}}
                for s, _ in runs]
            observed[role] = {"repeats": len(runs), "stable": all(x==samples[0] for x in samples),
                              **samples[0], "resultsets": runs[0][1]}
        result.append({"case": case.name, "script": script.name, "observed": observed})
        summary = {"case": case.name, "script": script.name}
        for r in roles:
            if r in observed:
                o = observed[r]
                summary[r] = f"{o['repeats']}x; rc={o['client_exit']}; errors={len(o['sql_errors'])}; warn={len(o['warnings'])}; sets={len(o['resultsets'])}; stable={o['stable']}"
        for name, a, b in [("introducing_boundary", roles[0], roles[1]), ("fix_boundary", roles[2], roles[3])]:
            if a in observed and b in observed:
                aa, bb = observed[a], observed[b]
                summary[name] = "same rows" if aa["resultsets"] == bb["resultsets"] else "different or missing rows"
        summaries.append(summary)
(base/"observations.json").write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
with (base/"matrix.csv").open("w", newline="", encoding="utf-8") as f:
    out = csv.DictWriter(f, fieldnames=["case", "script", *roles, "introducing_boundary", "fix_boundary"])
    out.writeheader()
    out.writerows(summaries)
