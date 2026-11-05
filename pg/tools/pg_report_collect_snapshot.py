"""Collect server records and continuation artifact hashes without altering attempts."""
import json
from pathlib import Path
from mysql_server_batch_transport import call

ROOT=Path('experiments/pg_report_replay_20261104/run_001')
CODE=r'''
import datetime,hashlib,json,subprocess,io,tarfile
from pathlib import Path
r=Path('/mnt/sdb/dufei/pg_report_replay_20261104_run001')
processes=subprocess.run(['ps','-eo','pid,etime,args'],capture_output=True,text=True).stdout.splitlines()
processes=[x for x in processes if str(r) in x and ('python3' in x or 'postgres -D' in x or 'pgbench -' in x)]
builds={p.parent.name:json.loads(p.read_text()) for p in (r/'special_builds').glob('*/manifest.json')}
artifacts={}
for b in ['batch008','batch009','batch010','batch011','batch012','batch013','batch014','batch015']:
 for dest in (r/'attempts'/b).glob('*/*'):
  for p in dest.iterdir():
   if p.is_file():artifacts[str(p.relative_to(r))]={'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
  for p in dest.glob('cluster/*.log'):
   try: raw=p.read_bytes()
   except PermissionError:
    assert b=='batch015' and p.name=='server.log'
    name='pg_report_17362_fix_'+dest.name.replace('.','_')+'_20261104'
    copied=subprocess.run(['docker','cp',name+':/evidence/cluster/server.log','-'],capture_output=True,check=True)
    with tarfile.open(fileobj=io.BytesIO(copied.stdout)) as archive:
     raw=archive.extractfile('server.log').read()
   artifacts[str(p.relative_to(r))]={'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
logs={p.name:p.read_text(errors='replace')[-1800:] for p in r.glob('batch*.log')}
logs.update({p.name:p.read_text(errors='replace')[-1800:] for p in r.glob('continuation*builds.log')})
print(json.dumps(dict(snapshot_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 batches={p.name:json.loads(p.read_text()) for p in r.glob('batch*_results.json')},
 configure=json.loads((r/'configure_results.json').read_text()),builds=builds,logs=logs,
 dependency_manifest=json.loads((r/'continuation_deps/manifest.json').read_text()),
 processes=processes,continuation_artifacts=artifacts)))
'''


def main():
    data=json.loads(call(CODE,timeout=180))
    continuation=ROOT/'continuation_20261104'
    for name,value in [('execution_snapshot.json',data['batches']),('configure_results.json',data['configure'])]:
        (ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
    metadata={k:v for k,v in data.items() if k not in ['batches','configure']}
    (continuation/'server_evidence_snapshot.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(snapshot_utc=data['snapshot_utc'],batch_counts={k:len(v) for k,v in data['batches'].items()},
                         active_processes=data['processes'],logs={k:v for k,v in data['logs'].items() if k>='batch008'}),ensure_ascii=False,indent=2))


if __name__=='__main__':main()
