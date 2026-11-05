from pathlib import Path
import json,hashlib,collections
r=Path(__file__).resolve().parents[1]
def load(p):return json.loads((r/p).read_text(encoding='utf8'))
x=load('cases/report_version_items.json');y=load('experiments/baseline_20261029/boundary_items.json')
assert len(x)==len({a['task_id'] for a in x})==895
assert sum(bool(a['executed']) for a in x)==125
assert sum(a['current_category']=='reproduced' for a in x)==106
assert len({a['report_id'] for a in x if a['current_category']=='reproduced'})==99
assert len(y)==106
assert dict(collections.Counter(a['category'] for a in y))=={'前版正常、目标版异常':6,'前版已有同样异常':5,'条件不可比或证据不足':95}
for a in x:
 assert a['scope_status']=='included_explicit_version'
 assert a['target_version'] in a['official_version_field'] or (a['version_match']['match_kind']=='explicit_slash_shorthand' and a['task_id']=='mysql-114255-8.0.35' and a['official_version_field']=='8.0.34/35')
for a in load('docs/migration_manifest.json')['files']:
 assert hashlib.sha256((r/a['destination']).read_bytes()).hexdigest()==a['destination_sha256'],a['destination']
print('PASS: scope 895; executed 125; reproduced 106 / 99 reports; boundary 6/5/95; migration hashes verified')
