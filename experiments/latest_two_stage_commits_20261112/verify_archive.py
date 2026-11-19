"""Read-only verification of frozen inputs and execution evidence; no API/database calls."""
import hashlib
import json
from pathlib import Path
import re
import runpy
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent

def load(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

manifest = load(ROOT / 'integrity.json')
for name, expected in manifest['files'].items():
    assert digest(ROOT / name) == expected, name
provenance = load(ROOT / 'provenance.json')
for item in provenance['byte_preserved_copies']:
    assert digest(ROOT / item['destination']) == item['sha256'], item['destination']
scripts = executions = differences = invalid = 0
for meta in load(ROOT / 'summary.json')['targets']:
    d = ROOT / meta['target_id']
    summary = load(d / 'summary.json')
    handoff = (d / 'generation/stage1_output.txt').read_text(encoding='utf-8')
    filled = (d / 'generation/stage2_prompt_filled.txt').read_text(encoding='utf-8')
    assert handoff.strip() and handoff in filled
    assert '{{STAGE1_OUTPUT}}' not in filled
    assert summary['feedback_used'] is False
    for case in summary['cases']:
        n = int(case['case_id'][1:])
        assert digest(d / f'sql/sql_{n}.sql') == case['sql_sha256']
        scripts += 1
        differences += case['status'] == 'stable_result_difference'
        invalid += case['status'] == 'sql_error_not_valid_for_differential_conclusion'
        for side in ('parent','target'):
            assert len(case['trials'][side]) == 3
            for t in case['trials'][side]:
                stem = d / f'evidence/sql_{n}/{side}/trial-{t["repeat"]}'
                stdout = stem.with_suffix('.stdout.xml')
                stderr = stem.with_suffix('.stderr.txt')
                assert digest(stdout) == t['stdout_sha256']
                assert digest(stderr) == t['stderr_sha256']
                xml = re.sub(rb'<\?xml[^?]*\?>', b'', stdout.read_bytes())
                assert len(ET.fromstring(b'<all>' + xml + b'</all>').findall('resultset')) == len(t['resultsets'])
                errors = re.findall(r'ERROR\s+\d+[^\r\n]*', stderr.read_text(encoding='utf-8',errors='replace'))
                assert errors == t['sql_errors']
                executions += 1
assert (scripts, executions, differences, invalid) == (15, 90, 6, 3)
print(f'PASS: {len(manifest["files"])} file hashes; complete Stage1 handoffs; {scripts} scripts, {executions} executions; {differences} stable differences; {invalid} SQL-error cases')
runpy.run_path(str(ROOT / 'item_property_recalculation_248c7f7c227e/sql_rerun_20261118/verify.py'), run_name='__main__')
