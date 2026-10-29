"""One fresh container per frozen report/version; bounded retained data monitoring."""
import json,subprocess,sys,threading,time
from pathlib import Path
import run_boundary_core as core

core.PURPOSE='mysql-adjacent-version-boundary-20261029'
original_environment=core.Batch.environment
def environment(self,name,version,image_info):
    result=original_environment(self,name,version,image_info)
    result['optimizer_switch_probe']=self.query(name,'SELECT @@optimizer_switch AS optimizer_switch;\n')
    if result['optimizer_switch_probe']['returncode'] != 0:raise RuntimeError('Optimizer settings not recorded')
    return result
core.Batch.environment=environment
original_stop=core.Batch.stop_owned
def stop_owned(self,name,version):
    with self.monitor_lock:
        self.monitor_data_enabled=False
    return original_stop(self,name,version)
core.Batch.stop_owned=stop_owned
original_budget=core.Batch.budget
def budget(self):
    return original_budget(self)
core.Batch.budget=budget

if __name__=='__main__':
    manifest=Path(sys.argv[1]); out=Path(sys.argv[2])
    m,rows=core.validate_manifest(manifest)
    assert len(rows)==1 and len(m['cases'])==1
    b=core.Batch(manifest,out)
    b.monitor_lock=threading.Lock()
    b.monitor_data_enabled=True
    finished=threading.Event()
    def monitor():
        while not finished.wait(1):
            for name in list(b.owned):
                with b.monitor_lock:
                    if not b.monitor_data_enabled:return
                    if b.owns(name) and b.state(name).get('Running'):
                        q=b.docker('exec',name,'du','-sk','/var/lib/mysql',timeout=10)
                        core.save(out/'data_usage.json',q)
                        if q['returncode'] != 0:
                            b.halt('Container data usage probe failed; preserve evidence')
                        elif int(q['stdout'].split()[0])*1024>2*1024**3:
                            b.halt('Per-case retained data budget exceeded (2 GiB monitored threshold)')
            if not b.budget():
                for name in list(b.owned):
                    if b.owns(name) and b.state(name).get('Running'):
                        core.save(out/'resource_stop.json',b.docker('stop','-t','2',name,timeout=15))
                return
    t=threading.Thread(target=monitor,daemon=True);t.start()
    try:rc=b.run()
    finally:finished.set();t.join(timeout=20)
    sys.exit(rc)
