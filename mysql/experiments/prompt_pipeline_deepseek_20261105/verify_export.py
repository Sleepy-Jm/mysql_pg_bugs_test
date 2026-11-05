from pathlib import Path
import hashlib, json, re, xml.etree.ElementTree as ET
root = Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
checks = []
bundle = root / "input_bundle"
for line in (bundle / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
    if not line.strip(): continue
    expected, rel = line.split(None, 1)
    rel = rel.strip().lstrip("*")
    if sha(bundle / rel) != expected: raise SystemExit(f"input hash mismatch: {rel}")
    checks.append(rel)
manifest = json.loads((root / "run_manifest.json").read_text(encoding="utf-8"))
summary = json.loads((root / "server_evidence" / "summary.json").read_text(encoding="utf-8"))
targets = list(manifest["targets"])
if len(targets) != 3 or len(summary["groups"]) != 3: raise SystemExit("expected three targets and groups")
xml_count = 0
for target in targets:
    expected = manifest["targets"][target]["generated_sql_sha256"]
    if sha(root / target / "generated.sql") != expected: raise SystemExit(f"generated SQL hash mismatch: {target}")
    if sha(root / "server_evidence" / "input" / f"{target}.sql") != expected: raise SystemExit(f"server SQL hash mismatch: {target}")
    for side in ("parent", "target"):
        d = root / "server_evidence" / "results" / target / side
        result = json.loads((d / "result.json").read_text(encoding="utf-8"))
        if len(result["trials"]) != 3 or any(t["returncode"] != 0 for t in result["trials"]):
            raise SystemExit(f"execution count/return code mismatch: {target}/{side}")
        for output in sorted(d.glob("trial-*.stdout.xml")):
            data = re.sub(br'<\?xml[^?]*\?>', b'', output.read_bytes())
            ET.fromstring(b'<root>' + data + b'</root>')
            xml_count += 1
for group in summary["groups"]:
    if len(group["comparisons"]) != 3 or any(c["status"] != "no_observed_difference" for c in group["comparisons"]):
        raise SystemExit(f"comparison mismatch: {group['case']}")
if xml_count != 18: raise SystemExit(f"expected 18 XML outputs, got {xml_count}")
if manifest["database_execution_summary"]["full_script_executions"] != 18:
    raise SystemExit("execution total mismatch")
print(f"OK: {len(checks)} input hashes; 3 targets; 18 successful runs; {xml_count} XML outputs parsed.")
