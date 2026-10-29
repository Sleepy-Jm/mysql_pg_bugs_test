import concurrent.futures,hashlib,json,shutil,subprocess,sys,threading
from pathlib import Path
ROOT=Path(__file__).resolve().parent
assert ROOT.parent==Path('<EXPERIMENT_ROOT>/mysql_version_boundary_20261029')
plan=json.loads((ROOT/'plan.json').read_text())
for p,h in json.loads((ROOT/'hashes.json').read_text()).items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
with (ROOT/'EXECUTION_CLAIM.json').open('x') as f:json.dump({'planned_items':plan['task_ids']},f)
stop=threading.Event()
def one(item):
    task=item['task_id'];d=ROOT/task
    if stop.is_set():return {'task_id':task,'status':'not_started_after_failure'}
    # Reserve full per-case threshold for each existing data directory; no
    # host permission changes to mysql-owned files are required.
    reserved=2*plan['data_threshold_per_case_bytes']
    for data in ROOT.parent.glob('batch_*/*/results/data'):
        usage=data.parent/'data_usage.json'
        if usage.exists():
            recorded=json.loads(usage.read_text())
            reserved += int(recorded['stdout'].split()[0])*1024 if recorded.get('returncode')==0 else plan['data_threshold_per_case_bytes']
        else:reserved += plan['data_threshold_per_case_bytes']
    if reserved>plan['retention_threshold_bytes'] or shutil.disk_usage(ROOT).free<plan['minimum_free_disk_bytes']:
        stop.set();return {'task_id':task,'status':'disk_precheck_blocked'}
    with (d/'runner_stdout.txt').open('x') as out,(d/'runner_stderr.txt').open('x') as err:
        p=subprocess.run(['python3','-u','-B',str(ROOT/'run_boundary_case.py'),str(d/'manifest.json'),str(d/'results')],stdout=out,stderr=err)
    complete=json.loads((d/'results/completion.json').read_text()) if (d/'results/completion.json').exists() else {}
    # A boundary failure requires review before further batches; no automatic retries.
    if p.returncode or not complete.get('all_rows_recorded'):stop.set()
    result={'task_id':task,'returncode':p.returncode,'completion':complete}
    print(json.dumps(result),flush=True);return result
results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    it=iter(plan['cases']);active={}
    for _ in range(2):
        item=next(it,None)
        if item:active[pool.submit(one,item)]=item
    while active:
        done,_=concurrent.futures.wait(active,return_when=concurrent.futures.FIRST_COMPLETED)
        for f in done:
            results.append(f.result());active.pop(f)
            if not stop.is_set():
                item=next(it,None)
                if item:active[pool.submit(one,item)]=item
    for item in it:results.append({'task_id':item['task_id'],'status':'not_started_after_failure'})
(ROOT/'batch_completion.json').write_text(json.dumps(results,indent=2))
