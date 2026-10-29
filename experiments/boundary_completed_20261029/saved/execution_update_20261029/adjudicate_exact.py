"""Conservative equivalence proof against a frozen, reviewed abnormal target.
Only complete, error-free transcripts with identical statements/results/warnings
and matching recorded environments enter this path. Other cases need review.
"""
import json,pathlib,subprocess,sys
OUT=pathlib.Path(__file__).resolve().parent
label=sys.argv[1];p=OUT/(label+'_pair_inspection.json')
items=json.loads(p.read_text(encoding='utf-8'));spec=[];pending=[]
for x in items:
    tid=x['task_id'];r=x['record'];tr=x['target_record'];review=x['review']
    if (OUT/'decisions'/(tid+'.json')).exists():continue
    eligible=(x['exact_transcript_equal'] and x['same_statement_sequence'] and len(x['previous_segments'])>0
        and any(s['result_lines'] for s in x['previous_segments'])
        and not x['previous_stderr'] and not x['target_stderr']
        and r.get('execution_status')=='completed' and r.get('returncode')==0 and tr.get('returncode')==0
        and tr.get('actual_version')==review['target_version']
        and not x['environment_diff'] and not x['environment_missing_keys'] and not x['optimizer_switch_diff']
        and review['source_review_complete'])
    if not eligible:pending.append(tid);continue
    oracle=review['oracle']
    expected=next((oracle[k] for k in ['reported','reproduced','reproduced_when','reported_result_sets','failure'] if k in oracle),'见冻结 oracle 与目标审核记录')
    spec.append(dict(task_id=tid,inspection=p.name,boundary_status='pre_existing',
        method='Exact full statement/result/warning equivalence to source-reviewed target; actual-source/postcheck hashes and recorded environment matched; no SQL errors',
        reason='前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象：'+json.dumps(expected,ensure_ascii=False)))
name=label+'_exact_decisions.json'
with (OUT/name).open('x',encoding='utf-8') as f:json.dump(spec,f,ensure_ascii=False,indent=2)
if spec:subprocess.run([sys.executable,'-B',str(OUT/'save_decisions.py'),name],check=True)
print(json.dumps({'exact_proven':len(spec),'needs_review':pending},ensure_ascii=False))
