"""Execute the frozen SQLite scripts using each pinned engine in a private in-memory database."""
from pathlib import Path
import base64, ctypes as C, datetime, hashlib, json, sys, time
ROOT=Path(__file__).resolve().parent
P,I,J,S,D=C.c_void_p,C.c_int,C.c_longlong,C.c_char_p,C.c_double
def load(path):
    lib=C.CDLL(str(path))
    for name,(ret,types) in {
        'open':(I,[S,C.POINTER(P)]),'close':(I,[P]),'prepare_v2':(I,[P,P,I,C.POINTER(P),C.POINTER(P)]),
        'step':(I,[P]),'finalize':(I,[P]),'errmsg':(S,[P]),'column_count':(I,[P]),'column_name':(S,[P,I]),
        'column_type':(I,[P,I]),'column_text':(P,[P,I]),'column_blob':(P,[P,I]),'column_bytes':(I,[P,I]),
        'column_double':(D,[P,I]),'column_int64':(J,[P,I]),'sourceid':(S,[]),'libversion':(S,[]),
    }.items():
        fn=getattr(lib,'sqlite3_'+name);fn.argtypes=types;fn.restype=ret
    return lib
def unit(lib,st,col):
    ty=lib.sqlite3_column_type(st,col)
    if ty==1:return ['integer',int(lib.sqlite3_column_int64(st,col))]
    if ty==2:
        x=lib.sqlite3_column_double(st,col);return ['real',x.hex()]
    if ty==5:return ['null',None]
    addr=(lib.sqlite3_column_text if ty==3 else lib.sqlite3_column_blob)(st,col)
    b=C.string_at(addr,lib.sqlite3_column_bytes(st,col))
    if ty==3:
        try:return ['text',b.decode('utf8')]
        except UnicodeDecodeError:return ['text-bytes',b.hex()]
    return ['blob',b.hex()]
def trial(lib,sql):
    db=P(); assert lib.sqlite3_open(b':memory:',C.byref(db))==0
    buf=C.create_string_buffer(sql);base=C.addressof(buf);pos=0;entries=[];failure=None
    try:
        while pos<len(sql):
            st=P();tail=P()
            rc=lib.sqlite3_prepare_v2(db,base+pos,len(sql)-pos,C.byref(st),C.byref(tail))
            new=tail.value-base if tail.value is not None else pos
            if rc:
                failure={'stage':'prepare','code':rc,'message':lib.sqlite3_errmsg(db).decode('utf8','replace'),'offset':pos}
                if st.value:lib.sqlite3_finalize(st)
                break
            if new<=pos:raise ValueError(('no progress',pos))
            start=pos;pos=new
            if not st.value:continue
            n=lib.sqlite3_column_count(st)
            entry={'sql':sql[start:pos].decode('utf8'),'columns':[lib.sqlite3_column_name(st,i).decode('utf8') for i in range(n)],'rows':[]}
            try:
                while True:
                    rc=lib.sqlite3_step(st)
                    if rc==101:break
                    if rc!=100:
                        failure={'stage':'step','code':rc,'message':lib.sqlite3_errmsg(db).decode('utf8','replace'),'offset':start};break
                    entry['rows'].append([unit(lib,st,i) for i in range(n)])
            finally:lib.sqlite3_finalize(st)
            entries.append(entry)
            if failure:break
    finally:lib.sqlite3_close(db)
    return {'error':failure,'statements':entries}
def main():
    case,role=sys.argv[1:3]
    plan=next(x for x in json.loads((ROOT/'plan.json').read_text()) if x['case']==case)
    ref=plan['versions'][role]['git']
    tag='-optin' if plan['versions'][role].get('count_of_view_optin') else ''
    b=ROOT/'builds'/(ref[:12]+tag)
    rcpt=json.loads((b/'built.json').read_text());path=b/'libquery.so'
    assert rcpt['lib_sha256']==hashlib.sha256(path.read_bytes()).hexdigest()
    lib=load(path);sid=lib.sqlite3_sourceid().decode()
    assert rcpt['manifest'][:36] in sid,(ref,sid,rcpt['manifest'])
    bundle={'dbms':'SQLite','case':case,'role':role,'git':ref,'build':rcpt,'source_id':sid,'version':lib.sqlite3_libversion().decode(),'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tests':{}}
    for f in sorted((ROOT/'inputs'/case).glob('T*.sql')):
        sql=f.read_bytes()
        assert hashlib.sha256(sql).hexdigest()==json.loads((ROOT/'input-hashes.json').read_text())[case+'/'+f.name]
        bundle['tests'][f.stem]={'input_sha256':hashlib.sha256(sql).hexdigest(),'trials':[trial(lib,sql) for i in range(3)]}
    assert len(bundle['tests'])==5
    bundle['ended_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    folder=ROOT/'evidence'/case;folder.mkdir(exist_ok=True,parents=True)
    f=folder/(role+'.json');temp=f.with_suffix('.tmp')
    temp.write_text(json.dumps(bundle,ensure_ascii=False,separators=(',',':'))+'\n');temp.replace(f)
if __name__=='__main__':main()
