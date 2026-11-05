"""Server-side task-local dependencies and source-tagged diagnostic builds."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tarfile

ROOT = Path('/mnt/sdb/dufei/pg_report_replay_20261104_run001')
REPO = Path('/mnt/sdb/dufei/postgresql-upstream')


def main():
    deps = ROOT/'continuation_deps'
    deps.mkdir(exist_ok=True)
    unpack = deps/'unpacked'
    assert (deps/'manifest.json').exists()
    llvm = unpack/'usr/lib/llvm-10'
    env = dict(os.environ)
    env['PATH'] = str(llvm/'bin')+':'+env['PATH']
    env['LD_LIBRARY_PATH'] = str(unpack/'usr/lib/x86_64-linux-gnu')+':'+env.get('LD_LIBRARY_PATH', '')
    jobs = [(v, 'valgrind_instrumented') for v in ['14.1', '14.2', '14.3']]
    for version, variant in jobs:
        dest = ROOT/'special_builds'/(version+'_'+variant)
        dest.mkdir(exist_ok=False)
        source = dest/'source'; source.mkdir()
        work = dest/'work'; work.mkdir()
        prefix = dest/'install'
        rec = dict(version=version, variant=variant, commands=[],
                   started_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
        try:
            tag = 'REL_'+version.replace('.', '_')
            commit = subprocess.check_output(['git', '-C', str(REPO), 'rev-parse', tag+'^{commit}'], text=True).strip()
            rec.update(tag=tag, commit=commit)
            archive = dest/'source.tar'
            with archive.open('wb') as f:
                subprocess.run(['git', '-C', str(REPO), 'archive', commit], stdout=f, check=True)
            rec['source_sha256'] = hashlib.sha256(archive.read_bytes()).hexdigest()
            with tarfile.open(archive) as t:
                assert all(not m.issym() and not m.islnk() and source.resolve() in (source/m.name).resolve().parents for m in t.getmembers())
                t.extractall(source)
            config = [str(source/'configure'), '--prefix='+str(prefix), '--enable-debug',
                      '--with-icu', '--with-openssl', 'CFLAGS=-O1 -g']
            if variant == 'jit_nocassert':
                config += ['--with-llvm', 'LLVM_CONFIG='+str(llvm/'bin/llvm-config'),
                           'CLANG='+str(llvm/'bin/clang')]
            else:
                config += ['--enable-cassert',
                           'CPPFLAGS=-DUSE_VALGRIND -I'+str(unpack/'usr/include')]
            for n, cmd in enumerate([config, ['make', '-j4', 'world-bin'], ['make', 'install-world-bin']]):
                with (dest/f'step_{n}.log').open('wb') as f:
                    p = subprocess.run(['nice', '-n', '15']+cmd, cwd=work, env=env,
                                       stdout=f, stderr=subprocess.STDOUT, timeout=2400)
                rec['commands'].append(dict(args=cmd, returncode=p.returncode))
                if p.returncode:
                    raise RuntimeError('build step failed '+str(n))
            probe=subprocess.check_output(['gcc','-dM','-E','-D_GNU_SOURCE','-DUSE_VALGRIND','-I'+str(unpack/'usr/include'),'-I'+str(work/'src/include'),'-I'+str(source/'src/include'),'-include','postgres.h','-'],input=b'',env=env).decode()
            assert '#define USE_VALGRIND 1' in probe
            (dest/'preprocessor_macros.txt').write_text(probe)
            rec['use_valgrind_verified']=True
            binary = prefix/'bin/postgres'
            rec.update(status='built', actual_version=subprocess.check_output([str(binary), '--version'], text=True, env=env).strip(),
                       binary_sha256=hashlib.sha256(binary.read_bytes()).hexdigest(),
                       configure=subprocess.check_output([str(prefix/'bin/pg_config'), '--configure'], text=True, env=env).strip())
        except Exception as exc:
            rec.update(status='build_failed', error=str(exc))
        rec['finished_at'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        (dest/'manifest.json').write_text(json.dumps(rec, indent=2))
        print(version, variant, rec['status'], flush=True)


if __name__ == '__main__':
    main()
