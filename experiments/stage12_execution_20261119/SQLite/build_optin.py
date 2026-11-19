"""Build the explicitly enabled count-of-view configuration at the original boundary."""
from pathlib import Path
import hashlib,json,subprocess
r=Path(__file__).resolve().parent
row=next(x for x in json.loads((r/'plan.json').read_text()) if x['case']=='d1ba200234f40b84')
for name in ['optin-intro-parent','optin-intro']:
    v=row['versions'][name];sha=v['git']
    src=r/'builds'/sha[:12]
    old=json.loads((src/'built.json').read_text())
    target=r/'builds'/(sha[:12]+'-optin');target.mkdir(exist_ok=True)
    amalg=src/'obj'/'sqlite3.c';assert hashlib.sha256(amalg.read_bytes()).hexdigest()==old['amalgamation_sha256']
    cmd=['gcc','-fPIC','-O0','-g0','-shared','-DSQLITE_THREADSAFE=1','-DSQLITE_COUNTOFVIEW_OPTIMIZATION',str(amalg),'-o',str(target/'libquery.so'),'-ldl','-lpthread','-lm']
    if not (target/'built.json').exists():
        subprocess.run(cmd,check=True)
        old.update({'lib_sha256':hashlib.sha256((target/'libquery.so').read_bytes()).hexdigest(),'cflags':'-fPIC -O0 -g0 -shared -DSQLITE_THREADSAFE=1 -DSQLITE_COUNTOFVIEW_OPTIMIZATION'})
        (target/'built.json').write_text(json.dumps(old,indent=2)+'\n')
    subprocess.run(['python3',str(r/'execute.py'),row['case'],name],check=True)
