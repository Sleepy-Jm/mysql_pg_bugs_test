"""Run or resume the two-stage DeepSeek generation, without executing SQL."""
from pathlib import Path
import argparse
import concurrent.futures
import datetime
import hashlib
import http.client
import json
import os
import re
import socket
import ssl
import subprocess
import threading
import time
import urllib.error
import urllib.request
import uuid

RUN = Path(__file__).resolve().parent
REPO = RUN.parents[2]
INPUT = REPO / "experiments/stage1_commit_inputs_20261119/model-inputs"
PIN = "52c57a9dc837e78b40cd401ef453521766774948"
ENDPOINT = "https://api.deepseek.com/chat/completions"
DBS = {"MySQL":"MySQL","PG":"PostgreSQL","SQLite":"SQLite"}
HALT = threading.Event()
PRINT = threading.Lock()

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")

def log(s):
    with PRINT:
        print(now(), s, flush=True)

def write(path, data):
    path.parent.mkdir(exist_ok=True, parents=True)
    tmp = path.with_name(path.name+"."+uuid.uuid4().hex+".part")
    tmp.write_bytes(data if isinstance(data,bytes) else data.encode("utf-8"))
    os.replace(tmp,path)

def dump(path, obj):
    write(path,json.dumps(obj,ensure_ascii=False,indent=2)+"\n")

def sha(data):
    return hashlib.sha256(data).hexdigest()

def extract(text):
    # All SQL fences and T headings are checked so no block is silently dropped.
    blocks=list(re.finditer(r"(?ims)^[ \t]*\x60{3,}sql[ \t]*\r?\n(.*?)^[ \t]*\x60{3,}[ \t]*\r?$",text))
    headings=list(re.finditer(r"(?im)^#{1,6}[ \t]+\**T([1-5])\b[^\n]*",text))
    if not 1<=len(blocks)<=5 or len(headings)!=len(blocks):
        return None
    out={}
    for i,(head,block) in enumerate(zip(headings,blocks),1):
        if head[1]!=str(i) or head.start()>block.start() or (i<len(headings) and block.end()>headings[i].start()):return None
        sql=block[1]
        if not sql.strip() or not re.search(r"(?i)\bSELECT\b",sql):return None
        out[f"T{i}.sql"]=sql.encode("utf-8")
    return out

class CallFailure(Exception):
    def __init__(self,message,retry=True,fatal=False):
        super().__init__(message);self.retry=retry;self.fatal=fatal

def stream(payload,key):
    req=urllib.request.Request(ENDPOINT,data=payload,headers={"Content-Type":"application/json","Accept":"text/event-stream","Authorization":"Bearer "+key})
    try:
        res=urllib.request.urlopen(req,timeout=150)
    except urllib.error.HTTPError as e:
        try:
            err=json.loads(e.read(8192))["error"];code=err.get("code");msg=str(err.get("message",""))[:220]
        except Exception:
            code=None;msg=""
        msg=msg.replace(key,"[redacted]")
        raise CallFailure(f"HTTP {e.code} {code or ''} {msg}",e.code in (408,409,429) or e.code>=500,e.code in (401,402,403,404)) from None
    content=[];info={};done=False;finish=None
    with res:
        for line in res:
            if not line.startswith(b"data:"):continue
            data=line[5:].strip()
            if data==b"[DONE]":
                done=True;break
            if not data:continue
            obj=json.loads(data)
            if obj.get("error"):
                raise CallFailure("Provider stream error: "+str(obj["error"].get("code","unknown")))
            for k in ("id","model","created","usage","system_fingerprint"):
                if obj.get(k) is not None:info[k]=obj[k]
            for choice in obj.get("choices") or []:
                if choice.get("index",0)!=0:continue
                delta=choice.get("delta") or {}
                if isinstance(delta.get("content"),str):content.append(delta["content"])
                if choice.get("finish_reason"):finish=choice["finish_reason"]
    info.update({"finish_reason":finish,"stream_done":done})
    return "".join(content),info

def generate_stage(dir,stage,user,key):
    model="deepseek-v4-pro" if stage==1 else "deepseek-flash"
    temp=0.3 if stage==1 else 0.2
    response=dir/f"stage{stage}-output.md";receipt=dir/f"stage{stage}-receipt.json"
    data_sha=sha(user.encode())
    if response.is_file() and receipt.is_file():
        record=json.loads(receipt.read_text("utf-8"));data=response.read_bytes()
        if record.get("input_sha256")==data_sha and record.get("output_sha256")==sha(data) and record["returned"]["model"]==model:
            return data.decode()
        raise CallFailure("Existing final output does not match its receipt",False)
    failures=0; expanded=False
    while failures<3:
        if HALT.is_set():raise CallFailure("Run stopped after provider authentication/account error",False)
        tries=dir/"attempts";tries.mkdir(parents=True,exist_ok=True)
        n=len(list(tries.glob(f"stage{stage}-*.json")))+1
        af=tries/f"stage{stage}-{n:02d}.json"
        limit=(65536 if expanded else 32768) if stage==1 else (16384 if expanded else 8192)
        options={"model":model,"temperature":temp,"max_tokens":limit,"stream":True,"stream_options":{"include_usage":True}}
        if stage==2:options["thinking"]={"type":"disabled"}
        payload=json.dumps({**options,"messages":[{"role":"user","content":user}]},ensure_ascii=False,separators=(",",":")).encode()
        rec={"stage":stage,"attempt":n,"started_utc":now(),"status":"in_flight","options":options,"input_sha256":data_sha,"request_sha256":sha(payload)}
        dump(af,rec); log(f"{dir.parent.name}/{dir.name} stage{stage} attempt {n} started")
        t0=time.monotonic()
        try:
            text,info=stream(payload,key)
            rec.update({"returned":info,"ended_utc":now(),"seconds":round(time.monotonic()-t0,1),"output_sha256":sha(text.encode())})
            if not(info.get("stream_done") and info.get("finish_reason")=="stop"):
                if text:write(af.with_suffix(".partial.md"),text)
                if info.get("finish_reason")=="length":expanded=True
                raise CallFailure("Incomplete response: "+str(info.get("finish_reason")))
            if info.get("model")!=model:
                if text:write(af.with_suffix(".unaccepted.md"),text)
                raise CallFailure("Unexpected returned model: "+str(info.get("model")),False)
            if not text.strip(): raise CallFailure("Empty visible response")
            if stage==2 and not extract(text):
                write(af.with_suffix(".unparsed.md"),text)
                raise CallFailure("Output headings or SQL fences did not satisfy T1-T5 contract")
            write(response,text);rec["status"]="success";dump(af,rec);dump(receipt,rec)
            log(f"{dir.parent.name}/{dir.name} stage{stage} complete ({len(text)} characters)")
            return text
        except (CallFailure,TimeoutError,OSError,http.client.HTTPException,ValueError) as err:
            rec.update({"ended_utc":now(),"seconds":round(time.monotonic()-t0,1),"status":"failed","error":str(err)[:350].replace(key,"[redacted]")})
            dump(af,rec);log(f"{dir.parent.name}/{dir.name} stage{stage}: {rec['error']}")
            if isinstance(err,CallFailure) and err.fatal:HALT.set()
            if isinstance(err,CallFailure) and not err.retry:raise
            failures+=1
            if failures>=3:raise
            time.sleep(2**failures)
    raise AssertionError()

def one(path, template,key):
    db=path.parent.name; name=path.stem
    run=RUN/'cases'/db/name;run.mkdir(parents=True,exist_ok=True)
    original=subprocess.check_output(["git","-c","safe.directory="+REPO.as_posix(),"-C",str(REPO),"show",PIN+":"+path.relative_to(REPO).as_posix()])
    if original!=path.read_bytes():raise RuntimeError("Frozen input changed")
    first=generate_stage(run,1,original.decode("utf-8"),key)
    second_user=template.replace("{{DB}}",DBS[db]).replace("{{STAGE1_OUTPUT}}",first)
    assert first in second_user and "{{STAGE1_OUTPUT}}" not in second_user
    second=generate_stage(run,2,second_user,key)
    blocks=extract(second)
    for name,data in blocks.items():write(run/"sql"/name,data)
    return len(blocks)

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--workers",type=int,default=6)
    parser.add_argument("--key-file",type=Path);args=parser.parse_args()
    key=os.environ.get("DEEPSEEK_API_KEY") or (args.key_file.read_text("utf-8-sig").strip() if args.key_file else "")
    if not key:raise SystemExit("Set DEEPSEEK_API_KEY or supply --key-file")
    template=(RUN/"stage2-template.md").read_bytes().decode()
    paths=sorted(INPUT.glob("*/*.md"))
    assert len(paths)==12 and all(sum(p.parent.name==db for p in paths)==4 for db in DBS)
    # Only frozen model inputs and the shared second-stage instructions are read.
    manifest={"run_id":RUN.name,"frozen_input_commit":PIN,"endpoint":ENDPOINT,"stage2_template_sha256":sha(template.encode()),"requested_models":["deepseek-v4-pro","deepseek-flash"],"workers":args.workers,"case_counts":{},"errors":{},"sql_executed":False}
    old=RUN/"run.json"
    if old.is_file():manifest["started_utc"]=json.loads(old.read_text("utf-8"))["started_utc"]
    else:manifest["started_utc"]=now()
    dump(old,manifest)
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        jobs={pool.submit(one,p,template,key):p for p in paths}
        for j in concurrent.futures.as_completed(jobs):
            p=jobs[j];tag=p.parent.name+"/"+p.stem
            try:manifest["case_counts"][tag]=j.result()
            except Exception as e:manifest["errors"][tag]=str(e)[:350].replace(key,"[redacted]")
            dump(old,manifest)
    manifest["ended_utc"]=now();dump(old,manifest)
    print("Final: ",len(manifest["case_counts"]),"cases,",sum(manifest["case_counts"].values()),"SQL scripts,",len(manifest["errors"]),"errors",flush=True)
    return 1 if manifest["errors"] else 0
if __name__=="__main__":raise SystemExit(main())
