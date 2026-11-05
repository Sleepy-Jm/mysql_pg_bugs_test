"""Upload immutable batch files and queue behind the preceding completed matrix."""
import argparse
import base64
import json
from pathlib import Path
from mysql_server_batch_transport import call

ROOT=Path('experiments/pg_report_replay_20261104/run_001')
REMOTE='/mnt/sdb/dufei/pg_report_replay_20261104_run001'


def main():
    p=argparse.ArgumentParser();p.add_argument('--batch',required=True);p.add_argument('--runner',required=True);p.add_argument('--after');p.add_argument('--after-count',type=int);p.add_argument('--material',action='append',default=[]);a=p.parse_args()
    spec='prepared_specs_'+a.batch+'.json'
    files={Path(a.runner).name:Path(a.runner).read_bytes(),spec:(ROOT/spec).read_bytes()}
    files.update({'materials/'+n:(ROOT/'materials'/n).read_bytes() for n in a.material})
    for name,data in files.items():
        encoded=base64.b64encode(data).decode()
        code=f"from pathlib import Path\nimport base64\nr=Path({REMOTE!r});p=r/{name!r};p.parent.mkdir(parents=True,exist_ok=True);data=base64.b64decode({encoded!r})\nassert not p.exists() or p.read_bytes()==data\np.write_bytes(data) if not p.exists() else None\n"
        call(code)
    queue="import json,time,subprocess\nfrom pathlib import Path\n"+f"r=Path({REMOTE!r})\n"
    if a.after:
        queue+=f"p=r/{(a.after+'_results.json')!r}\nwhile not p.exists() or len(json.loads(p.read_text()))<{a.after_count}:time.sleep(5)\n"
    queue+="while (r/'sock/.s.PGSQL.55483.lock').exists():time.sleep(2)\n"
    queue+=f"subprocess.run(['python3','-u',str(r/{Path(a.runner).name!r}),'--batch',{a.batch!r},'--specs',{spec!r}],check=True)\n"
    code="import subprocess,json\nfrom pathlib import Path\n"+f"r=Path({REMOTE!r});q=r/{('queue_'+a.batch+'.py')!r};assert not q.exists();q.write_text({queue!r});f=(r/{(a.batch+'.log')!r}).open('wb');p=subprocess.Popen(['python3','-u',str(q)],stdout=f,stderr=subprocess.STDOUT,start_new_session=True);print(json.dumps({{'pid':p.pid,'batch':{a.batch!r}}}))\n"
    raw=call(code);(ROOT/(a.batch+'_launch.json')).write_bytes(raw);print(raw.decode())


if __name__=='__main__':main()
