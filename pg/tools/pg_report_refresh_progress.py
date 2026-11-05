"""Refresh auditable live preparation/execution counts across immutable batches."""
import csv
import datetime
import json
from collections import Counter
from pathlib import Path

ROOT=Path('experiments/pg_report_replay_20261104/run_001')


def main():
    reports=json.loads((ROOT/'frozen_reports.json').read_text(encoding='utf-8'))
    specs=[]
    for p in sorted(ROOT.glob('prepared_specs*.json')):specs.extend(json.loads(p.read_text(encoding='utf-8')))
    superseded={s['supersedes_spec_sha256'] for s in specs if 'supersedes_spec_sha256' in s}
    active=[s for s in specs if s['spec_sha256'] not in superseded]
    batches=json.loads((ROOT/'execution_snapshot.json').read_text(encoding='utf-8'))
    attempts=[dict(x,batch=b.removesuffix('_results.json')) for b,rs in batches.items() for x in rs]
    current=[x for x in attempts if x['spec_sha256'] not in superseded]
    audit={r['report_id']:r for r in json.loads((ROOT/'source_audit.json').read_text(encoding='utf-8'))} if (ROOT/'source_audit.json').exists() else {}
    rows=[]
    for r in reports:
        ss=[s for s in active if s['report_id']==r['report_id']]
        rr=[x for x in current if x['report_id']==r['report_id']]
        rows.append(dict(report_id=r['report_id'],original_version_field=r['version_field'],target_version=r['version_field'],source_url=r['source_url'],
                         preparation_status='prepared' if ss else audit.get(r['report_id'],{}).get('review_disposition','review_required'),
                         scenario_count=len(ss),source_fragment_count=sum(len(s['parts']) for s in ss),
                         sql_fragment_count=sum(p.get('material_kind','sql')=='sql' for s in ss for p in s['parts']),
                         oracle_count=len(ss),target_executions=sum(x['version']==x['target_version'] for x in rr),adjacent_executions=sum(x['version']!=x['target_version'] for x in rr),
                         target_results=';'.join(x['status'] for x in rr if x['version']==x['target_version']),
                         sql_sources=';'.join(p['source'] for s in ss for p in s['parts']),
                         reported_phenomenon=';'.join(s['oracle']['reported_phenomenon'] for s in ss),author_expected_behavior=';'.join(s['oracle']['author_expected_behavior'] for s in ss),
                         oracle_patterns=';'.join(s['oracle']['pattern'] for s in ss),spec_paths=';'.join(str(ROOT/'prepared'/s['scenario_id']/'spec.json') for s in ss),review_note=audit.get(r['report_id'],{}).get('review_note','')))
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    summary=dict(snapshot_utc=now,report_count=len(rows),prepared_reports=sum(bool(r['scenario_count']) for r in rows),
                 all_attempts=len(attempts),superseded_attempts=sum(x['spec_sha256'] in superseded for x in attempts),current_attempts=len(current),
                 target_attempts=sum(x['version']==x['target_version'] for x in current),adjacent_attempts=sum(x['version']!=x['target_version'] for x in current),
                 target_statuses=dict(Counter(x['status'] for x in current if x['version']==x['target_version'])),all_statuses=dict(Counter(x['status'] for x in current)))
    for name,value in [('preparation_inventory.json',rows),('execution_summary.json',summary)]:
        (ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
    with (ROOT/'preparation_inventory.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    lines=['# PostgreSQL SQL/oracle 与回放进度','',f'快照 UTC：{now}。这是进行中的统计，非全部回放完成报告。','',
           '|版本|Version字段入选项|已整理脚本/步骤与oracle|已执行目标项|已执行相邻项|','|---|---:|---:|---:|---:|']
    for v in ['14.1','14.2','17.1','17.2']:
        rr=[r for r in rows if r['target_version']==v]
        lines.append(f'|{v}|{len(rr)}|{sum(bool(r["scenario_count"]) for r in rr)}|{sum(r["target_executions"] for r in rr)}|{sum(r["adjacent_executions"] for r in rr)}|')
    lines+=['','17428 的展示换行修订保留原 oracle；旧尝试以 superseded 标记单独统计，不覆盖原证据。','',
            'SQL 片段、操作步骤、场景、报告与执行次数分别统计。配置/网络/客户端测试不是全部由SQL构成；目录片段数量不是SQL语句数。复现报告现象不等于确认独立bug。','',
            '```json',json.dumps(summary,ensure_ascii=False,indent=2),'```','',
            '## 对应文件','',
            '- [逐项准备与执行清单](preparation_inventory.csv)','- [来源审查与具体缺口](source_audit.csv)','- [冻结报告及 Version 字段](frozen_reports.json)',
            '- [实际执行快照](execution_snapshot.json)','- [脚本及冻结 oracle](prepared/)','- [原报告文字](source_text/)','- [官方讨论串](thread_text/)','- [附件及来源哈希](materials/manifest.json)','',
            '服务器原始尝试、日志和数据库目录：`/mnt/sdb/dufei/pg_report_replay_20261104_run001/attempts/`。SQL提取失败、环境缺失和观察不完整不得算作有效未复现。']
    (ROOT/'SQL_ORACLE_PROGRESS.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
