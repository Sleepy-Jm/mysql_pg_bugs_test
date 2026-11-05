"""Compare frozen report phenomena across versions without inferring root causes."""
import csv
import datetime
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path('experiments/pg_report_replay_20261104/run_001')
REMOTE = '/mnt/sdb/dufei/pg_report_replay_20261104_run001'
LABELS = {'reproduced': '已复现报告现象', 'not_reproduced': '有效重放后未复现',
          'inconclusive': '资料或环境不足，无法判断', 'other_anomaly': '出现其他异常，尚不能归因',
          'execution_failed': '未执行或执行失败', 'not_run': '未执行或执行失败'}


def compare(previous, target, following):
    if target == 'reproduced' and previous == 'reproduced':
        introduction = '前一相邻版本已有报告现象；不支持目标小版本新引入'
    elif target == 'reproduced' and previous == 'not_reproduced':
        introduction = '候选引入区间：前一相邻版本到目标版本；尚未确认引入提交或独立根因'
    elif target == 'reproduced':
        introduction = '目标版出现报告现象，前版证据不足；引入边界无法判断'
    elif target == 'not_reproduced':
        introduction = '目标版本有效重放未出现报告现象；原因未确定，不能判断引入'
    else:
        introduction = '目标版本判定或执行不完整；引入边界无法判断'
    disappearance = ('后一相邻版本有效重放未出现报告现象；仅为现象消失边界，未确认修复提交'
                     if target == 'reproduced' and following == 'not_reproduced' else '')
    return introduction, disappearance


def write_csv(path, rows):
    if not rows:
        return
    fields = list(dict.fromkeys(k for row in rows for k in row))
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
        w.writerows({k: json.dumps(v, ensure_ascii=False) if isinstance(v,(list,dict)) else v
                     for k,v in row.items()} for row in rows)


def main():
    reports = json.loads((ROOT/'frozen_reports.json').read_text(encoding='utf-8'))
    specs = [s for p in sorted(ROOT.glob('prepared_specs*.json'))
             for s in json.loads(p.read_text(encoding='utf-8'))]
    superseded = {s['supersedes_spec_sha256'] for s in specs if 'supersedes_spec_sha256' in s}
    active = [s for s in specs if s['spec_sha256'] not in superseded]
    batches = json.loads((ROOT/'execution_snapshot.json').read_text(encoding='utf-8'))
    attempts = [dict(x,batch=b.removesuffix('_results.json')) for b,rs in batches.items()
                for x in rs if x['spec_sha256'] not in superseded]
    configure = json.loads((ROOT/'configure_results.json').read_text(encoding='utf-8'))
    if configure:
        report = next(r for r in reports if r['report_id']=='17466')
        imported = dict(report_id='17466',scenario_id='17466_configure',target_version='14.2',
            source_url=report['source_url'],parts=[dict(source=str(ROOT/'source_text/17466.txt'))],
            mode='configure_not_sql',oracle=configure[0]['oracle'],
            notes='单列configure执行；不是SQL重放或数据库运行时bug。')
        imported['spec_sha256'] = hashlib.sha256(json.dumps(imported,sort_keys=True).encode()).hexdigest()
        active.append(imported)
        attempts.extend(dict(x,spec_sha256=imported['spec_sha256'],scenario_id=imported['scenario_id'],
            batch='configure_replay_17466',stage='configure',trigger_output=x.get('CFLAGS',''),
            evidence_override=f"{REMOTE}/configure_replay_17466/{x['version']}/result.json") for x in configure)
    by_key = {}
    for x in attempts:
        key = x['spec_sha256'], x['version']
        if key in by_key:
            raise ValueError('Repeated active spec/version needs explicit attempt selection: '+str(key))
        by_key[key] = x
    scenarios = []
    executions = []
    for s in active:
        major,minor = map(int,s['target_version'].split('.'))
        versions = [f'{major}.{n}' for n in [minor-1,minor,minor+1]]
        statuses = []
        evidence = []
        for v in versions:
            x = by_key.get((s['spec_sha256'],v))
            status = x['status'] if x else 'not_run'
            statuses.append(status)
            path = x.get('evidence_override',f"{REMOTE}/attempts/{x['batch']}/{s['scenario_id']}/{v}/result.json") if x else ''
            evidence.append(path)
            executions.append(dict(report_id=s['report_id'],scenario_id=s['scenario_id'],
                original_version_field=s['target_version'],version=v,version_role=['previous','target','following'][len(statuses)-1],
                spec_sha256=s['spec_sha256'],execution_kind=s.get('mode','psql'),build_variant=s.get('build_variant','ordinary'),
                sql_sources=[p['source'] for p in s['parts']],source_url=s['source_url'],
                oracle=s['oracle'],status=status,main_result=LABELS[status],
                execution_substatus='completed' if status in ['reproduced','not_reproduced','other_anomaly'] else status,
                stage=x.get('stage','') if x else '',reason=x.get('reason','') if x else 'not executed',
                actual_version=x.get('actual_version','') if x else '',
                actual_config=x.get('config',{}) if x else {},
                build_manifest=x.get('build_manifest',{}) if x else {},
                trigger_output=x.get('trigger_output','') if x else '',evidence=path))
        intro,disappearance = compare(*statuses)
        scenarios.append(dict(report_id=s['report_id'],scenario_id=s['scenario_id'],
            target_version=s['target_version'],execution_kind=s.get('mode','psql'),build_variant=s.get('build_variant','ordinary'),
            version_role='client' if s.get('server_version') else 'server',
            fixed_server_version=s.get('server_version',''),
            previous_version=versions[0],previous_status=statuses[0],target_status=statuses[1],
            following_version=versions[2],following_status=statuses[2],
            introduction_assessment=intro,disappearance_assessment=disappearance,
            reported_phenomenon=s['oracle']['reported_phenomenon'],
            author_expected_behavior=s['oracle']['author_expected_behavior'],
            source_url=s['source_url'],spec_sha256=s['spec_sha256'],evidence=evidence,
            notes=s.get('notes','')))
    audit = {r['report_id']:r for r in json.loads((ROOT/'source_audit.json').read_text(encoding='utf-8'))}
    rows = []
    for r in reports:
        ss = [s for s in scenarios if s['report_id']==r['report_id']]
        target = [e for e in executions if e['report_id']==r['report_id'] and e['version_role']=='target']
        counts = Counter(e['status'] for e in target)
        # A report may have multiple explicitly separate build/scenario results.
        if counts['reproduced']:
            main = LABELS['reproduced']
        elif counts['inconclusive']:
            main = LABELS['inconclusive']
        elif counts['other_anomaly']:
            main = LABELS['other_anomaly']
        elif counts['not_reproduced']:
            main = LABELS['not_reproduced']
        elif ss:
            main = LABELS['not_run']
        else:
            main = LABELS['inconclusive']
        a = audit[r['report_id']]
        rows.append(dict(report_id=r['report_id'],original_version_field=r['version_field'],
            source_url=r['source_url'],title=r['title'],main_result=main,
            execution_substatus='not_run_missing_material_or_environment' if not ss else dict(counts),
            scenario_count=len(ss),target_scenario_statuses=dict(counts),
            introduction_assessments=[s['introduction_assessment'] for s in ss],
            disappearance_assessments=[s['disappearance_assessment'] for s in ss if s['disappearance_assessment']],
            reason_or_gap=a['review_note'] if not ss else [e['reason'] for e in target if e['status'] not in ['reproduced','not_reproduced']],
            source_audit_disposition=a['review_disposition'],
            evidence=[e['evidence'] for e in target] or [x['path'] for x in a['evidence']]))
    assert len(rows)==len(reports) and len({r['report_id'] for r in rows})==len(rows)
    summary = dict(snapshot_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        report_count=len(rows),version_item_count=len(rows),reports_with_scenarios=sum(bool(r['scenario_count']) for r in rows),
        reports_without_executable_scenario=sum(not r['scenario_count'] for r in rows),
        active_scenarios=len(scenarios),planned_scenario_version_items=len(executions),
        configuration_scenarios=sum(s['execution_kind']=='configure_not_sql' for s in scenarios),
        executed_scenario_version_items=sum(e['status']!='not_run' for e in executions),
        report_main_results=dict(Counter(r['main_result'] for r in rows)),
        target_scenario_statuses=dict(Counter(e['status'] for e in executions if e['version_role']=='target')),
        unexecuted_dispositions=dict(Counter(r['source_audit_disposition'] for r in rows if not r['scenario_count'])),
        introduction_assessments=dict(Counter(s['introduction_assessment'] for s in scenarios)),
        candidate_minor_introduction_scenarios=sum(s['introduction_assessment'].startswith('候选引入区间') for s in scenarios),
        candidate_disappearance_scenarios=sum(bool(s['disappearance_assessment']) for s in scenarios),
        root_cause_confirmed_new_bugs=None,
        limitation='Report phenomena and version boundaries only; no independent root-cause deduplication or introduction-commit confirmation.')
    for name,value in [('version_comparison.json',scenarios),('all_report_results.json',rows),
                       ('all_execution_results.json',executions),('version_comparison_summary.json',summary)]:
        (ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
    write_csv(ROOT/'version_comparison.csv',scenarios)
    write_csv(ROOT/'all_report_results.csv',rows)
    write_csv(ROOT/'all_execution_results.csv',executions)
    lines = ['# PG 全部报告处理与相邻版本对照','',f"证据快照 UTC：{summary['snapshot_utc']}",'',
             f"冻结集合 {len(rows)} 份报告，逐项均保留。具备已冻结执行场景的报告 {summary['reports_with_scenarios']} 份；缺必要资料/平台/判据或不适用运行时回放的报告 {summary['reports_without_executable_scenario']} 份。",
             f"场景×版本项 {len(executions)}，已执行 {summary['executed_scenario_version_items']} 项。报告、场景、版本项和执行次数不可混计。",'',
             '这里的复现指报告描述的现象，包含符合设计的行为及客户端/配置问题，不能直接当作确认的数据库bug。前版也出现现象，只能排除该目标小版本首次引入该现象；不能证明它从未由更早版本变更引入。',
             '前版未出现、目标版出现，只形成候选版本区间；确认新引入bug还需核对前提、重复复现与定位提交/根因。后版不再出现也不直接证明修复根因。',
             '不同构建场景分别比较；17456固定13.6服务端，对比14.x客户端。旧尝试及superseded记录保留，现行统计按显式替代关系排除。','',
             '## 目标版本按报告汇总','', '|主结果|报告数|','|---|---:|']
    lines += [f'|{k}|{v}|' for k,v in summary['report_main_results'].items()]
    lines += ['', '多场景报告的汇总采用：有任一场景复现则记“已复现报告现象”，详细表仍保留其他场景的异常及缺口；这不表示其他场景完成。','',
              '## 相邻版本判断（按独立执行场景）','', '|判断|场景数|','|---|---:|']
    lines += [f'|{k}|{v}|' for k,v in summary['introduction_assessments'].items()]
    focus={'18801_module_count_revision1','18810_nocassert','18792_linked_config_nocassert',
           '17462_instrumented','17424_main','17437_main'}
    short={'reproduced':'复现报告现象','not_reproduced':'有效未复现','inconclusive':'无法判断',
           'other_anomaly':'其他异常','execution_failed':'执行失败','not_run':'尚未执行'}
    lines += ['', '## 本轮重点对照','', '|报告/场景|前版|目标版|后版|', '|---|---|---|---|']
    lines += [f"|{s['scenario_id']}|{s['previous_version']}：{short[s['previous_status']]}|{s['target_version']}：{short[s['target_status']]}|{s['following_version']}：{short[s['following_status']]}|"
              for s in scenarios if s['scenario_id'] in focus]
    lines += ['', '## 文件入口','', '- `all_report_results.csv`：全部136份报告，包括未执行项和具体缺口。',
              '- `all_execution_results.csv`：目标版、前版、后版的环境、oracle、实际现象、阶段和证据路径。',
              '- `version_comparison.csv`：每个场景的三版本对照和引入/消失边界判断。',
              '- `execution_snapshot.json`：服务器原始结果，保留原判定。',
              '- `source_audit.csv`：逐份来源及缺口审查。',
              '- `continuation_20261104/initial_server_snapshot.json`：本轮继续执行前的服务器快照。','',
              '## 继续执行的修订与限制','',
              '- 18801：首次把每模块优化前/后两个bitcode文件重复计数；依据LLVM源码及报告示例改为统计未优化模块文件，保留总文件数。原SQL与10001判据不变，旧尝试显式替代，三版本重新执行。',
              '- 17462：首次构建的--with-valgrind被PG14忽略，缺USE_VALGRIND，阴性无效。改用源码要求的-DUSE_VALGRIND并验证预处理宏，旧尝试不计有效未复现；原负载及oracle不变。',
              '- 17462原文指向1e0dfd166b3，其主题为增加Valgrind缓冲区访问检测。官方回复明确区分“检测开始报告”与更早存在的底层缺陷，不据此宣称缺陷由该提交引入。',
              '- 17437仅有定性时间归因描述，无明确量化阈值；保留原SQL及JIT开/关完整观测，主结果仍无法判断，不按输出事后编造阈值。',
              '- 18792链接的官方讨论明确给出直接修改postgresql.conf并重载的步骤；该关联场景与原ALTER SYSTEM路径分列，不补造复制槽。18792/18810可能同根因，不计为两个独立bug。',
              '- clang/LLVM/Valgrind及debug/cassert差异均记录在各执行证据中；Linux执行不能验证原Windows/macOS/HA拓扑场景。','',
              '## 尚未执行的报告及缺口','', '|报告|来源/环境缺口|','|---|---|']
    lines += [f"|{r['report_id']}|{str(r['reason_or_gap']).replace('|','/')}|" for r in rows if not r['scenario_count']]
    (ROOT/'VERSION_COMPARISON.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
