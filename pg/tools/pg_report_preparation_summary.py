"""Summarize frozen PG preparation separately from actual replay attempts."""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path('experiments/pg_report_replay_20261104/run_001')


def main():
    read = lambda name: json.loads((ROOT / name).read_text(encoding='utf-8'))
    specs = read('prepared_specs.json') + read('prepared_specs_batch002.json')
    assert len({s['scenario_id'] for s in specs}) == len(specs)
    rows = read('preparation_inventory.json')
    reports = {r['report_id']: r for r in read('frozen_reports.json')}
    for row in rows:
        ss = [s for s in specs if s['report_id'] == row['report_id'] and s['target_version'] == row['target_version']]
        row['original_version_field'] = reports[row['report_id']]['version_field']
        row.update(preparation_status='ready' if ss else 'review_required',
                   source_sql_prepared=bool(ss), oracle_frozen=bool(ss),
                   scenario_count=len(ss), sql_phase_count=sum(len(s['parts']) for s in ss))
        for key, source in [('oracle_kinds', 'kind'), ('reported_phenomenon', 'reported_phenomenon'),
                            ('author_expected_behavior', 'author_expected_behavior'), ('oracle_patterns', 'pattern')]:
            row[key] = '\n'.join(s['oracle'][source] for s in ss)
        row['spec_paths'] = '\n'.join(str(ROOT / 'prepared' / s['scenario_id'] / 'spec.json') for s in ss)
        if ss:
            row['pending_note'] = ''
        if row['report_id'] == '17428':
            row['preparation_status'] = 'correction_required'
            row['pending_note'] = '原文行尾注释发生展示换行，提取脚本残留裸数字，导致后续 INSERT 语法错误；须保留原尝试，记录来源变换修订后重放。oracle 不变。'
    summary = []
    for version in ['14.1', '14.2', '17.1', '17.2']:
        rr = [r for r in rows if r['target_version'] == version]
        summary.append(dict(version=version, report_version_items=len(rr),
                            sql_and_oracle_prepared=sum(r['source_sql_prepared'] and r['oracle_frozen'] for r in rr),
                            ready=sum(r['preparation_status'] == 'ready' for r in rr),
                            correction_required=sum(r['preparation_status'] == 'correction_required' for r in rr),
                            review_required=sum(r['preparation_status'] == 'review_required' for r in rr),
                            sql_phase_count=sum(r['sql_phase_count'] for r in rr),
                            frozen_oracle_count=sum(r['scenario_count'] for r in rr)))
    attempts = [x for batch in read('execution_snapshot.json').values() for x in batch]
    execution = dict(attempts=len(attempts), target_attempts=sum(x['version'] == x['target_version'] for x in attempts),
                     adjacent_attempts=sum(x['version'] != x['target_version'] for x in attempts),
                     all_statuses=dict(Counter(x['status'] for x in attempts)),
                     target_statuses=dict(Counter(x['status'] for x in attempts if x['version'] == x['target_version'])))
    for name, value in [('preparation_inventory.json', rows), ('preparation_summary.json', summary), ('execution_summary.json', execution)]:
        (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    with (ROOT / 'preparation_inventory.csv').open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
    lines = ['# PostgreSQL SQL/oracle 准备进度', '', '执行中的快照；尚未完成全部 136 项来源核对。', '',
             '|版本|入选项|已整理 SQL+oracle|其中待修订|待来源核对|SQL 片段|冻结 oracle|',
             '|---|---:|---:|---:|---:|---:|---:|']
    for s in summary:
        lines.append('|{version}|{report_version_items}|{sql_and_oracle_prepared}|{correction_required}|{review_required}|{sql_phase_count}|{frozen_oracle_count}|'.format(**s))
    lines += ['', 'SQL 片段按执行阶段计，不是 SQL 语句数或独立 bug 数。oracle 按场景计。待来源核对不等于缺 SQL 或 oracle。', '',
              '17428 的展示换行污染了 SQL，已标记待修订；原始尝试保留为无法判断，不计有效未复现。', '',
              '实际执行统计：', '', '```json', json.dumps(execution, ensure_ascii=False, indent=2), '```', '',
              '逐项来源、报告现象、作者预期、判据和证据路径见 preparation_inventory.csv 及 prepared/*/spec.json。复现报告现象不等于确认独立缺陷。']
    (ROOT / 'SQL_ORACLE_PROGRESS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps(dict(preparation=summary, execution=execution), indent=2))


if __name__ == '__main__':
    main()
