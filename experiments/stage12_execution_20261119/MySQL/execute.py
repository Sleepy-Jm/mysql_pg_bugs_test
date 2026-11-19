"""Run one build through a private socket in disposable schemas; no shared DB service is used."""
from pathlib import Path
import datetime,hashlib,json,os,re,shutil,subprocess,sys,tempfile,time,xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parent
def stamp():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,x):
    p.parent.mkdir(parents=True,exist_ok=True);tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');os.replace(tmp,p)
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    return h.hexdigest()
def call(args,data=None,timeout=120,check=True):
    cp=subprocess.run(list(map(str,args)),input=data,capture_output=True,timeout=timeout)
    if cp.returncode and check:raise RuntimeError(str(args[0])+' rc '+str(cp.returncode)+': '+cp.stderr[-1800:].decode('utf8','replace'))
    return cp
def parse_output(stdout):
    root=ET.fromstring(b'<all>'+re.sub(rb'<\?xml[^?]*\?>',b'',stdout)+b'</all>')
    return [{'sql':s.get('statement'),'columns':[[c.get('name') for c in row.findall('field')] for row in s.findall('row')][:1],
             'rows':[[None if c.get('{http://www.w3.org/2001/XMLSchema-instance}nil')=='true' else c.text or '' for c in row.findall('field')] for row in s.findall('row')]} for s in root.findall('resultset')]
def main():
    case,role,prefix=sys.argv[1:4];prefix=Path(prefix).resolve()
    ref=next(c for c in json.loads((ROOT/'plan.json').read_text()) if c['case']==case)['versions'][role]
    checks=json.loads((ROOT/'input-hashes.json').read_text())
    assert (prefix/'COMMIT').read_text().strip()==ref,('unexpected build',prefix,ref)
    dest=ROOT/'evidence'/case/role;dest.mkdir(exist_ok=True,parents=True)
    binary=prefix/'bin'/'mysqld';client=prefix/'bin'/'mysql'
    (dest/'build-sha256.txt').write_bytes((prefix/'SHA256SUMS').read_bytes())
    bash={p.name:sha(p) for p in (binary,client)}
    for value in bash.values():assert value in (dest/'build-sha256.txt').read_text()
    version=call([binary,'--no-defaults','--version']).stdout.decode().strip()
    ram=Path(tempfile.mkdtemp(prefix='s12mys-',dir='/tmp'))
    sock=ram/'db.sock';datadir=ram/'data'
    share=next((q for q in (prefix/'share',prefix/'share'/'mysql') if (q/'english'/'errmsg.sys').exists()),prefix/'share')
    srv=[binary,'--no-defaults','--basedir='+str(prefix),'--lc-messages-dir='+str(share),'--datadir='+str(datadir),'--innodb-buffer-pool-size=64M']
    conn=[client,'--no-defaults','--protocol=SOCKET','--socket='+str(sock),'--default-character-set=utf8mb4']
    admin=conn+['-uroot','--batch','--raw','--skip-column-names']
    rec={'case':case,'role':role,'git':ref,'server_version':version,'bin_sha256':bash,'started_utc':stamp(),'tests':{}}
    proc=None
    try:
        init=call(srv+['--initialize-insecure'],timeout=220,check=False)
        if init.returncode:raise RuntimeError('initialize '+init.stderr.decode('utf8','replace')[-2000:])
        with (ram/'server.log').open('wb') as logfile:
            proc=subprocess.Popen(list(map(str,srv+['--socket='+str(sock),'--pid-file='+str(ram/'server.pid'),'--skip-networking','--skip-log-bin','--loose-mysqlx=OFF'])),stdout=logfile,stderr=subprocess.STDOUT)
        for n in range(120):
            if proc.poll() is not None:raise RuntimeError('startup '+(ram/'server.log').read_text(errors='replace')[-2000:])
            if sock.exists() and call(admin+['-e','SELECT 1'],check=False).returncode==0:break
            time.sleep(1)
        else:raise RuntimeError('socket startup timeout')
        diag=call(admin+['-e','SELECT VERSION(), @@version_compile_machine, @@sql_mode, @@optimizer_switch, @@character_set_server, @@collation_server, @@socket']).stdout.decode('utf8','replace').strip()
        rec['session_environment']=diag
        call(admin+['-e',"CREATE USER 's12_reader'@'localhost' IDENTIFIED BY '';"])
        for sql in sorted((ROOT/'inputs'/case).glob('T*.sql')):
            raw=sql.read_bytes();check=hashlib.sha256(raw).hexdigest();assert checks[case+'/'+sql.name]==check
            trials=[]
            for i in range(1,4):
                db='s12_'+sql.stem.lower()+'_r'+str(i)
                call(admin+['-e',"CREATE DATABASE "+db+"; GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, CREATE VIEW, SHOW VIEW ON "+db+".* TO 's12_reader'@'localhost';"])
                try:
                    cp=call(conn+['-us12_reader','--database='+db,'--xml','--batch','--binary-mode','--comments'],raw,90,False)
                    stem=sql.stem+'-'+str(i)
                    (dest/(stem+'.xml')).write_bytes(cp.stdout)
                    (dest/(stem+'.stderr.txt')).write_bytes(cp.stderr)
                    trial={'round':i,'exit':cp.returncode,'stderr':cp.stderr.decode('utf8','replace'),'stdout_sha256':hashlib.sha256(cp.stdout).hexdigest()}
                    try:trial['sets']=parse_output(cp.stdout)
                    except ET.ParseError as err:trial['parse_error']=str(err)
                    trials.append(trial)
                finally:call(admin+['-e','DROP DATABASE '+db],check=False)
            rec['tests'][sql.stem]={'input_sha256':check,'trials':trials}
        assert len(rec['tests'])==5;rec['ended_utc']=stamp()
        save(dest/'results.json',rec)
    finally:
        if proc is not None and proc.poll() is None:
            call(admin+['-e','SHUTDOWN'],timeout=15,check=False)
            try:proc.wait(timeout=40)
            except subprocess.TimeoutExpired:
                proc.terminate();proc.wait(timeout=30)
        if ram.parent==Path('/tmp') and ram.name.startswith('s12mys-'):
            shutil.rmtree(ram)
if __name__=='__main__':main()
