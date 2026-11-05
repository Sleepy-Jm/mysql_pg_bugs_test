"""Build the frozen PostgreSQL version matrix inside its own server directory."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tarfile

ROOT = Path('/mnt/sdb/dufei/pg_report_replay_20261104_run001')
REPO = Path('/mnt/sdb/dufei/postgresql-upstream')
VERSIONS = ['14.1', '14.2', '17.1', '17.2', '14.0', '14.3', '17.0', '17.3']

def main():
    ROOT.mkdir(exist_ok=True)
    records = []
    for version in VERSIONS:
        dest = ROOT / 'builds' / version
        dest.mkdir(parents=True, exist_ok=False)
        source, build, prefix = (dest / n for n in ('source', 'work', 'install'))
        source.mkdir(); build.mkdir()
        tag = 'REL_' + version.replace('.', '_')
        commit = subprocess.check_output(['git', '-C', str(REPO), 'rev-parse', tag + '^{commit}'], text=True).strip()
        record = {'version': version, 'tag': tag, 'commit': commit, 'started_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'commands': []}
        records.append(record)
        try:
            archive = dest / 'source.tar'
            with archive.open('wb') as f:
                subprocess.run(['git', '-C', str(REPO), 'archive', '--format=tar', commit], stdout=f, check=True)
            record['source_archive_sha256'] = hashlib.sha256(archive.read_bytes()).hexdigest()
            with tarfile.open(archive) as tar:
                for member in tar.getmembers():
                    target = (source / member.name).resolve()
                    assert source.resolve() in target.parents
                    assert not member.issym() and not member.islnk()
                tar.extractall(source)
            commands = [[str(source/'configure'), '--prefix='+str(prefix), '--enable-debug', '--enable-cassert',
                         '--with-icu', '--with-openssl', '--with-python', 'CFLAGS=-O1 -g'],
                        ['make', '-j4', 'world-bin'], ['make', 'install-world-bin']]
            for n, cmd in enumerate(commands):
                with (dest/f'step_{n}.log').open('wb') as log:
                    p = subprocess.run(['nice', '-n', '10'] + cmd, cwd=build, stdout=log, stderr=subprocess.STDOUT, timeout=2400)
                record['commands'].append({'args':cmd, 'returncode':p.returncode, 'log':str(dest/f'step_{n}.log')})
                if p.returncode:
                    raise RuntimeError(f'build step {n} failed')
            actual = subprocess.check_output([str(prefix/'bin/postgres'), '--version'], text=True).strip()
            assert actual == 'postgres (PostgreSQL) ' + version, actual
            record.update(status='built', actual_version=actual,
                          configure=subprocess.check_output([str(prefix/'bin/pg_config'), '--configure'],text=True).strip(),
                          postgres_sha256=hashlib.sha256((prefix/'bin/postgres').read_bytes()).hexdigest())
        except Exception as exc:
            record.update(status='build_failed', error=str(exc))
        record['finished_at'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        (dest/'manifest.json').write_text(json.dumps(record,indent=2))
        (ROOT/'build_manifest.json').write_text(json.dumps(records,indent=2))
        print(version, record['status'], flush=True)

if __name__ == '__main__':
    main()
