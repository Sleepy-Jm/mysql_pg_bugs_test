"""Report 17466: source configure behavior, separately counted from SQL replay."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT=Path('/mnt/sdb/dufei/pg_report_replay_20261104_run001')


def main():
    oracle=dict(kind='build_configuration',pattern=r'(?m)^CFLAGS\s*=.*-DUSE_TOOLS',absent=r'(?:^|\s)-O\S*',reported_phenomenon='explicit CFLAGS=-DUSE_TOOLS does not add default optimization flag',author_expected_behavior='append -O2 if caller did not supply optimization')
    results=[]
    for version in ['14.1','14.2','14.3']:
        dest=ROOT/'configure_replay_17466'/version;dest.mkdir(parents=True,exist_ok=False)
        (dest/'oracle.json').write_text(json.dumps(oracle,indent=2))
        args=[str(ROOT/'builds'/version/'source/configure'),'CFLAGS=-DUSE_TOOLS']
        p=subprocess.run(args,cwd=dest,capture_output=True,timeout=180)
        (dest/'configure.stdout').write_bytes(p.stdout);(dest/'configure.stderr').write_bytes(p.stderr)
        rec=dict(report_id='17466',target_version='14.2',version=version,args=args,returncode=p.returncode,oracle=oracle,execution_kind='configure_not_sql')
        if p.returncode:rec.update(status='execution_failed',reason='configure failed')
        else:
            makefile=(dest/'src/Makefile.global').read_text();flags=re.search(r'(?m)^CFLAGS\s*=([^\n]+)',makefile)
            rec['CFLAGS']=flags[1].strip() if flags else None
            rec['makefile_sha256']=hashlib.sha256(makefile.encode()).hexdigest()
            if not flags:rec.update(status='inconclusive',reason='CFLAGS absent from generated Makefile')
            else:rec.update(status='reproduced' if '-DUSE_TOOLS' in flags[1] and not re.search(oracle['absent'],flags[1]) else 'not_reproduced')
        (dest/'result.json').write_text(json.dumps(rec,indent=2));results.append(rec)
    (ROOT/'configure_results.json').write_text(json.dumps(results,indent=2))


if __name__=='__main__':main()
