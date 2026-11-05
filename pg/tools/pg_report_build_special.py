"""Build report-required variants without modifying ordinary version builds."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import tarfile

ROOT=Path('/mnt/sdb/dufei/pg_report_replay_20261104_run001')
REPO=Path('/mnt/sdb/dufei/postgresql-upstream')


def main():
    jobs=[(v,'ubsan_client') for v in ['14.1','14.0','14.2']]+[(v,'serial') for v in ['14.1','14.0','14.2']]+[(v,'ordinary') for v in ['13.6','12.9']]
    for version,variant in jobs:
        dest=ROOT/'special_builds'/(version+'_'+variant);dest.mkdir(parents=True,exist_ok=False)
        source=dest/'source';source.mkdir();work=dest/'work';work.mkdir();prefix=dest/'install'
        rec=dict(version=version,variant=variant,commands=[],started_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
        try:
            commit=subprocess.check_output(['git','-C',str(REPO),'rev-parse','REL_'+version.replace('.','_')+'^{commit}'],text=True).strip();rec['commit']=commit
            archive=dest/'source.tar'
            with archive.open('wb') as f:subprocess.run(['git','-C',str(REPO),'archive',commit],stdout=f,check=True)
            rec['source_sha256']=hashlib.sha256(archive.read_bytes()).hexdigest()
            with tarfile.open(archive) as t:
                assert all(not m.issym() and not m.islnk() and source.resolve() in (source/m.name).resolve().parents for m in t.getmembers());t.extractall(source)
            config=[str(source/'configure'),'--prefix='+str(prefix),'--enable-debug','--enable-cassert','--with-icu','--with-openssl']
            if variant=='ubsan_client':
                flags='-fsanitize=undefined -g -O2'
                config += ['CFLAGS='+flags,'CXXFLAGS='+flags,'LDFLAGS='+flags]
                commands=[config,['make','-j2','-C','src/bin/psql','all']]
            else:
                config+=['CFLAGS=-O1 -g']
                if variant=='serial':config+=['CPPFLAGS=-O0 -DTEST_SUMMARIZE_SERIAL']
                commands=[config,['make','-j2','world-bin'],['make','install-world-bin'],['make','-j2','-C','src/test/isolation','all']]
            for n,cmd in enumerate(commands):
                with (dest/f'step_{n}.log').open('wb') as f:p=subprocess.run(['nice','-n','15']+cmd,cwd=work,stdout=f,stderr=subprocess.STDOUT,timeout=3600)
                rec['commands'].append(dict(args=cmd,returncode=p.returncode))
                if p.returncode:raise RuntimeError('build step failed '+str(n))
            binary=work/'src/bin/psql/psql' if variant=='ubsan_client' else prefix/'bin/postgres'
            rec.update(status='built',binary=str(binary),binary_sha256=hashlib.sha256(binary.read_bytes()).hexdigest(),actual_version=subprocess.check_output([str(binary),'--version'],text=True).strip())
        except Exception as e:rec.update(status='build_failed',error=str(e))
        rec['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
        (dest/'manifest.json').write_text(json.dumps(rec,indent=2));print(version,variant,rec['status'],flush=True)


if __name__=='__main__':main()
