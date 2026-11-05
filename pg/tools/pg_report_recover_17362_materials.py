"""Bounded recovery of original-version RPMs and CentOS7 runtime resources."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import subprocess

ROOT=Path('/mnt/sdb/dufei/pg_report_replay_20261104_run001/remaining69_review_20261104')


def download(url):
    name=url.rsplit('/',1)[-1];dest=ROOT/name
    record={'url':url,'file':name,'status':'not_downloaded'}
    if not dest.exists():
        temporary=ROOT/(name+'.partial')
        p=subprocess.run(['curl','-f','-L','--connect-timeout','8','--max-time','35',url,'-o',str(temporary)],capture_output=True,text=True,timeout=40)
        if p.returncode:
            return dict(record,status='download_failed',returncode=p.returncode,stderr=p.stderr[-600:])
        temporary.rename(dest)
    data=dest.read_bytes()
    if data[:4]!=bytes.fromhex('edabeedb'):
        return dict(record,status='invalid_rpm_magic',bytes=len(data))
    return dict(record,status='downloaded_not_installed',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
                qualification='RPM name, signature and dependencies must still be verified in the target environment')


def image():
    try:
        p=subprocess.run(['docker','pull','centos:7'],capture_output=True,text=True,timeout=50)
        result=dict(returncode=p.returncode,stdout=p.stdout[-1800:],stderr=p.stderr[-1800:])
    except subprocess.TimeoutExpired as exc:
        result=dict(status='timeout',stdout=(exc.stdout or b'').decode(errors='replace')[-1800:],stderr=(exc.stderr or b'').decode(errors='replace')[-1800:])
    p=subprocess.run(['docker','image','inspect','centos:7','--format','{{json .RepoDigests}}'],capture_output=True,text=True,timeout=10)
    result['image_present']=p.returncode==0;result['repo_digests']=p.stdout.strip()
    return result


def main():
    base='https://download.postgresql.org/pub/repos/yum/14/redhat/rhel-7-x86_64/'
    urls=[base+f'{p}-{v}-1PGDG.rhel7.x86_64.rpm' for v in ['14.0','14.1','14.2']
          for p in ['postgresql14','postgresql14-libs','postgresql14-server']]
    urls+=['https://archive.kernel.org/centos-vault/7.9.2009/os/x86_64/Packages/libicu-50.2-4.el7_7.x86_64.rpm']
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        image_job=pool.submit(image)
        downloads=list(pool.map(download,urls))
        result=dict(downloads=downloads,centos7=image_job.result(),database_execution_performed=False)
    (ROOT/'bounded_acquisition.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result),flush=True)


if __name__=='__main__':main()
