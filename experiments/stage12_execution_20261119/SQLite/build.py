from pathlib import Path
import concurrent.futures
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
import time

root=Path(__file__).resolve().parent
def call(args,cwd,log,timeout):
    with log.open("ab") as f:
        f.write(("\n$ "+" ".join(map(str,args))+"\n").encode()); f.flush()
        p=subprocess.run(args,cwd=cwd,stdout=f,stderr=subprocess.STDOUT,timeout=timeout)
    if p.returncode:raise RuntimeError("command failed: "+str(args[0])+" rc "+str(p.returncode))
def out(args,cwd):
    return subprocess.check_output(args,cwd=cwd,text=True).strip()
def build(item):
    sha,fossil=item
    b=root/'builds'/sha[:12];b.mkdir(parents=True,exist_ok=True)
    log=b/'build.log';receipt=b/'built.json'
    if receipt.exists() and (b/'libquery.so').exists():return
    record={'revision':sha,'expected_fossil_prefix':fossil}
    try:
        tarpath=b/'official.tar.gz'; source=b/'source'
        if not source.exists():
            url='https://codeload.github.com/sqlite/sqlite/tar.gz/'+sha
            if not tarpath.is_file():
                partial=tarpath.with_suffix('.part')
                call(['curl','-fLsS','--connect-timeout','10','--max-time','150','--retry','3','--retry-delay','1','-o',str(partial),url],b,log,600)
                os.replace(partial,tarpath)
            call(['tar','-xzf',str(tarpath)],b,log,120)
            (b/('sqlite-'+sha)).rename(source)
        mf=(source/'manifest.uuid').read_text().strip()
        if fossil and not mf.startswith(fossil):raise ValueError(('manifest',mf,fossil))
        obj=b/'obj';obj.mkdir(exist_ok=True)
        env=dict(os.environ);env['CFLAGS']='-O0 -g0';env['CXXFLAGS']='-O0 -g0'
        with log.open('ab') as f:
            conf=[str(source/'configure')]
            f.write(('\n$ CFLAGS="-O0 -g0" '+conf[0]+'\n').encode());f.flush()
            cp=subprocess.run(conf,cwd=obj,env=env,stdout=f,stderr=subprocess.STDOUT,timeout=240)
            if cp.returncode:raise RuntimeError('configure rc '+str(cp.returncode))
        call(['make','-j2','sqlite3.c'],obj,log,360)
        call(['gcc','-fPIC','-O0','-g0','-shared','-DSQLITE_THREADSAFE=1','sqlite3.c','-o',str(b/'libquery.so'),'-ldl','-lpthread','-lm'],obj,log,300)
        record.update({'manifest':mf,'git_archive_url':'https://codeload.github.com/sqlite/sqlite/tar.gz/'+sha,'lib_sha256':hashlib.sha256((b/'libquery.so').read_bytes()).hexdigest(),'amalgamation_sha256':hashlib.sha256((obj/'sqlite3.c').read_bytes()).hexdigest(),'compiler':out(['gcc','-dumpfullversion'],b),'cflags':'-fPIC -O0 -g0 -shared -DSQLITE_THREADSAFE=1','host_arch':out(['uname','-m'],b),'status':'built'})
        receipt.write_text(json.dumps(record,indent=2)+'\n')
        print('BUILT',sha,mf,flush=True)
    except Exception as e:
        record.update({'status':'failed','error':str(e)})
        (b/'failure.json').write_text(json.dumps(record,indent=2)+'\n')
        print('FAILED',sha,str(e),flush=True)
def main():
    plan=json.loads((root/'plan.json').read_text())
    refs={}
    for case in plan:
        for _,v in case['versions'].items():refs[v['git']]=v['fossil']
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(build,refs.items()))
if __name__=='__main__':main()
