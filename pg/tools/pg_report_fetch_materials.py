"""Download explicitly linked reproducer materials; do not execute them."""
import concurrent.futures as cf
import hashlib
import json
from pathlib import Path
import time
import urllib.request

ROOT=Path('experiments/pg_report_replay_20261104/run_001/materials')
URLS={
 '17292_buggy.tgz':'https://www.postgresql.org/message-id/attachment/128345/buggy.tgz',
 '17335_repro_dump.sql.zst':'https://gist.github.com/funny-falcon/45fa9460507c015390db99a7efd18a75/raw/06a55e57bc6c460ea8800600b1b597c1ed216259/repro_dump.sql.zst',
 '17406_v3_region.psql.gz':'https://www.postgresql.org/message-id/attachment/131162/v3_region.psql.gz',
 '17406_index.datafile.gz':'https://www.postgresql.org/message-id/attachment/131163/region_ltree_path_idx_gist-4221598933.datafile.gz',
 '17445_schema.html':'https://paste.opensuse.org/19058183',
 '17445_works.html':'https://paste.opensuse.org/61559625',
 '17445_fails.html':'https://paste.opensuse.org/44857745',
 '17393_base_recovery.sh':'https://www.postgresql.org/message-id/attachment/132660/base_recovery.sh',
 '18792_related_thread.html':'https://www.postgresql.org/message-id/flat/202411281216.sutbxtr6idnn%40alvherre.pgsql',
}
def one(pair):
 name,url=pair; dest=ROOT/name
 record={'name':name,'url':url}
 for attempt in range(4):
  try:
   if dest.exists():raw=dest.read_bytes()
   else:
    with urllib.request.urlopen(url,timeout=40) as r:
     record['resolved_url']=r.url;raw=r.read(32*1024**2+1)
    if len(raw)>32*1024**2:raise RuntimeError('Material exceeds 32 MiB acquisition bound')
    dest.write_bytes(raw)
   record.update(status='downloaded',bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),path=str(dest));return record
  except Exception as exc:
   record.update(status='source_unavailable',error=str(exc));time.sleep(1)
 return record
if __name__=='__main__':
 ROOT.mkdir(exist_ok=True)
 with cf.ThreadPoolExecutor(max_workers=4) as pool: rows=list(pool.map(one,URLS.items()))
 (ROOT/'manifest.json').write_text(json.dumps(rows,indent=2))
 print(json.dumps(rows))
