"""Prepare exactly the two explicitly authorized initialization retries."""
import datetime,hashlib,json,pathlib,shutil,sys,tarfile
OUT=pathlib.Path(__file__).resolve().parent;ROOT=OUT.parent
sys.path.insert(0,str(ROOT))
from run_boundary_core import validate_manifest
def read(p):return json.loads(pathlib.Path(p).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def save(p,x):
    with p.open('x',encoding='utf-8') as f:json.dump(x,f,ensure_ascii=False,indent=2)
tasks=['mysql-79813-8.0.34','mysql-112910-8.0.35']
summary=read(ROOT/'current_boundary_summary.json')
assert set(summary['unresolved_tasks'])==set(tasks)
prior={str(p):sha(p) for p in ROOT.rglob('*') if p.is_file() and OUT not in p.parents}
save(OUT/'before_file_hashes.json',prior)
for name in ['current_boundary_results.json','current_boundary_summary.json']:
    shutil.copyfile(ROOT/name,OUT/('before_'+name))
authorization={'user_instruction':'对剩余两项启动超时的用例各重试一次，完成前版对照并更新清单，保留之前的失败记录。',
 'task_ids':tasks,'maximum_retries_per_item':1,'parallel_containers':1,
 'limits':read(ROOT/'protocol.json')['runtime_limits'],'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'failure_retention':'Original batch_001 records remain unchanged. attempt_number=2; repeat=1 denotes first possible submitted source SQL, because attempt1 submitted none.'}
save(OUT/'authorization.json',authorization)
wave=ROOT/'batch_004';wave.mkdir(exist_ok=False)
plan=read(ROOT/'batch_003/plan.json')
plan={k:plan[k] for k in ['max_parallel','data_threshold_per_case_bytes','retention_threshold_bytes','minimum_free_disk_bytes']}
plan.update(task_ids=tasks,cases=[],retry_authorization=authorization)
for task in tasks:
    source=ROOT/'retrieved/batch_001'/task
    record=read(source/'results/records.jsonl')
    assert record['task_id']==task and record['sql_submitted'] is False
    assert record['blocked_reason']=='Environment/initialization boundary: Startup time limit reached'
    cleanup=read(next((source/'results').glob('cleanup-*.json')))
    assert cleanup['stop']['returncode']==0 and cleanup['state']['Status']=='exited'
    assert not list(ROOT.glob('retrieved/batch_00[4-9]/'+task+'/results/records.jsonl'))
    d=wave/task;d.mkdir()
    for name in ['source.sql','postcheck.sql','review.json','oracle.json']:shutil.copyfile(source/name,d/name)
    shutil.copyfile(source/'results/records.jsonl',d/'previous_attempt_record.json')
    m=read(source/'manifest.json')
    m['run_id']='boundary_004_'+m['cases'][0]['report_id']+'_'+record['target_version'].replace('.','_')+'_retry1'
    r=m['cases'][0]['runs'][0]
    r.update(run_id=record['run_id']+'_retry1',attempt_number=2,retry_of_run_id=record['run_id'])
    m['authorized_initialization_retry']={'prior_record_file':'previous_attempt_record.json','prior_record_sha256':sha(d/'previous_attempt_record.json'),
        'prior_sql_submitted':False,'retry_number':1,'maximum_retries':1,'authorization':authorization}
    save(d/'manifest.json',m);validate_manifest(d/'manifest.json')
    plan['cases'].append({'task_id':task,'manifest_sha256':sha(d/'manifest.json')})
save(wave/'plan.json',plan)
for name in ['run_boundary_core.py','run_boundary_case.py','run_boundary_batch.py']:
    shutil.copyfile(ROOT/'batch_003'/name,wave/name)
files=sorted(p for p in wave.rglob('*') if p.is_file())
save(wave/'hashes.json',{p.relative_to(wave).as_posix():sha(p) for p in files})
with tarfile.open(ROOT/'batch_004.tar.gz','x:gz') as t:
    for p in files+[wave/'hashes.json']:t.add(p,arcname=p.relative_to(ROOT).as_posix())
print(json.dumps({'batch':'batch_004','tasks':tasks,'parallel':1,'retry_number':1}))
