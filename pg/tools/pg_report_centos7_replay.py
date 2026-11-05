"""Source-RPM replay for report17362 on isolated CentOS7 containers."""
import datetime
import json
from pathlib import Path
import re
import subprocess
import time

ROOT=Path('/mnt/sdb/dufei/pg_report_replay_20261104_run001')
MATERIAL=ROOT/'remaining69_review_20261104'
IMAGE='sha256:eeb6ee3f44bd0b5103bb561b4c16bcb82328cfe5809ab675bb17ab3a16c517c9'


def main():
    spec=json.loads((ROOT/'prepared_specs_batch014.json').read_text())[0]
    results=[]
    for version in ['14.0','14.1','14.2']:
        dest=ROOT/'attempts/batch014'/spec['scenario_id']/version;dest.mkdir(parents=True,exist_ok=False)
        name='pg_report_17362_'+version.replace('.','_')+'_20261104'
        rec=dict(report_id='17362',scenario_id=spec['scenario_id'],version=version,target_version='14.1',
                 spec_sha256=spec['spec_sha256'],oracle=spec['oracle'],commands=[],stage='container_create',
                 status='execution_failed',started_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                 build_manifest={'image_id':IMAGE,'packages':[]},config={'listen_addresses':'','socket':'/evidence','port':55483})
        def call(args,label,timeout=90):
            start=time.monotonic()
            try:
                p=subprocess.run(list(map(str,args)),capture_output=True,text=True,timeout=timeout)
                x=dict(returncode=p.returncode,stdout=p.stdout,stderr=p.stderr,timed_out=False)
            except subprocess.TimeoutExpired as exc:
                x=dict(returncode=None,stdout=(exc.stdout or b'').decode(errors='replace'),stderr=(exc.stderr or b'').decode(errors='replace'),timed_out=True)
            x['elapsed_seconds']=time.monotonic()-start
            (dest/(label+'.stdout')).write_text(x['stdout']);(dest/(label+'.stderr')).write_text(x['stderr'])
            rec['commands'].append(dict(label=label,args=list(map(str,args)),**x));return x
        def run(args,label,timeout=90):
            return call(['docker','exec',name]+args,label,timeout)
        def pg(args,label,timeout=90):
            return call(['docker','exec','-u','postgres','-e','PGHOST=/evidence','-e','PGPORT=55483',name]+args,label,timeout)
        created=False;started=False
        try:
            p=call(['docker','create','--name',name,'--network','none','-v',str(MATERIAL)+':/inputs:ro','-v',str(dest)+':/evidence',IMAGE,'sleep','3600'],'create')
            if p['returncode']:raise RuntimeError('container creation failed')
            created=True
            if call(['docker','start',name],'container_start')['returncode']:raise RuntimeError('container start failed')
            rec['stage']='package_install'
            packages=[f'/inputs/{p}-{version}-1PGDG.rhel7.x86_64.rpm' for p in ['postgresql14','postgresql14-libs','postgresql14-server']]
            packages+=['/inputs/libicu-50.2-4.el7_7.x86_64.rpm','/inputs/systemd-sysv-219-78.el7.x86_64.rpm']
            p=run(['rpm','-Uvh']+packages,'rpm_install',120)
            if p['returncode']:raise RuntimeError('source package installation failed')
            p=run(['rpm','-q','postgresql14','postgresql14-libs','postgresql14-server','libicu','systemd-sysv'],'package_identity')
            rec['build_manifest']['packages']=p['stdout'].splitlines()
            p=run(['/usr/pgsql-14/bin/postgres','--version'],'binary_identity')
            rec['actual_version']=p['stdout'].strip()
            assert rec['actual_version']=='postgres (PostgreSQL) '+version
            assert 'libicu-50.2-4.el7_7.x86_64' in rec['build_manifest']['packages']
            if run(['chown','postgres:postgres','/evidence'],'evidence_owner')['returncode']:raise RuntimeError('evidence ownership failed')
            rec['stage']='initdb'
            if pg(['/usr/pgsql-14/bin/initdb','-D','/evidence/data','-A','trust','--no-locale','-E','UTF8','--no-sync'],'initdb')['returncode']:raise RuntimeError('initdb failed')
            rec['stage']='startup'
            p=pg(['/usr/pgsql-14/bin/pg_ctl','-D','/evidence/data','-l','/evidence/server.log','-o',"-h '' -k /evidence -p 55483",'-w','start'],'pg_start')
            if p['returncode']:raise RuntimeError('server startup failed')
            started=True
            pg(['/usr/pgsql-14/bin/psql','-XAt','-c',"SELECT version(); SELECT collname,collversion FROM pg_collation WHERE collname='fi-FI-x-icu';"],'runtime_identity')
            rec['stage']='setup'
            p=pg(['/usr/pgsql-14/bin/psql','-X','-v','ON_ERROR_STOP=1','-f','/inputs/17362_setup.sql'],'setup')
            if p['returncode']:raise RuntimeError('original schema or data failed')
            rec['stage']='replay'
            p=pg(['/usr/pgsql-14/bin/psql','-XAt','-v','ON_ERROR_STOP=1','-f','/inputs/17362_trigger.sql'],'replay')
            matched=bool(re.search(spec['oracle']['pattern'],p['stderr']))
            rec.update(trigger_reached=True,script_completed=p['returncode']==0,oracle_matched=matched,
                       trigger_output=p['stdout'],trigger_stderr=p['stderr'])
            if matched:rec.update(status='reproduced',reason='original query error matches frozen source oracle')
            elif p['returncode']==0:rec.update(status='not_reproduced',reason='original query completed without report error; cause not determined')
            else:rec.update(status='inconclusive',reason='different query error or timeout')
        except Exception as exc:
            rec.update(reason=str(exc))
        finally:
            if started:
                p=pg(['/usr/pgsql-14/bin/pg_ctl','-D','/evidence/data','-m','immediate','-w','stop'],'pg_stop')
                rec['cleanup_confirmed']=p['returncode']==0
            if created:
                p=call(['docker','stop','-t','5',name],'container_stop',30)
                rec['container_stopped']=p['returncode']==0
            rec['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
            (dest/'result.json').write_text(json.dumps(rec,indent=2));results.append(rec)
            (ROOT/'batch014_results.json').write_text(json.dumps(results,indent=2))
        print(version,rec['status'],rec.get('reason'),flush=True)


if __name__=='__main__':main()
