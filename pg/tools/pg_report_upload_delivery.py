"""Upload a versioned report/evidence snapshot and verify every file remotely."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import tarfile
from mysql_server_batch_transport import SSH,call

ROOT=Path('experiments/pg_report_replay_20261104/run_001')
CENSUS=Path('experiments/pg_version_report_census_20261104/run_001')
REMOTE='/mnt/sdb/dufei/pg_report_replay_20261104_run001'


def main():
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    local=Path('experiments/pg_report_deliveries_20261104')/stamp;local.mkdir(parents=True,exist_ok=False)
    files={p.as_posix():p for p in ROOT.rglob('*') if p.is_file()}
    for p in CENSUS.glob('*'):
        if p.is_file():files[p.as_posix()]=p
    reports=json.loads((ROOT/'frozen_reports.json').read_text(encoding='utf-8'))
    for r in reports:
        p=Path(r['snapshot']);files[p.as_posix()]=p
    for p in Path('tools').glob('pg_report_*.py'):files[p.as_posix()]=p
    for n in ['tools/pg_version_report_census.py','tools/mysql_server_batch_transport.py','tests/test_pg_version_report_census.py','tests/test_pg_report_version_comparison.py','AGENTS.md','docs/mysql_report_preparation.md']:
        p=Path(n)
        if p.exists():files[p.as_posix()]=p
    manifest=dict(snapshot_utc=stamp,server='dufei@47.108.211.69',remote_directory=REMOTE+'/deliveries/'+stamp,
                  report=(ROOT/('VERSION_COMPARISON.md' if (ROOT/'VERSION_COMPARISON.md').exists() else 'SQL_ORACLE_PROGRESS.md')).as_posix(),
                  files={name:dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for name,p in sorted(files.items())})
    m=local/'DELIVERY_MANIFEST.json';m.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    readme=local/'README.md';readme.write_text('# PG 报告与证据快照\n\n主报告：['+manifest['report']+']('+manifest['report']+')\n\n本目录是进行中的版本化快照，原始服务器回放证据仍位于 '+REMOTE+'/attempts/。\n\nDELIVERY_MANIFEST.json 逐文件保存 SHA-256；VERIFY_RESULT.json 是服务器校验结果。\n',encoding='utf-8')
    archive=local/'bundle.tar.gz'
    with tarfile.open(archive,'w:gz') as t:
        for name,p in sorted(files.items()):t.add(p,arcname=name,recursive=False)
        t.add(m,arcname='DELIVERY_MANIFEST.json');t.add(readme,arcname='README.md')
    remote=manifest['remote_directory']
    call(f"from pathlib import Path\np=Path({remote!r});p.mkdir(parents=True,exist_ok=False)\n")
    # scp uses the same host-key and forwarding restrictions as the established transport.
    args=['scp']+SSH[1:-1]+[str(archive),SSH[-1]+':'+remote+'/bundle.tar.gz']
    subprocess.run(args,check=True,timeout=180)
    sha=hashlib.sha256(archive.read_bytes()).hexdigest()
    code="import hashlib,json,tarfile\nfrom pathlib import Path\n"+f"r=Path({remote!r});a=r/'bundle.tar.gz';assert hashlib.sha256(a.read_bytes()).hexdigest()=={sha!r}\n"
    code+="with tarfile.open(a) as t:\n for member in t.getmembers():\n  p=r/member.name\n  assert member.isfile() and r.resolve() in p.resolve().parents\n  p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(t.extractfile(member).read())\nm=json.loads((r/'DELIVERY_MANIFEST.json').read_text());bad=[n for n,v in m['files'].items() if hashlib.sha256((r/n).read_bytes()).hexdigest()!=v['sha256']]\nresult={'remote_directory':str(r),'verified_files':len(m['files']),'mismatches':bad,'archive_sha256':hashlib.sha256(a.read_bytes()).hexdigest()}\n(r/'VERIFY_RESULT.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))\nassert not bad\n"
    raw=call(code,timeout=180);(local/'VERIFY_RESULT.json').write_bytes(raw);print(raw.decode())
    (ROOT/'latest_delivery.json').write_text(json.dumps(dict(remote_directory=remote,report_path=remote+'/'+manifest['report'],local_verification=str(local/'VERIFY_RESULT.json')),indent=2),encoding='utf-8')


if __name__=='__main__':main()
