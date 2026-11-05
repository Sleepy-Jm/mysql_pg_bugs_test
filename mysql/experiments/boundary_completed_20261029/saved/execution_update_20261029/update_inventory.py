"""Build an append-only phase inventory from saved evidence and explicit decisions."""
import collections,datetime,hashlib,json,pathlib,sys
OUT=pathlib.Path(__file__).resolve().parent
ROOT=OUT.parent
def read(p):return json.loads(pathlib.Path(p).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def save(p,v):
    with p.open('x',encoding='utf-8') as f:json.dump(v,f,ensure_ascii=False,indent=2)
baseline=read(ROOT/'local_status_20261029/stage_status.json')
decisions={}
for p in sorted((OUT/'decisions').glob('*.json')):
    d=read(p);decisions[d['task_id']]=dict(d,decision_file=str(p))
records=collections.defaultdict(list)
unique={}
record_files=sorted(OUT.glob('progress_*/mysql-*/results/records.jsonl'))+sorted((ROOT/'retrieved').glob('batch_*/*/results/records.jsonl'))
for p in record_files:
    for s in p.read_text(encoding='utf-8').splitlines():
        r=json.loads(s);key=(r['task_id'],r['run_id'])
        if key in unique:assert unique[key]['record']==r
        unique[key]=dict(record=r,path=str(p),sha256=sha(p))
for evidence in unique.values():records[evidence['record']['task_id']].append(evidence)
rows=[]
for old in baseline['items']:
    tid=old['task_id'];rr=records.get(tid,[]);submitted=[r for r in rr if r['record'].get('sql_submitted')]
    decision=decisions.get(tid)
    state=old['saved_boundary_status'] if old['comparable_two_sided_evidence'] else 'unknown'
    reason=old['saved_basis'] if old['comparable_two_sided_evidence'] else old['missing_evidence']
    if decision:
        assert submitted and not old['comparable_two_sided_evidence']
        for path,h in decision['evidence_hashes'].items():assert sha(path)==h
        state=decision['boundary_status'];reason=decision['reason']
    elif rr:
        reason='; '.join(x['record'].get('blocked_reason') or '已提交 SQL，结果待按 oracle 判定' for x in rr)
    execution=('historical_comparable_pair_reused' if old['comparable_two_sided_evidence'] else
               ('completed_and_adjudicated' if decision else 'submitted_pending_adjudication') if submitted else
               'initialization_failed_sql_not_submitted' if rr else 'not_started')
    review=old['saved_review'];oracle=review.get('oracle',{})
    phenomenon=review.get('phenomenon_type') or oracle.get('phenomenon') or oracle.get('kind') or review.get('oracle_kind') or 'report_phenomenon_type_not_explicit'
    rows.append(dict(task_id=tid,report_id=old['report_id'],target_version=old['target_version'],previous_version=old['previous_version'],
        boundary_status=state,reason=reason,phenomenon=phenomenon,execution_status=execution,new_actual_runs=len(submitted),
        new_attempt_records=len(rr),historical_comparable_pair_reused=old['comparable_two_sided_evidence'],
        new_records=rr,decision=decision,target_review_path=old['evidence_paths'][0],baseline_path=str(ROOT/'local_status_20261029/stage_status.json')))
counts={}
for v in ['8.0.32','8.0.33','8.0.34','8.0.35']:
    a=[r for r in rows if r['target_version']==v]
    counts[v]=dict(total=len(a),historical_pairs=sum(r['historical_comparable_pair_reused'] for r in a),
        new_executed_items=sum(r['new_actual_runs']>0 for r in a),new_actual_runs=sum(r['new_actual_runs'] for r in a),
        new_normal_previous=sum(bool(r['decision']) and r['boundary_status']=='observed_new_at_release' for r in a),
        new_same_anomaly_previous=sum(bool(r['decision']) and r['boundary_status']=='pre_existing' for r in a),
        cumulative_new_at_release=sum(r['boundary_status']=='observed_new_at_release' for r in a),
        cumulative_pre_existing=sum(r['boundary_status']=='pre_existing' for r in a),
        unresolved=sum(r['boundary_status']=='unknown' for r in a),
        startup_failed_no_sql=sum(r['execution_status']=='initialization_failed_sql_not_submitted' for r in a),
        not_started=sum(r['execution_status']=='not_started' for r in a))
    assert counts[v]['total']==counts[v]['cumulative_new_at_release']+counts[v]['cumulative_pre_existing']+counts[v]['unresolved']
old_inventory=read(ROOT/'local_status_20261029/original_file_inventory.json')
preservation={p:sha(p)==v['sha256'] for p,v in old_inventory.items()}
assert all(preservation.values())
result=dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope=106,
    original_target_results_unchanged=True,original_files_preserved=len(preservation),
    statistics_note='New runs are predecessor-control source SQL submissions only; initialization attempts and history copies are excluded. Target-stage 895/125/215/106 statistics remain unchanged.',
    counts_by_version=counts,items=rows)
result['totals']={k:sum(c[k] for c in counts.values()) for k in next(iter(counts.values()))}
assert result['totals']['total']==106
assert result['totals']['historical_pairs']+result['totals']['new_executed_items']+result['totals']['startup_failed_no_sql']+result['totals']['not_started']==106
result['phase_limits']=read(ROOT/'protocol.json')['runtime_limits']
result['new_run_repeat_count']=1
result['old_target_stage_counters']={'candidate_items':895,'executed_items':125,'actual_runs':215,'reproduced_items':106,'changed_by_this_phase':False}
dest=OUT/sys.argv[1];dest.mkdir(exist_ok=False)
save(dest/'current_inventory.json',result)
save(dest/'preservation_audit.json',{'checked_original_files':len(preservation),'all_unchanged':True})
lines=['MySQL 相邻版本回放清单更新','生成时间 UTC：'+result['time_utc'],
    '统计单位：报告编号 × 目标版本。新增运行只统计实际提交用例 SQL；初始化失败不计实际运行。',
    '历史目标版实验 895 候选项、125 已执行项、215 次运行、106 已复现项不因本阶段前版对照而增加。',
    '目标版本 | 项数 | 历史两侧项 | 新增执行项/运行次 | 累计前版正常目标异常 | 累计前版同样异常 | 边界未知 | 启动失败未提交SQL | 尚未启动']
for v,c in counts.items():lines.append(f"{v} | {c['total']} | {c['historical_pairs']} | {c['new_executed_items']}/{c['new_actual_runs']} | {c['cumulative_new_at_release']} | {c['cumulative_pre_existing']} | {c['unresolved']} | {c['startup_failed_no_sql']} | {c['not_started']}")
total=result['totals']
lines += [f"合计 | {total['total']} | {total['historical_pairs']} | {total['new_executed_items']}/{total['new_actual_runs']} | {total['cumulative_new_at_release']} | {total['cumulative_pre_existing']} | {total['unresolved']} | {total['startup_failed_no_sql']} | {total['not_started']}",
          '',f"新增判定：前版正常 {total['new_normal_previous']} 项，前版已有同样异常 {total['new_same_anomaly_previous']} 项。新执行项各运行1次；不声称已做多轮稳定性确认。",
          f"守恒：历史已有前版证据 {total['historical_pairs']} + 本轮实际执行 {total['new_executed_items']} + 初始化失败未执行SQL {total['startup_failed_no_sql']} + 尚未启动 {total['not_started']} = 106。",
          '未解决项目：'+ '、'.join(r['task_id'] for r in rows if r['boundary_status']=='unknown')]
lines+=['','新增记录与判定：']
for r in rows:
    if r['new_records']:
        lines.extend([r['task_id']+'：'+r['execution_status']+'；'+r['boundary_status'],r['reason']])
        lines.extend(x['path'] for x in r['new_records'])
        if r['decision']:lines.append(r['decision']['decision_file'])
lines+=['','逐项清单：']
for r in rows:lines.append(r['task_id']+' | '+r['execution_status']+' | '+r['boundary_status']+' | '+str(r['reason']))
lines+=['','证据与执行边界：',
    'batch_001：4 项启动尝试，实际提交 SQL 2 项/2 次，2 项因启动超过 180 秒受阻；4 个容器均有停止成功、exited 的保存证据。',
    'batch_002：仅本地准备，未上传未运行；全部 91 项由降低并发的 batch_003 承接，task_id 不变。',
    'batch_003：单并发，未重试 batch_001 失败的两项；以保存的 records/completion 为准，上传和准备不等同实际 SQL 执行。',
    '初始化超时属于条件不足，不是目标 Bug 的正常或异常 oracle 结果；不自动重启、恢复或增加超时上限。',
    '本次使用冻结镜像 ID，每项保存实际版本、环境、源 SQL、输出、错误码及清理记录；外层批次退出码 0 不代表每个子任务成功。',
    '旧 server_preflight.json 的独立退出码与审批回执仍未知；不能由本次运行反推旧预检审批。',
    '本地约束测试 5 项通过，记录见 ../local_contract_test_workspace_tmp.json；首次默认临时目录权限错误单独保留。',
    f'原有 {len(preservation)} 个文件哈希均保持不变；现有结果仅证明所记录条件下的相邻版本现象，不能推出引入提交或独立根因数。']
with (dest/'execution_report.txt').open('x',encoding='utf-8') as f:f.write('\n'.join(lines)+'\n')
print(json.dumps({'counts':counts,'output':str(dest)},ensure_ascii=False))
