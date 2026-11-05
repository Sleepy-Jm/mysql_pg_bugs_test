import datetime, hashlib, json, os, re, subprocess, time
from pathlib import Path
from decimal import Decimal
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent
IMAGE='sha256:b2f51e7795136616ef1b1a35c529fb290dfdfe8e5f7fdd348248b5991f38674d'
OLD=Path('/EXPERIMENT_STORAGE/mysql-intro-bisect-20261103')
PREV=Path('/EXPERIMENT_STORAGE/mysql-three-prompts-20261104-a')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):
 p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')
def cmd(a,data=None,check=True,timeout=120):
 r=subprocess.run(list(map(str,a)),input=data,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=timeout)
 if check and r.returncode: raise RuntimeError(str(a)+'\n'+r.stderr.decode(errors='replace'))
 return r
def txt(a): return cmd(a).stdout.decode().strip()
def parse(raw):
 root=ET.fromstring('<all>'+re.sub(r'<\?xml[^?]*\?>','',raw)+'</all>')
 out=[]
 for rs in root.findall('resultset'):
  rows=[]; columns=[]
  for row in rs.findall('row'):
   fs=row.findall('field'); names=[f.attrib['name'] for f in fs]
   assert not columns or columns==names
   columns=names
   rows.append([None if any(k.endswith('}nil') and v=='true' for k,v in f.attrib.items()) else f.text or '' for f in fs])
  out.append(dict(statement=rs.attrib.get('statement'),columns=columns,rows=rows))
 return out
def differences(a,e):
 out=[]
 if a['rows'] and a['columns']!=e['columns']: out.append(dict(kind='columns',actual=a['columns'],expected=e['columns']))
 if len(a['rows'])!=len(e['rows']): out.append(dict(kind='row_count',actual=len(a['rows']),expected=len(e['rows'])))
 for i,(ar,er) in enumerate(zip(a['rows'],e['rows'])):
  assert len(ar)==len(er)
  for j,(av,ev) in enumerate(zip(ar,er)):
   if av is None or ev is None: ok=av is None and ev is None
   elif e['columns'][j]=='tag_hex': ok=av==ev
   else:
    tolerance=max(Decimal('1e-10'),Decimal('1e-12')*abs(Decimal(str(ev)))) if e['case_id'] in ('WF_REAL_LOW','WF_REAL_HIGH') and j==2 else Decimal(0)
    ok=abs(Decimal(av)-Decimal(str(ev)))<=tolerance
   if not ok: out.append(dict(row=i,column=e['columns'][j],actual=av,expected=ev))
 return out
def main():
 assert (ROOT/'.owned-isolated').is_file()
 assert not (ROOT/'results/summary.json').exists(), 'Do not overwrite completed run'
 plan=json.loads((ROOT/'runtime_plan.json').read_text(encoding='utf-8-sig'))
 summary=dict(started=datetime.datetime.now(datetime.timezone.utc).isoformat(),generation_run_id=plan['run_id'],execution_id=ROOT.name,runner_sha256=sha(ROOT/'runner.py'),image=IMAGE,host=txt(['hostname']),runs=[],blocked=[])
 for job in plan['jobs']:
  if not job.get('ready_for_execution_with_review_policy'):
   summary['blocked'].append(job['target']); continue
  inp=ROOT/'inputs'/job['target']
  for name,info in job['inputs'].items(): assert sha(inp/name)==info['sha256']
  sql=(inp/'test.sql').read_bytes()
  expected=json.loads((inp/'expected.json').read_text(encoding='utf-8-sig'))['cases']
  assert [c['case_id'] for c in expected]==job['result_set_order']
  assert re.findall(rb'-- case_id ([A-Z_]+)',sql)==[x.encode() for x in job['result_set_order']]
  parents=txt(['git','-C',PREV/'repo','show','-s','--format=%P',job['mysql_target_sha']]).split()
  assert parents==[job['parent_sha']]
  for role,key in [('parent','parent_sha'),('target','mysql_target_sha')]:
   rev=job[key]; rt=next(p/'runtime'/rev[:12] for p in (OLD,PREV) if (p/'runtime'/rev[:12]/'manifest.json').exists())
   manifest=json.loads((rt/'manifest.json').read_text()); assert manifest['sha']==rev and manifest['patch_mode'] is None and manifest['diff']=='' and manifest['builder_image']==IMAGE
   hashes={}
   for line in manifest['binary_hashes'].splitlines():
    h,p=line.split(None,1); name=Path(p).name; assert sha(rt/'bin'/name)==h; hashes[name]=h
   assert set(hashes)=={'mysql','mysqld','mysqladmin'}
   deps=rt.parent.parent/'build/library_output_directory'
   dependency_hashes={p.name:sha(p) for p in deps.glob('*.so*') if p.is_file()}
   assert 'libprotobuf-lite.so.3.19.4' in dependency_hashes
   save(ROOT/'results/builds'/f'{rev}.json',dict(manifest=manifest,verified_hashes=hashes,runtime=str(rt),target_parents=parents,shared_library_directory=str(deps),shared_library_hashes=dependency_hashes))
   rid=rev[:12]; name='codex-supplemental-'+rid; cid=None
   launch=['docker','run','-d','--name',name,'--label','experiment='+ROOT.name,'--network','none','--cpus','2','--memory','3g','--user',f'{os.getuid()}:{os.getgid()}','-v',str(ROOT)+':/work','-v',str(rt)+':/runtime:ro','-v',str(deps)+':/deps:ro','-e','LD_LIBRARY_PATH=/deps',IMAGE,'bash','/work/server.sh',rid]
   save(ROOT/'results'/rid/'launch.json',launch)
   try:
    cid=txt(launch)
    client=['docker','exec','-i',cid,'/runtime/bin/mysql','--no-defaults','--protocol=socket','--socket=/work/data/'+rid+'/mysql.sock','-uroot']
    for _ in range(120):
     if cmd(client+['-NBe','SELECT 1'],check=False).returncode==0: break
     if txt(['docker','inspect','--format','{{.State.Running}}',cid])!='true': raise RuntimeError('startup failed')
     time.sleep(2)
    else: raise RuntimeError('startup timeout')
    for trial in range(1,4):
     dest=ROOT/'results'/rid/f'trial_{trial}'; dest.mkdir(parents=True,exist_ok=True)
     schema='isolated_trial_'+str(trial)
     cmd(client+['-e',f'CREATE DATABASE {schema} CHARACTER SET utf8mb4 COLLATE utf8mb4_bin'])
     preamble=b'SELECT VERSION() AS version, @@version_comment AS version_comment, @@SESSION.sql_mode AS sql_mode, @@SESSION.div_precision_increment AS div_precision_increment, @@SESSION.windowing_use_high_precision AS windowing_use_high_precision;\n'
     submitted=preamble+sql; (dest/'submitted.sql').write_bytes(submitted)
     run=dict(target=job['target'],role=role,revision=rev,trial=trial,sql_sha256=sha(inp/'test.sql'),expected_sha256=sha(inp/'expected.json'),submitted_sha256=sha(dest/'submitted.sql'),command=client+['--xml',schema])
     try:
      r=cmd(run['command'],data=submitted,check=False,timeout=120); (dest/'stdout.xml').write_bytes(r.stdout); (dest/'stderr.txt').write_bytes(r.stderr)
      run['returncode']=r.returncode; run['cases']=[]
      datasets=parse(r.stdout.decode()); save(dest/'parsed.json',datasets)
      assert len(datasets)==1+len(expected), f'unexpected resultsets {len(datasets)}'
      assert datasets[0]['columns']==['version','version_comment','sql_mode','div_precision_increment','windowing_use_high_precision']
      run['session']=dict(zip(datasets[0]['columns'],datasets[0]['rows'][0])); assert run['session']['div_precision_increment']=='4'
      for actual,oracle in zip(datasets[1:],expected):
       assert not actual['rows'] or actual['columns']==oracle['columns']
       diff=differences(actual,oracle); hold=oracle['case_id'] in job['oracle_hold_case_ids']
       run['cases'].append(dict(case_id=oracle['case_id'],status='oracle_hold' if hold else ('mismatch' if diff else 'pass'),differences=diff))
      run['status']='sql_error' if r.returncode else 'completed'
     except subprocess.TimeoutExpired as ex:
      (dest/'stdout.xml').write_bytes(ex.stdout or b''); (dest/'stderr.txt').write_bytes(ex.stderr or b''); run['status']='timeout'
     except Exception as ex: run['status']='adapter_error'; run['error']=str(ex)
     run['container_state']=json.loads(txt(['docker','inspect','--format','{{json .State}}',cid]))
     save(dest/'comparison.json',run); summary['runs'].append(run); save(ROOT/'results/summary.json',summary)
     print(json.dumps(dict(revision=rid,trial=trial,status=run['status'],cases=[(c['case_id'],c['status'],len(c['differences'])) for c in run.get('cases',[])])),flush=True)
   finally:
    if cid:
     cmd(['docker','stop','-t','10',cid],check=False); log=cmd(['docker','logs',cid],check=False); (ROOT/'results'/rid/'container.log').write_bytes(log.stdout+log.stderr)
     cmd(['docker','rm',cid]); save(ROOT/'results'/rid/'cleanup.json',dict(container_id=cid,removed=True))
 summary['finished']=datetime.datetime.now(datetime.timezone.utc).isoformat(); save(ROOT/'results/summary.json',summary)
if __name__=='__main__': main()
