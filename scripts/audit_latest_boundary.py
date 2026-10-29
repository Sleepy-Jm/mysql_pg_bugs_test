"""Check the completed phase from saved files only. No database/network access."""
from pathlib import Path
import json,hashlib,collections
ROOT=Path(__file__).resolve().parents[1]
def load(p):return json.loads((ROOT/p).read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
P='experiments/boundary_completed_20261029'
x=load(P+'/results.json');s=load(P+'/summary.json')
assert len(x['items'])==len({r['task_id'] for r in x['items']})==106
assert collections.Counter(r['boundary_status'] for r in x['items'])=={'observed_new_at_release':15,'pre_existing':91}
assert collections.Counter(r['execution_status'] for r in x['items'])=={'completed_and_adjudicated':95,'historical_comparable_pair_reused':11}
assert load('cases/version_boundary_items.json')==x['items']
assert x['totals']==s['totals']
assert sum(r['new_actual_runs'] for r in x['items'])==95
assert sum(r['new_attempt_records'] for r in x['items'])==97
manifest=load(P+'/source_manifest.json')['files'];sources={r['source']:r for r in load('docs/excluded_files.json')['files']};sources.update({r['source']:r for r in load('docs/migration_manifest.json')['files']});sources.update({r['source']:r for r in manifest})
for row in manifest:
 if row.get('destination'):assert sha(ROOT/row['destination'])==row['destination_sha256'],row['destination']
def resolve(path):
 prefix='<ORIGINAL_PROJECT>/'
 path=path.replace(chr(92),'/')
 assert path.startswith(prefix),path
 return path[len(prefix):]
submitted=[];failed=[];record_refs=0;decisions=0
for row in x['items']:
 assert int(row['target_version'].split('.')[-1])-1==int(row['previous_version'].split('.')[-1])
 for wrapper in row['new_records']:
  source=sources[resolve(wrapper['path'])]
  assert source['sha256']==wrapper['sha256']
  assert source.get('destination'),source['source']
  rr=[json.loads(line) for line in (ROOT/source['destination']).read_text(encoding='utf8').splitlines() if line.strip()]
  assert wrapper['record'] in rr
  rec=wrapper['record'];record_refs+=1
  if rec.get('sql_submitted'):
   assert rec['actual_version']==row['previous_version']
   submitted.append((rec['task_id'],rec['run_id']))
  else:failed.append(rec)
 for path,expected in (row.get('decision') or {}).get('evidence_hashes',{}).items():
  source=sources[resolve(path)]
  assert source['sha256']==expected
  decisions+=1
assert record_refs==97 and len(submitted)==len(set(submitted))==95 and len(failed)==2
assert s['totals']['historical_pairs']==11 and s['totals']['unresolved']==0
assert s['retry_update']['new_sql_runs_this_retry']==2
assert s['old_target_stage_counters']=={'candidate_items':895,'executed_items':125,'actual_runs':215,'reproduced_items':106,'changed_by_this_phase':False}
print('PASS: completed boundary 15/91/0; new SQL 95; attempts 97; reused pairs 11; failures retained 2; record refs',record_refs,'decision hash refs',decisions)
