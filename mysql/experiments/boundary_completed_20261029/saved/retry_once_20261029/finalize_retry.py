"""Audit the authorized retries, retain old failures, and update current indexes."""
import datetime,hashlib,json,pathlib
OUT=pathlib.Path(__file__).resolve().parent;ROOT=OUT.parent
def read(p):return json.loads(pathlib.Path(p).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def save(p,x):
    with p.open('x',encoding='utf-8') as f:json.dump(x,f,ensure_ascii=False,indent=2)
before=read(OUT/'before_file_hashes.json')
assert all(pathlib.Path(p).is_file() and sha(p)==h for p,h in before.items())
tasks=set(read(OUT/'authorization.json')['task_ids'])
base=ROOT/'retrieved/batch_004';hashes=read(base/'evidence_hashes.json')
assert all(sha(base/p)==h for p,h in hashes.items())
completion=read(base/'batch_completion.json')
assert len(completion)==2 and {r['task_id'] for r in completion}==tasks
assert all(r['returncode']==0 and r['completion']['halt_reason'] is None for r in completion)
pairs=read(ROOT/'execution_update_20261029/batch_004_pair_inspection.json')
assert {x['task_id'] for x in pairs}==tasks
proofs=[]
for x in pairs:
    tid=x['task_id'];r=x['record'];result=base/tid/'results'
    oldpath=ROOT/'retrieved/batch_001'/tid/'results/records.jsonl';old=read(oldpath)
    assert old['sql_submitted'] is False and 'Startup time limit reached' in old['blocked_reason']
    assert r['sql_submitted'] and r['returncode']==0 and r['execution_status']=='completed'
    assert r['attempt_number']==2 and r['retry_of_run_id']==old['run_id'] and r['run_id'].endswith('_retry1')
    assert r['requested_version']==x['review']['previous_version']==r['actual_version']
    assert r['script_sha256']==old['script_sha256'] and r['postcheck_sha256']==old['postcheck_sha256']
    assert x['exact_transcript_equal'] and x['same_statement_sequence'] and not x['previous_stderr']
    assert not x['environment_diff'] and not x['environment_missing_keys'] and not x['optimizer_switch_diff']
    env=read(result/r['environment_file'])
    assert sha(result/r['executed_sql_file'])==r['executed_sql_sha256'] and sha(result/r['environment_file'])==r['environment_manifest_sha256']
    assert env['network']=='none' and env['published_ports']==[] and env['cpus']==2 and env['memory_bytes']==2147483648 and env['pids_limit']==256
    assert x['cleanup']['stop']['returncode']==0 and x['cleanup']['state']['Status']=='exited' and not x['cleanup']['state']['Running']
    if x['review']['report_id']=='79813':
        lines=next(s['result_lines'] for s in x['previous_segments'] if 'JSON_OBJECT' in s['sql'])
        objs=[json.loads(line) for line in lines[1:]]
        assert len(objs)==3 and [o['can_edit'] for o in objs]==[1,0,1]
        assert all(type(o['can_edit']) is int and o['is_true'] is True and o['is_false'] is False for o in objs)
    else:
        queries=[s for s in x['previous_segments'] if s['sql'].upper().startswith('SELECT')]
        assert queries[0]['result_lines']==[] and queries[1]['result_lines']==['column_0\tcolumn_1','a\t0']
        assert queries[2]['result_lines']==['expected_constant\tdiv_precision','0.0625\t4']
    proofs.append({'task_id':tid,'old_failed_record':str(oldpath),'old_failed_record_sha256':sha(oldpath),
        'retry_record':str(result/'records.jsonl'),'retry_record_sha256':sha(result/'records.jsonl'),
        'actual_version':r['actual_version'],'source_sql_submissions_this_retry':1,'retries_performed':1,
        'container_name':x['cleanup']['container_name'],'confirmed_stopped':True,'boundary_status':'pre_existing'})
inventory=read(ROOT/'execution_update_20261029/after_retry_001/current_inventory.json')
assert inventory['totals']['total']==106 and inventory['totals']['new_actual_runs']==95
assert inventory['totals']['cumulative_new_at_release']==15 and inventory['totals']['cumulative_pre_existing']==91 and inventory['totals']['unresolved']==0
assert sum(r['new_attempt_records'] for r in inventory['items'])==97
for tid in tasks:
    item=next(r for r in inventory['items'] if r['task_id']==tid)
    assert item['new_attempt_records']==2 and item['new_actual_runs']==1
    assert sum(not r['record']['sql_submitted'] for r in item['new_records'])==1
    assert sum(bool(r['record']['sql_submitted']) for r in item['new_records'])==1
inventory['retry_update']={'batch':'batch_004','new_sql_runs_this_retry':2,'new_executed_items_this_retry':2,'maximum_retries_per_item':1,
    'historical_startup_failure_records_retained':2,'phase_attempt_records':97,'phase_actual_sql_runs':95,
    'phase_unique_sql_executed_items':95,'historical_comparable_items':11,'all_106_items_have_comparable_evidence':True,'items':proofs}
final=OUT/'final';final.mkdir(exist_ok=False)
save(final/'current_inventory.json',inventory)
summary={k:inventory[k] for k in ['time_utc','scope','counts_by_version','totals','old_target_stage_counters','new_run_repeat_count','retry_update']}
summary.update(report_path=str(final/'retry_report.txt'),inventory_path=str(ROOT/'current_boundary_results.json'),
    audit_path=str(final/'retry_audit.json'),unresolved_tasks=[])
save(final/'current_summary.json',summary)
save(final/'transport_receipt.json',{'batch':'batch_004','upload':'Verified payload extracted','local_launch_exit_code':0,
    'remote_outer_returncode':0,'collection_exit_code':0,'evidence_hash_verification':True,
    'approval_receipt':'Execution was permitted by tool; no separate structured review receipt returned.'})
lines=['MySQL 前版对照：两项授权重试完成报告','生成时间 UTC：'+datetime.datetime.now(datetime.timezone.utc).isoformat(),
    '本次各重试一次，新增实际执行2项、2次；两项均判为前版已有同样现象。新容器均确认停止。',
    '#79813/8.0.34：前版8.0.33返回三个 JSON 对象；can_edit 为数值1/0/1，直接布尔控制为 true/false，与目标版相同。',
    '#112910/8.0.35：前版8.0.34单行 VALUES 为空、两行 VALUES 错误返回(a,0)，直接 CAST 控制0.0625、div_precision=4，与目标版相同。',
    'source SQL、postcheck、实际版本、release构建、架构、关键环境及 optimizer_switch 已核对；没有新增重复 SQL 稳定性运行。',
    '', '目标版本 | 项数 | 本次新增执行/运行 | 阶段累计新增执行/运行 | 累计前版正常目标异常 | 累计前版同样异常 | 未决']
for v,c in inventory['counts_by_version'].items():
    n=int(v in ['8.0.34','8.0.35'])
    lines.append(f"{v} | {c['total']} | {n}/{n} | {c['new_executed_items']}/{c['new_actual_runs']} | {c['cumulative_new_at_release']} | {c['cumulative_pre_existing']} | {c['unresolved']}")
lines += ['合计 | 106 | 2/2 | 95/95 | 15 | 91 | 0','',
    '统计守恒：11项复用历史两侧证据 + 95项本阶段实际执行 = 106项；未执行0项、未决0项。',
    '阶段共有97条启动/执行尝试记录：95次实际用例SQL运行 + 2条原启动超时记录。原超时不计SQL运行、不删除，也不改写为成功。',
    '两项的 attempt_number=2；repeat=1 表示其第一次实际提交用例SQL，原 attempt1 没有提交SQL。',
    '资源和时间上限保持原样：单并发、2 CPU、2 GiB、256 PID、启动180秒、SQL20秒、单项600秒。',
    '历史目标版实验895候选项、125已执行项、215次运行、106已复现项未改动；本统计为前版对照，计数单位是报告编号×目标版本，不是独立根因数。','', '证据：']
for p in proofs:lines.extend([p['task_id'],'  原失败：'+p['old_failed_record'],'  重试：'+p['retry_record']])
lines += ['完整清单：'+str(ROOT/'current_boundary_results.json'),'当前摘要：'+str(ROOT/'current_boundary_summary.json'),
    '更新前清单快照：'+str(OUT/'before_current_boundary_results.json'),'更新前摘要快照：'+str(OUT/'before_current_boundary_summary.json'),
    '历史交付清单中 current_boundary_* 的旧哈希，可用上述逐字节快照核验；原历史报告、失败记录和日志均保持原样。']
(final/'retry_report.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
# Only the two explicitly current indexes are updated; their exact prior bytes
# were archived before any work and every other existing file is checked below.
for name,source in [('current_boundary_results.json',final/'current_inventory.json'),('current_boundary_summary.json',final/'current_summary.json')]:
    assert sha(ROOT/name)==before[str(ROOT/name)]
    assert sha(OUT/('before_'+name))==before[str(ROOT/name)]
    (ROOT/name).write_bytes(source.read_bytes())
changed=[p for p,h in before.items() if sha(p)!=h]
assert set(changed)=={str(ROOT/'current_boundary_results.json'),str(ROOT/'current_boundary_summary.json')}
audit={'prior_files_checked':len(before),'unchanged_prior_files':len(before)-2,'updated_current_indexes':changed,
    'prior_index_bytes_archived':True,'original_failure_records_unchanged':True,'new_evidence_hash_checks':len(hashes),
    'new_actual_runs':2,'retries_per_item':1,'both_new_containers_confirmed_stopped':True,'items':proofs,
    'phase_attempt_records':97,'phase_actual_sql_runs':95,'historical_failure_record_count':2}
save(final/'retry_audit.json',audit)
save(final/'historical_index_mapping.json',{p:{'before_sha256':before[p],'archived_path':str(OUT/('before_'+pathlib.Path(p).name)),'current_sha256':sha(p)} for p in changed})
files=sorted(p for p in final.iterdir() if p.is_file())+[ROOT/'current_boundary_results.json',ROOT/'current_boundary_summary.json']
save(final/'delivery_manifest.json',{str(p):{'sha256':sha(p),'bytes':p.stat().st_size} for p in files})
print(json.dumps({'totals':inventory['totals'],'retry_audit':audit,'report':str(final/'retry_report.txt')},ensure_ascii=False))
