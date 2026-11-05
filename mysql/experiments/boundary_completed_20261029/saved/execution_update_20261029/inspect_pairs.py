"""Offline pair extraction only. Does not execute SQL or contact a server."""
import hashlib,json,pathlib,re,sys
ROOT=pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT.parent/'official_research_20261029'))
from sql_evidence_parser import parse_verbose

def read(p):return json.loads(pathlib.Path(p).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def text(p):return pathlib.Path(p).read_text(encoding='utf-8')
def segments(raw,db):
    out=[]
    try:
        parsed=parse_verbose(raw)
    except ValueError as error:
        # Stored programs contain internal semicolons but mysql echoes their
        # complete CREATE as one command. Keep the entire raw command; never
        # merge result bodies or discard an unparsed output prefix.
        if str(error)!='Verbose SQL block is not one statement':raise
        boundaries=list(re.finditer(r'(?m)^--------------\r?$',raw))
        assert boundaries and len(boundaries)%2==0 and not raw[:boundaries[0].start()].strip()
        parsed=[]
        for n in range(0,len(boundaries),2):
            sql=raw[boundaries[n].end():boundaries[n+1].start()].strip()
            end=boundaries[n+2].start() if n+2<len(boundaries) else len(raw)
            parsed.append({'sql':sql,'normalized':re.sub(r'\s+',' ',sql).strip(),
                'raw_body':raw[boundaries[n+1].end():end]})
    for s in parsed:
        low=s['normalized'].lower()
        if low.startswith('use ') or low in ('set time_zone="+00:00"',"set time_zone='+00:00'") or '__preflight_sql_mode' in low:continue
        body=s['raw_body'].replace(db,'<OWNED_DATABASE>') if db else s['raw_body']
        lines=[v.rstrip('\r') for v in body.splitlines() if v.strip()]
        warnings=[v for v in lines if re.match(r'^(Warning|Note|Error) \(Code \d+\):',v)]
        result=[v for v in lines if v not in warnings and not re.match(r'^(Query OK,|Empty set\b|\d+ rows? in set\b|Bye$)',v)]
        out.append({'sql':s['sql'],'normalized':s['normalized'],'result_lines':result,'warnings':warnings})
    return out

def inspect(batch):
    items=[]
    evidence_root=pathlib.Path(__file__).parent/batch if batch.startswith('progress_') else ROOT/'retrieved'/batch
    for path in sorted(evidence_root.glob('*/results/records.jsonl')):
        for line in text(path).splitlines():
            r=json.loads(line);tid=r['task_id'];d=path.parent;review=read(d.parent/'review.json')
            target_dir=pathlib.Path(review['sql_path']).parent
            tr=read(target_dir/'target_record.json')
            tenvs=list(target_dir.glob('target_environment*.json'));assert len(tenvs)==1
            te=read(tenvs[0]);e=read(d/r['environment_file']) if r.get('environment_file') else {}
            assert not r.get('environment_file') or sha(d/r['environment_file'])==r['environment_manifest_sha256']
            assert r['script_sha256']==review['sql_sha256'] and r['postcheck_sha256']==review['postcheck_sha256']
            a=segments(text(target_dir/'target_stdout.txt'),tr.get('isolated_database'))
            b=segments(text(d/r['stdout_file']),r.get('isolated_database')) if r.get('sql_submitted') else []
            keys=['sql_mode','character_set_server','collation_server','character_set_client','character_set_connection','collation_connection','time_zone','default_storage_engine','transaction_isolation','lower_case_table_names','div_precision_increment','auto_increment_increment','auto_increment_offset']
            envdiff={k:[te.get('variables',{}).get(k),e.get('variables',{}).get(k)] for k in keys if te.get('variables',{}).get(k)!=e.get('variables',{}).get(k)}
            missing=[k for k in keys if te.get('variables',{}).get(k) is None or e.get('variables',{}).get(k) is None]
            switches=lambda x:dict(p.split('=',1) for p in x.get('variables',{}).get('optimizer_switch','').split(',') if '=' in p)
            ta,pa=switches(te),switches(e)
            swdiff={k:[ta.get(k),pa.get(k)] for k in sorted(set(ta)|set(pa)) if ta.get(k)!=pa.get(k)}
            items.append({'task_id':tid,'record_path':str(path),'record':r,'target_record':tr,'review':review,
                'target_environment_path':str(tenvs[0]),'previous_environment_path':str(d/r['environment_file']) if r.get('environment_file') else None,
                'environment_diff':envdiff,'environment_missing_keys':missing,'optimizer_switch_diff':swdiff,
                'target_build':te.get('build_type'),'previous_build':e.get('build_type'),'target_image_architecture':te.get('image_architecture'),'previous_image_architecture':e.get('image_architecture'),
                'target_segments':a,'previous_segments':b,'exact_transcript_equal':a==b,
                'same_statement_sequence':[x['normalized'] for x in a]==[x['normalized'] for x in b],
                'previous_stderr':text(d/r['stderr_file']) if r.get('stderr_file') else None,
                'target_stderr':text(target_dir/'target_stderr.txt'),
                'completion':read(d/'completion.json'),
                'cleanup':read(next(d.glob('cleanup-*.json'))) if list(d.glob('cleanup-*.json')) else None})
    dest=pathlib.Path(__file__).parent/(batch+'_pair_inspection.json')
    with dest.open('x',encoding='utf-8') as f:json.dump(items,f,ensure_ascii=False,indent=2)
    for x in items:
        print(x['task_id'],json.dumps({'status':x['record'].get('execution_status'),'equal':x['exact_transcript_equal'],'same_statements':x['same_statement_sequence'],'env_diff':x['environment_diff'],'missing':x['environment_missing_keys'],'switch_diff':x['optimizer_switch_diff']},ensure_ascii=False))
    return items
if __name__=='__main__':inspect(sys.argv[1])
