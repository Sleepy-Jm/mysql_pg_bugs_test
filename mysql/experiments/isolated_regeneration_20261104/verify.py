"""Verify archive hashes, stage handoff, and recompute comparisons from raw XML offline."""
import collections,hashlib,importlib.util,json
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads((R/p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
exports=read('export_manifest.json')['files']
by_path={x['destination']:x for x in exports};assert len(by_path)==len(exports)
for p,e in by_path.items():
 assert sha(p)==e['exported_sha256'],p
 if not e['transformations']:assert e['original_sha256']==e['exported_sha256']
for t in read('lineage.json')['targets']:
 a=t['artifacts']
 assert (R/a['src2req_output']['path']).read_bytes()==(R/a['req2test_input']['path']).read_bytes()
 for key,v in a.items():
  assert sha(v['path'])==v['exported_sha256']
  assert by_path[v['path']]['original_sha256']==v['original_sha256']
 if t['generation_status']=='blocked':assert 'sql' not in a and not t['executions']
for e in read('source_analysis/manifest.json'):assert sha('source_analysis/'+e['path'])==e['sha256']
for phase,want in [('runtime',{'pass':57,'mismatch':9,'oracle_hold':6}),('supplemental',{'pass':60,'mismatch':12})]:
 spec=importlib.util.spec_from_file_location('archived_'+phase,R/phase/'runner.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 plan=read(phase+'/runtime_plan.json');jobs={j['target']:j for j in plan['jobs']}
 summary=read(phase+'/results/summary.json');assert len(summary['runs'])==12 and summary.get('finished')
 counts=collections.Counter()
 for run in summary['runs']:
  j=jobs[run['target']];assert run['revision']==j['parent_sha' if run['role']=='parent' else 'mysql_target_sha']
  assert run['status']=='completed' and run['returncode']==0 and not run['container_state']['OOMKilled']
  d=f"{phase}/results/{run['revision'][:12]}";trial=d+f"/trial_{run['trial']}"
  assert read(d+'/cleanup.json')['removed']
  inp=f"{phase}/inputs/{run['target']}"
  assert sha(inp+'/test.sql')==run['sql_sha256']==j['inputs']['test.sql']['sha256']
  assert sha(trial+'/submitted.sql')==run['submitted_sha256']
  assert (R/trial/'submitted.sql').read_bytes().endswith((R/inp/'test.sql').read_bytes())
  parsed=module.parse((R/trial/'stdout.xml').read_text(encoding='utf-8'))
  assert parsed==read(trial+'/parsed.json')==read(d+'/trial_1/parsed.json')
  expected=read(inp+'/expected.json')['cases'];assert len(parsed)==len(expected)+1
  assert [x['case_id'] for x in expected]==j['result_set_order']
  for actual,oracle,record in zip(parsed[1:],expected,run['cases']):
   diffs=module.differences(actual,oracle)
   status='oracle_hold' if oracle['case_id'] in j['oracle_hold_case_ids'] else ('mismatch' if diffs else 'pass')
   assert record==dict(case_id=oracle['case_id'],status=status,differences=diffs)
   counts[status]+=1
 assert dict(counts)==want,(phase,counts)
 print(phase+': 12 runs verified; '+str(dict(counts)))
print('PASS: export hashes, handoff, source diffs, frozen SQL, raw XML, per-case oracle checks and repeatability')
