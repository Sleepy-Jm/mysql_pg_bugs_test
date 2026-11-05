"""Save official discussion threads without altering the frozen report scope."""
import concurrent.futures as cf
import hashlib
import html
import json
from pathlib import Path
import re
import pg_version_report_census as fetcher

ROOT = Path('experiments/pg_report_replay_20261104/run_001')

def one(row):
    url = row['source_url'].replace('/message-id/', '/message-id/flat/')
    raw, path = fetcher.fetch(url, 'sources')
    bodies = re.findall(r'<div[^>]+class="[^"]*message-content[^"]*"[^>]*>(.*?)</div>', raw, re.S)
    text = '\n\n'.join(f'### MESSAGE {i}\n'+fetcher.clean(body) for i,body in enumerate(bodies))
    (ROOT/'thread_text'/f"{row['report_id']}.txt").write_text(text,encoding='utf-8')
    links = sorted(set(html.unescape(x) for x in re.findall(r'href="([^"]*(?:attachment)[^"]*)"',raw)))
    return {'report_id':row['report_id'], 'url':url, 'snapshot':path,
            'sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(), 'messages':len(bodies), 'attachments':links}

if __name__ == '__main__':
    fetcher.OUT = ROOT/'threads'
    (fetcher.OUT/'sources').mkdir(parents=True,exist_ok=True)
    (ROOT/'thread_text').mkdir(exist_ok=True)
    rows = json.loads((ROOT/'frozen_reports.json').read_text(encoding='utf-8'))
    result=[]
    with cf.ThreadPoolExecutor(max_workers=4) as pool:
        pending = {pool.submit(one,r): r['report_id'] for r in rows}
        for f in cf.as_completed(pending):
            try: result.append(f.result())
            except Exception as exc: result.append({'report_id':pending[f],'error':str(exc)})
    (ROOT/'thread_manifest.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'threads':len(result),'errors':[r for r in result if 'error' in r]}))
