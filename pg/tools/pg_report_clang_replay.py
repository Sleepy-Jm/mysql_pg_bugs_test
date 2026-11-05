"""Replay report17424 source compiler flags; expected compile errors are observations."""
import datetime
import json
import os
from pathlib import Path
import re
import subprocess

ROOT=Path('/mnt/sdb/dufei/pg_report_replay_20261104_run001')


def main():
    spec=json.loads((ROOT/'prepared_specs_batch011.json').read_text())[0]
    compiler=ROOT/'continuation_deps/unpacked/usr/lib/llvm-10/bin'
    env=dict(os.environ,PATH=str(compiler)+':'+os.environ['PATH'],
             LD_LIBRARY_PATH=str(ROOT/'continuation_deps/unpacked/usr/lib/x86_64-linux-gnu'))
    results=[]
    for version in ['14.1','14.2','14.3']:
        dest=ROOT/'attempts/batch011'/spec['scenario_id']/version;dest.mkdir(parents=True,exist_ok=False)
        (dest/'oracle.json').write_text(json.dumps(spec['oracle'],indent=2))
        build=json.loads((ROOT/'builds'/version/'manifest.json').read_text())
        rec=dict(report_id=spec['report_id'],scenario_id=spec['scenario_id'],version=version,
                 target_version=spec['target_version'],spec_sha256=spec['spec_sha256'],
                 started_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),commands=[],
                 status='execution_failed',stage='configure',build_manifest=build,
                 actual_version='PostgreSQL source tag '+build['tag'],
                 compiler_version=subprocess.check_output([str(compiler/'clang'),'--version'],text=True,env=env),
                 oracle=spec['oracle'],config={'CC':'clang','CXX':'clang++',
                     'CFLAGS':'-O2 -fgnuc-version=0','CXXFLAGS':'-O2 -fno-builtin -fgnuc-version=0'})
        try:
            config=[str(ROOT/'builds'/version/'source/configure'),'--prefix='+str(dest/'install'),
                    'CC=clang','CXX=clang++','CFLAGS=-O2 -fgnuc-version=0',
                    'CXXFLAGS=-O2 -fno-builtin -fgnuc-version=0']
            for label,args in [('configure',config),('compile',['make','-j2','world-bin'])]:
                rec['stage']=label
                with (dest/(label+'.log')).open('wb') as f:
                    p=subprocess.run(['nice','-n','15']+args,cwd=dest,env=env,stdout=f,stderr=subprocess.STDOUT,timeout=600)
                text=(dest/(label+'.log')).read_text(errors='replace')
                rec['commands'].append(dict(label=label,args=args,returncode=p.returncode,log=str(dest/(label+'.log'))))
                if p.returncode:
                    matched=bool(re.search(spec['oracle']['pattern'],text,re.M))
                    rec.update(status='reproduced' if matched else 'inconclusive',
                               reason='source slock_t compiler error observed' if matched else 'other build error prevented reported compiler observation',
                               trigger_output=text[-12000:],oracle_matched=matched)
                    break
            else:
                rec.update(status='not_reproduced',reason='complete build under recorded clang10 did not produce report error; original RHEL/clang environment not confirmed',trigger_output='build completed')
        except Exception as exc:
            rec.update(status='execution_failed',reason=str(exc))
        rec['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
        (dest/'result.json').write_text(json.dumps(rec,indent=2));results.append(rec)
        (ROOT/'batch011_results.json').write_text(json.dumps(results,indent=2))
        print(version,rec['status'],flush=True)


if __name__=='__main__':main()
