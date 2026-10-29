"""Export the frozen candidate/SQL catalogue from saved evidence, offline only."""
import argparse
import collections
import csv
import hashlib
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = 'docs/candidate_catalog_20261029'
BASE_COMMIT = 'b74ebe19359a2d0a1e70e359084981076406685e'
CANDIDATES = 'cases/report_version_items.json'
BOUNDARY = 'cases/version_boundary_items.json'
SAVED = 'experiments/saved_20261029'
LABELS = {
    'reproduced': '报告现象已复现', 'execution_failed': '执行失败',
    'other_anomaly': '其他异常', 'inconclusive': '证据不足',
    'not_reproduced': '未复现', 'observed_new_at_release': '前版正常、目标异常',
    'pre_existing': '前版同异常',
}


def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def sort_key(row):
    return tuple(map(int, row['target_version'].split('.'))), int(row['report_id'])


def md(value):
    return str(value).replace('|', '&#124;').replace('\r', '').replace('\n', '<br>')


def repo_link(path, label=None):
    from urllib.parse import quote
    return '[{}](../../{})'.format(label or path, quote(path, safe='/#'))


def main(check=False):
    outputs = {}
    inputs = {}

    def track(path):
        inputs[path] = sha((ROOT / path).read_bytes())

    def emit(path, data):
        outputs[path] = data if isinstance(data, bytes) else data.encode('utf-8')

    def emit_json(path, data):
        emit(path, json.dumps(data, ensure_ascii=False, indent=2) + '\n')

    candidates = sorted(load(CANDIDATES), key=sort_key)
    boundary = {a['task_id']: a for a in load(BOUNDARY)}
    current_path = SAVED + '/final_targeted_20261029/current_results.json'
    current = {a['task_id']: a for a in load(current_path)}
    for path in [CANDIDATES, BOUNDARY, current_path]:
        track(path)
    executed_ids = {a['task_id'] for a in candidates if a['executed']}
    reproduced_ids = {a['task_id'] for a in candidates if a['current_category'] == 'reproduced'}
    new_ids = {tid for tid, a in boundary.items() if a['boundary_status'] == 'observed_new_at_release'}
    assert len(candidates) == len({a['task_id'] for a in candidates}) == 895
    assert (len(executed_ids), len(reproduced_ids), len(new_ids)) == (125, 106, 15)
    assert new_ids <= reproduced_ids <= executed_ids
    assert set(boundary) == reproduced_ids

    # Index actual SQL bytes, never reconstruct SQL from text or normalize newlines.
    sql_index = collections.defaultdict(list)
    for p in sorted((ROOT / 'experiments').rglob('*.sql')):
        sql_index[sha(p.read_bytes())].append(p.relative_to(ROOT).as_posix())

    # Initial-evidence directories repeat earlier records. Preserve references but
    # count an actual run once, using its identity, timestamp and input hash.
    runs = collections.defaultdict(dict)
    for p in sorted((ROOT / SAVED).rglob('records.jsonl')):
        if 'version_boundary_20261029' in p.parts:
            continue
        rel = p.relative_to(ROOT).as_posix()
        for line_no, line in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
            if not line.strip():
                continue
            a = json.loads(line)
            if a.get('task_id') not in executed_ids or a.get('role') != 'target':
                continue
            if a.get('actual_version') != a.get('target_version'):
                continue
            # The legacy runner predates sql_submitted; its completed records
            # are retained explicitly, not mistaken for non-submitted failures.
            if not a.get('sql_submitted', a.get('execution_status') == 'completed'):
                continue
            h = a.get('source_sql_sha256') or a['script_sha256']
            assert sql_index[h], (a['task_id'], h)
            key = (a['run_id'], a.get('started_at_utc'), h)
            row = runs[a['task_id']].setdefault(key, {'record': a, 'record_references': []})
            assert row['record'] == a, (a['task_id'], key, 'conflicting duplicate')
            track(rel)
            row['record_references'].append({'path': rel, 'line': line_no, 'sha256': inputs[rel]})
    assert set(runs) == executed_ids
    assert sum(map(len, runs.values())) == 215

    source_mappings = {}
    for path in ['docs/migration_manifest.json',
                 'experiments/boundary_completed_20261029/source_manifest.json']:
        track(path)
        source_mappings.update({a['source'].replace('\\', '/'): a['destination']
                                for a in load(path)['files'] if a.get('destination')})

    def resolve_original(path):
        key = path.replace('\\', '/').removeprefix('<ORIGINAL_PROJECT>/')
        dest = source_mappings[key]
        track(dest)
        return dest

    def sql_artifact(h, destination):
        source = sql_index[h][0]
        track(source)
        data = (ROOT / source).read_bytes()
        assert sha(data) == h
        emit(destination, data)
        return {'file': destination, 'sha256': h, 'bytes': len(data), 'source': source}

    all_rows = []
    for original in candidates:
        row = dict(original)
        tid = row['task_id']
        row['status_zh'] = LABELS.get(row['current_category'], row['current_category'])
        row['sql_availability'] = 'target_execution_verified' if tid in executed_ids else 'not_exported_unexecuted'
        row['sql_variants'] = []
        assert row['executed'] == current[tid]['executed']
        assert row['current_category'] == current[tid]['current_category']
        if tid in executed_ids:
            rs = sorted(runs[tid].values(), key=lambda a: (
                a['record'].get('started_at_utc', ''), a['record']['run_id']))
            row['target_run_count'] = len(rs)
            row['target_runs'] = rs
            # Display the most recent input; retain every earlier input variant.
            chosen = rs[-1]['record']
            chosen_h = chosen.get('source_sql_sha256') or chosen['script_sha256']
            hashes = sorted({a['record'].get('source_sql_sha256') or a['record']['script_sha256'] for a in rs})
            for h in hashes:
                suffix = '' if h == chosen_h else '-' + h[:12]
                variant = sql_artifact(h, f'sql/executed_125/{tid}{suffix}.sql')
                variant['is_display_default'] = h == chosen_h
                row['sql_variants'].append(variant)
            row['sql_file'] = f'sql/executed_125/{tid}.sql'
            row['sql_sha256'] = chosen_h
            row['display_run_id'] = chosen['run_id']
            if tid in reproduced_ids:
                sql_artifact(chosen_h, f'sql/reproduced_106/{tid}.sql')
            if tid in boundary:
                b = boundary[tid]
                row['boundary'] = {k: v for k, v in b.items() if k not in ('new_records', 'decision')}
                review_path = resolve_original(b['target_review_path'])
                row['boundary']['review_file'] = review_path
                baseline_path = resolve_original(b['baseline_path'])
                row['boundary']['baseline_file'] = baseline_path
                # Check that the actual compared input is the displayed target SQL.
                boundary_source = str(Path(review_path).parent / 'source.sql').replace('\\', '/')
                track(boundary_source)
                assert sha((ROOT / boundary_source).read_bytes()) == chosen_h, tid
                if tid in new_ids:
                    sql_artifact(chosen_h, f'sql/boundary_new_15/{tid}.sql')
                row['boundary']['new_record_references'] = [
                    {'path': resolve_original(a['path']), 'original_sha256': a['sha256'],
                     'run_id': a['record']['run_id'], 'sql_submitted': a['record'].get('sql_submitted', False)}
                    for a in b['new_records']]
        all_rows.append(row)

    groups = [
        ('candidates_895', '895 项候选总表', all_rows, None),
        ('executed_125', '125 项目标版本已执行候选及 SQL', [a for a in all_rows if a['executed']], 'executed_125'),
        ('reproduced_106', '106 项报告现象复现 SQL', [a for a in all_rows if a['task_id'] in reproduced_ids], 'reproduced_106'),
        ('boundary_new_15', '15 项前版正常、目标异常 SQL', [a for a in all_rows if a['task_id'] in new_ids], 'boundary_new_15'),
    ]
    summary = {'source_commit': BASE_COMMIT, 'unit': 'official report × target version',
               'database_executed_by_this_export': False, 'target_run_count': 215,
               'groups': {}, 'per_version': []}
    columns = ['task_id', 'report_id', 'target_version', 'title', 'official_version_field',
               'source_url', 'executed', 'current_category', 'status_zh', 'round_state',
               'remaining_reasons', 'sql_availability', 'sql_file', 'sql_sha256',
               'sql_variant_count', 'target_run_count', 'previous_version', 'boundary_status',
               'boundary_reason', 'evidence_file']
    for name, title, rows, sql_group in groups:
        summary['groups'][name] = {'items': len(rows), 'unique_report_ids': len({a['report_id'] for a in rows})}
        emit_json(name + '.json', rows)
        buf = io.StringIO(newline='')
        writer = csv.DictWriter(buf, fieldnames=columns, lineterminator='\n')
        writer.writeheader()
        lines = [f'# {title}', '', '[返回目录](README.md)', '',
                 '按目标版本、bug 编号排序；每项为报告 × 目标版本。状态来自保存证据，本次没有运行数据库。', '',
                 '| 候选项 | Bug | 目标版本 | 标题 | 目标执行状态 | 相邻版本状态 | SQL |',
                 '|---|---|---|---|---|---|---|']
        for a in rows:
            b = a.get('boundary', {})
            flat = {k: a.get(k, '') for k in columns}
            flat.update(remaining_reasons=' | '.join(a['remaining_reasons']),
                        sql_variant_count=len(a['sql_variants']), previous_version=b.get('previous_version', ''),
                        boundary_status=b.get('boundary_status', ''), boundary_reason=b.get('reason', ''))
            if sql_group:
                flat['sql_file'] = f"sql/{sql_group}/{a['task_id']}.sql"
            writer.writerow(flat)
            sql_path = flat.get('sql_file')
            link = f'[SQL]({sql_path})' if sql_path else '未执行；本次未导出 SQL'
            lines.append('| {} | [{}]({}) | {} | {} | {} | {} | {} |'.format(
                a['task_id'], a['report_id'], a['source_url'], a['target_version'], md(a['title']),
                md(a['status_zh']), LABELS.get(b.get('boundary_status'), '未进入相邻版本集合'), link))
        emit(name + '.csv', '\ufeff' + buf.getvalue())
        lines += ['', '## 逐项内容', '']
        for a in rows:
            lines += [f"### {a['task_id']} · Bug #{a['report_id']}", '', a['title'], '',
                      f"官方版本字段：{a['official_version_field']}", '',
                      f"状态：{a['status_zh']}；阶段：{a['round_state']}", '',
                      '官方报告：[Bug #{}]({})'.format(a['report_id'], a['source_url']), '',
                      '当前结果依据：' + repo_link(a['evidence_file']), '',
                      '保存的结论或待处理原因：', '']
            lines += ['- ' + md(reason) for reason in a['remaining_reasons']]
            lines += ['']
            if a.get('boundary'):
                b = a['boundary']
                lines += [f"相邻比较：{b['previous_version']} → {a['target_version']}，{LABELS[b['boundary_status']]}。", '',
                          '保存的比较依据：' + md(b['reason']), '',
                          '边界审查：' + repo_link(b['review_file']) + '；历史基线：' + repo_link(b['baseline_file']), '']
            if sql_group:
                path = f"sql/{sql_group}/{a['task_id']}.sql"
                lines += [f"目标版本实际执行 {a['target_run_count']} 次；下列默认 SQL 对应 {a['display_run_id']}。", '',
                          f"[下载独立 SQL]({path})；SHA256：`{a['sql_sha256']}`。", '']
                if len(a['sql_variants']) > 1:
                    lines += ['本项曾执行多个输入版本，全部保留：', '']
                    lines += [f"- [{v['sha256']}]({v['file']})" for v in a['sql_variants']]
                    lines += ['']
                # Markdown uses LF for Git portability. The .sql download above
                # remains the authoritative byte-for-byte input, including CRLF.
                sql = outputs[path].decode('utf-8').replace('\r\n', '\n')
                fence = '`' * max(3, max((len(s) for s in re.findall(r'`+', sql)), default=0) + 1)
                lines += [fence + 'sql', sql.rstrip('\n'), fence, '']
                lines += ['目标执行记录（完整字段和所有重复证据位置见同名 JSON）：', '']
                for run in a['target_runs']:
                    rec = run['record']
                    ref = run['record_references'][0]
                    lines += ['- `{}`，实际版本 {}，{}；{}'.format(
                        rec['run_id'], rec['actual_version'], rec['execution_status'],
                        repo_link(ref['path'] + '#L' + str(ref['line']), 'records.jsonl:' + str(ref['line'])))]
                lines += ['']
            else:
                lines += [('SQL：' + f"[查看已执行 SQL]({a['sql_file']})") if a['executed'] else
                          '本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。', '']
        emit(name + '.md', '\n'.join(lines))

    for version in sorted({a['target_version'] for a in all_rows}):
        rows = [a for a in all_rows if a['target_version'] == version]
        summary['per_version'].append({'version': version, 'candidates': len(rows),
                                      'executed': sum(a['executed'] for a in rows),
                                      'reproduced': sum(a['task_id'] in reproduced_ids for a in rows),
                                      'previous_normal_target_abnormal': sum(a['task_id'] in new_ids for a in rows)})
    summary['executed_categories'] = dict(sorted(collections.Counter(
        a['current_category'] for a in all_rows if a['executed']).items()))
    emit_json('summary.json', summary)
    intro = ['# 候选项与 SQL 内容目录（2026-10-29）', '',
             '从仓库已有证据离线整理，源基线提交 `' + BASE_COMMIT + '`。', '',
             '| 资料 | 项数 | 不同 bug 编号数 | 格式 |', '|---|---:|---:|---|']
    for name, title, rows, group in groups:
        intro.append(f"| [{title}]({name}.md) | {len(rows)} | {len({a['report_id'] for a in rows})} | [CSV]({name}.csv) · [JSON]({name}.json) |")
    intro += ['', '| 目标版本 | 候选 | 已执行 | 现象复现 | 前版正常、目标异常 |', '|---|---:|---:|---:|---:|']
    for a in summary['per_version']:
        intro.append('| {version} | {candidates} | {executed} | {reproduced} | {previous_normal_target_abnormal} |'.format(**a))
    intro += ['', '## 阅读与口径', '',
              '- 候选内容包含标题、官方 Version 字段、报告链接、当前状态、阶段、结论或待处理原因；895 项中 770 项未执行，保留缺正文、失败和未知。本次不抓取或补写缺失的官方报告全文。',
              '- 125 项包含 215 次目标执行；当前类别为 106 项 reproduced、12 项 execution_failed、4 项 other_anomaly、2 项 inconclusive、1 项 not_reproduced。已执行不等于已复现。',
              '- 106 项指报告现象复现，涉及 99 个 bug 编号；15 项表示保存的严格相邻版本观察，涉及 15 个 bug 编号，并非确认了 15 个新漏洞或独立根因，也未定位引入提交。',
              '- 独立 SQL 分别在 [已执行](sql/executed_125)、[复现](sql/reproduced_106)、[前版正常、目标异常](sql/boundary_new_15) 目录；后三组 Markdown 均内嵌完整默认 SQL 内容。每个文件按 task_id 命名。',
              '- 独立 SQL 是保存的输入脚本，逐字节复制，不添加头注释或拼接成可批量执行脚本；Markdown 内嵌展示统一使用 LF 换行，精确字节以独立 SQL 为准。runner 的 USE/会话前导和 postcheck 并不全部包含于 source SQL，具体以 JSON 中的原始执行记录及原始 manifest/oracle 为准。',
              '- 同一候选有多个已执行输入时，默认展示按开始时间排序的最后一个，所有变体和全部记录均保留。Bug 119646 / 8.0.33 有两个输入，已执行目录因此有 126 个 SQL 文件；复现和边界目录各为 106、15 个。',
              '- 相邻版本所用 source.sql 已与展示的目标 SQL 逐项核对哈希。跨目录同一 task_id 的默认 SQL 完全相同；不对不同版本的同 bug 去重或合并。',
              '- CSV 使用 UTF-8 BOM；所有 CSV SQL 路径相对于本目录，JSON 同样如此。JSON 内 source、evidence_file、record_references 和 boundary 的证据路径相对于仓库根目录。原始哈希和导出文件哈希分别保留。',
              '- [输入及导出 SQL 哈希](provenance.json) 和 [汇总](summary.json) 用于核查；历史材料中的代码提交未知时仍为 unknown，不以本次整理提交冒充历史实验代码。', '',
              '## 更新与检查', '', '在仓库根目录执行（离线，不运行数据库）：', '', '```powershell',
              'python -X utf8 -B scripts/build_candidate_catalog.py',
              'python -X utf8 -B scripts/build_candidate_catalog.py --check',
              'python -X utf8 -B scripts/check_offline.py',
              'python -X utf8 -B scripts/audit_repository.py',
              'python -X utf8 -B scripts/audit_latest_boundary.py', '```', '']
    emit('README.md', '\n'.join(intro))
    emit_json('provenance.json', {'source_commit': BASE_COMMIT, 'inputs': inputs,
                                'sql_outputs': {k: sha(v) for k, v in sorted(outputs.items()) if k.endswith('.sql')}})

    target = ROOT / OUT
    if check:
        actual = {p.relative_to(target).as_posix() for p in target.rglob('*') if p.is_file()}
        assert actual == set(outputs), ('unexpected/missing catalogue files', actual ^ set(outputs))
        for path, data in outputs.items():
            assert (target / path).read_bytes() == data, ('stale or modified catalogue', path)
        print('PASS: catalogue exact regeneration; 895/125/106/15; 215 target runs; all SQL byte hashes verified')
    else:
        for path, data in outputs.items():
            p = target / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
        print(f'Wrote {len(outputs)} files to {OUT}; no database/network access')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='verify exact regeneration without writing')
    main(parser.parse_args().check)
