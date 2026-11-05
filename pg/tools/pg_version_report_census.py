"""Archive census of numbered PostgreSQL form reports; no database execution."""
import concurrent.futures as cf
import argparse
import csv
import hashlib
import html
import http.client
import json
from pathlib import Path
import re
import time
import threading
import urllib.parse
import urllib.request

BASE = 'https://www.postgresql.org'
OUT = Path('experiments/pg_version_report_census_20261104/run_001')
VERSIONS = ('14.1', '14.2', '17.1', '17.2')
OFFLINE = False
CONNECTIONS = threading.local()

def save(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

def fetch(url, kind):
    path = OUT / kind / (hashlib.sha256(url.encode()).hexdigest() + '.html')
    if path.exists():
        return path.read_text(encoding='utf-8'), str(path)
    if OFFLINE:
        raise FileNotFoundError(f'No cached official source: {url}')
    for attempt in range(5):
        try:
            if kind == 'sources':
                conn = getattr(CONNECTIONS, 'conn', None)
                if conn is None:
                    conn = http.client.HTTPSConnection('www.postgresql.org', timeout=25)
                    CONNECTIONS.conn = conn
                conn.request('GET', urllib.parse.urlsplit(url).path,
                             headers={'User-Agent': 'PostgreSQL-report-version-audit/1.0'})
                response = conn.getresponse()
                raw = response.read()
                if response.status != 200:
                    raise RuntimeError(f'HTTP {response.status}: {url}')
            else:
                req = urllib.request.Request(url, headers={'User-Agent': 'PostgreSQL-report-version-audit/1.0'})
                with urllib.request.urlopen(req, timeout=45) as response:
                    raw = response.read()
            text = raw.decode('utf-8')
            path.write_bytes(raw)
            return text, str(path)
        except Exception:
            conn = getattr(CONNECTIONS, 'conn', None)
            if conn:
                conn.close()
                CONNECTIONS.conn = None
            if attempt == 4:
                raise
            time.sleep(1 + attempt)

def clean(s):
    s = re.sub(r'<br\s*/?>|</p>', '\n', s, flags=re.I)
    return html.unescape(re.sub('<[^>]+>', '', s))

def month_scan(month):
    url = f'{BASE}/list/pgsql-bugs/{month}/'
    pages, reports, seen = [], {}, set()
    while url not in seen:
        seen.add(url)
        raw, path = fetch(url, 'indexes')
        pages.append({'url': url, 'snapshot': path, 'sha256': hashlib.sha256(Path(path).read_bytes()).hexdigest()})
        for href, title in re.findall(r'<a\s+href="(/message-id/[^"#]+)"[^>]*>(.*?)</a>', raw, re.S):
            title = clean(title).strip()
            match = re.match(r'BUG #(\d+):', title)
            if match:
                reports[BASE + html.unescape(href)] = {'report_id': match[1], 'title': title}
        nxt = re.search(r'<a href="([^"]+)"[^>]*>Next</a>', raw)
        if not nxt:
            break
        next_path = html.unescape(nxt[1])
        stamp = re.search(r'/since/(\d{6})', next_path)
        if not stamp or stamp[1] > month.replace('-', ''):
            break
        url = BASE + next_path
    return {'month': month, 'pages': pages, 'reports': reports}

def report_scan(pair):
    url, info = pair
    raw, path = fetch(url, 'sources')
    # Restrict to message body, before response/whole-thread navigation.
    body_match = re.search(r'<div[^>]+class="[^"]*message-content[^"]*"[^>]*>(.*?)</div>', raw, re.S)
    body = clean(body_match[1]) if body_match else ''
    header = body.split('Description:', 1)[0]
    field = re.search(r'^PostgreSQL version:[ \t]*([^\r\n]+)', header, re.M)
    ref = re.search(r'^Bug reference:[ \t]*(\d+)', header, re.M)
    date = re.search(r'<meta property="article:published_time" content="([^"]+)"', raw)
    author = re.search(r'<meta property="article:author" content="([^"]+)"', raw)
    is_form = bool(author and html.unescape(author[1]) == 'PG Bug reporting form')
    version = field[1].strip() if field else None
    tokens = re.findall(r'(?<![\d.])(\d+\.\d+)(?![\d.])', version or '')
    targets = [v for v in VERSIONS if v in tokens]
    return dict(info, source_url=url, version_field=version, target_versions=targets,
                report_date=date[1] if date else None,
                is_original_form_report=is_form,
                archive_author=html.unescape(author[1]) if author else None,
                reference_verified=bool(ref and ref[1] == info['report_id']),
                snapshot=path, sha256=hashlib.sha256(Path(path).read_bytes()).hexdigest(),
                version_source_excerpt=field[0] if field else None)

def main():
    global OUT, OFFLINE
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=OUT)
    parser.add_argument('--offline', action='store_true', help='Recalculate only from saved HTML snapshots')
    args = parser.parse_args()
    OUT, OFFLINE = args.output, args.offline
    OUT.mkdir(parents=True, exist_ok=True)
    for d in ('indexes', 'sources'):
        (OUT / d).mkdir(exist_ok=True)
    months = [f'{y}-{m:02}' for y in range(2021, 2027) for m in range(1, 13)
              if '2021-11' <= f'{y}-{m:02}' <= '2026-11']
    indexes, errors, candidates = [], [], {}
    with cf.ThreadPoolExecutor(max_workers=6) as pool:
        tasks = {pool.submit(month_scan, month): month for month in months}
        for future in cf.as_completed(tasks):
            month = tasks[future]
            try:
                result = future.result()
                indexes.append(result)
                candidates.update(result['reports'])
                print('INDEX', month, len(result['pages']), len(result['reports']), flush=True)
            except Exception as exc:
                errors.append({'stage': 'index', 'month': month, 'error': str(exc)})
    save('archive_inventory.json', indexes)
    save('candidates.json', candidates)
    records = []
    with cf.ThreadPoolExecutor(max_workers=6) as pool:
        tasks = {pool.submit(report_scan, pair): pair[0] for pair in candidates.items()}
        for future in cf.as_completed(tasks):
            try:
                records.append(future.result())
            except Exception as exc:
                errors.append({'stage': 'report', 'url': tasks[future], 'error': str(exc)})
            if (len(records) + len(errors)) % 100 == 0:
                print('REPORTS', len(records), '/', len(candidates), 'errors', len(errors), flush=True)
    records.sort(key=lambda r: (int(r['report_id']), r['source_url']))
    save('scope_audit.json', records)
    save('fetch_errors.json', errors)
    selected = {}
    for r in records:
        if r['is_original_form_report'] and r['target_versions'] and r['reference_verified'] and r['report_date'] and r['report_date'][:10] <= '2026-11-04':
            if r['report_id'] in selected:
                assert selected[r['report_id']]['version_field'] == r['version_field']
            selected[r['report_id']] = r
    reports = list(selected.values())
    items = [dict(r, item_id=f"pg-{r['report_id']}-{v}", target_version=v, execution_status='not_run')
             for r in reports for v in r['target_versions']]
    save('selected_reports.json', reports)
    save('scope_items.json', items)
    summary = {'versions': {v: sum(v in r['target_versions'] for r in reports) for v in VERSIONS},
               'report_count': len(reports), 'version_item_count': len(items),
               'candidate_urls': len(candidates), 'checked_urls': len(records),
               'months': len(indexes), 'errors': len(errors),
               'missing_fields': sum(r['is_original_form_report'] and (r['version_field'] is None or not r['reference_verified'] or not r['report_date']) for r in records),
               'original_form_reports_checked': sum(r['is_original_form_report'] for r in records),
               'non_form_messages_excluded': sum(not r['is_original_form_report'] for r in records),
               'scope': 'Numbered original BUG form reports in pgsql-bugs, archive months 2021-11 through 2026-11, fetched 2026-11-04; exact version tokens only; not confirmed independent bugs.'}
    summary['version_groups'] = {label: {'reports': sum(any(v in r['target_versions'] for v in versions) for r in reports),
                                         'version_items': sum(sum(v in r['target_versions'] for v in versions) for r in reports)}
                                 for label, versions in [('14.1-14.2', ('14.1', '14.2')), ('17.1-17.2', ('17.1', '17.2'))]}
    summary['archive_page_count'] = sum(len(i['pages']) for i in indexes)
    save('summary.json', summary)
    with (OUT / 'report_version_items.csv').open('w', encoding='utf-8-sig', newline='') as f:
        fields = ['item_id', 'report_id', 'title', 'report_date', 'version_field', 'target_version', 'source_url', 'snapshot', 'sha256', 'execution_status']
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(items)
    lines = ['# PostgreSQL 官方报告版本字段统计', '', '核对日期：2026-11-04。', '',
             '## 筛选口径', '',
             '- 沿用当前 MySQL 流程：只读取报告首帖的 `PostgreSQL version:` 原字段，匹配完整版本号；不凭标题、正文、回复、修复版本或发布日期推断。',
             '- 官方来源为 pgsql-bugs 中带 BUG 编号的表单报告。普通未编号讨论不属于此冻结集合；回复不重复计数。同一根因的不同报告仍按报告分别计数。',
             '- 遍历 2021-11 至 2026-11 的月归档及分页，覆盖 14.1 发布所在月份至核对日；仅纳入报告日期不晚于 2026-11-04 的匹配报告。',
             '- 不展开版本范围或省略写法；不将 14.10/14.20/17.10/17.20 当作目标版本。',
             '- 这是版本字段符合条件的报告统计，不是已确认独立 bug 数。未开展 SQL/oracle 整理、根因去重或数据库重放，所有入选项均为 `not_run`。', '',
             '## 统计', '', '| 目标版本 | 报告数 | 报告 × 版本项数 |', '|---|---:|---:|']
    for v, count in summary['versions'].items():
        lines.append(f'| {v} | {count} | {count} |')
    for group, counts in summary['version_groups'].items():
        lines.append(f"| {group} 合计 | {counts['reports']} | {counts['version_items']} |")
    lines += [f"| 全部（报告去重） | {len(reports)} | {len(items)} |", '',
              f"归档覆盖：{len(indexes)}/61 个月，{summary['archive_page_count']} 个页面；发现 {len(candidates)} 个候选首帖 URL，核对 {len(records)} 个；获取错误 {len(errors)} 个，字段/编号待核对 {summary['missing_fields']} 个。", '',
              f"候选中经发件身份确认的表单原始报告 {summary['original_form_reports_checked']} 个；排除沿用 BUG 标题的非表单邮件 {summary['non_form_messages_excluded']} 个。", '',
              '存在获取错误或字段待核对项时，统计仅为已核实下界，不应称为完整总数。归档公开可见范围之外、删除或未编号的邮件不在此集合中。', '',
              '## 证据文件', '',
              '- `report_version_items.csv`：逐报告 × 目标版本表，含原字段、官方链接、快照、SHA-256、执行状态。',
              '- `selected_reports.json` / `scope_items.json`：入选报告和版本项。',
              '- `scope_audit.json`：所有已读取候选的原字段与匹配结果，包含未入选项。',
              '- `archive_inventory.json` / `candidates.json`：目录分页证据与候选 URL；`fetch_errors.json`：获取缺口。',
              '- `indexes/` / `sources/`：原 HTML 字节快照；`summary.json`：机器可读汇总。', '',
              '## 入选报告', '', '| 编号 | 日期 | Version 原字段 | 标题（官方来源） |', '|---|---|---|---|']
    for r in reports:
        title = r['title'].replace('|', '\\|').replace('\n', ' ')
        field = r['version_field'].replace('|', '\\|')
        lines.append(f"| {r['report_id']} | {(r['report_date'] or '')[:10]} | {field} | [{title}]({r['source_url']}) |")
    (OUT / 'README.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False), flush=True)

if __name__ == '__main__':
    main()
