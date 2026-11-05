"""Run frozen source scenarios on isolated PostgreSQL clusters (server-side)."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import time
import concurrent.futures
import signal

ROOT=Path('/mnt/sdb/dufei/pg_report_replay_20261104_run001')

def limits():
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    resource.setrlimit(resource.RLIMIT_AS,(3*1024**3,3*1024**3))

def run_case(spec,version,batch):
    dest=ROOT/'attempts'/batch/spec['scenario_id']/version
    dest.mkdir(parents=True,exist_ok=False)
    prefix=ROOT/'builds'/version/'install'
    bindir=prefix/'bin'
    data=dest/'data'
    sock=ROOT/'sock'; sock.mkdir(exist_ok=True,mode=0o700)
    env=dict(os.environ,PGHOST=str(sock),PGPORT='55483',PGUSER='postgres',PGDATABASE='postgres',LC_ALL='C',PGCONNECT_TIMEOUT='5')
    rec={'scenario_id':spec['scenario_id'],'report_id':spec['report_id'],'version':version,
         'target_version':spec['target_version'],'spec_sha256':spec['spec_sha256'],
         'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commands':[],'status':'execution_failed','stage':'initdb'}
    def call(args,label,timeout=60,input=None):
        start=time.monotonic()
        try:
            p=subprocess.run([str(a) for a in args],input=input,capture_output=True,env=env,timeout=timeout,preexec_fn=limits)
            ret={'returncode':p.returncode,'stdout':p.stdout.decode('utf-8','replace'),'stderr':p.stderr.decode('utf-8','replace'),'timed_out':False}
        except subprocess.TimeoutExpired as exc:
            ret={'returncode':None,'stdout':(exc.stdout or b'').decode('utf-8','replace'),'stderr':(exc.stderr or b'').decode('utf-8','replace'),'timed_out':True}
        ret['elapsed_seconds']=time.monotonic()-start
        (dest/(label+'.stdout')).write_text(ret['stdout'])
        (dest/(label+'.stderr')).write_text(ret['stderr'])
        rec['commands'].append({'label':label,'args':[str(a) for a in args],**ret})
        return ret
    started=False
    try:
        actual=subprocess.check_output([str(bindir/'postgres'),'--version'],text=True).strip()
        assert actual=='postgres (PostgreSQL) '+version,actual
        rec['actual_version']=actual
        rec['build_manifest']=json.loads((ROOT/'builds'/version/'manifest.json').read_text())
        p=call([bindir/'initdb','-D',data,'-U','postgres','-A','trust','--no-locale','-E','UTF8','--no-sync'],'initdb')
        if p['returncode']!=0: raise RuntimeError('initdb failed')
        config={'listen_addresses':"''",'unix_socket_directories':"'"+str(sock)+"'",'port':'55483',
                'shared_buffers':"'32MB'",'max_connections':'40','log_statement':"'all'",'log_error_verbosity':"'verbose'",
                'log_line_prefix':"'%m [%p] '",'timezone':"'UTC'",'max_wal_size':"'256MB'"}
        config.update(spec.get('config',{}))
        with (data/'postgresql.conf').open('a') as f:
            f.write('\n'+'\n'.join(k+' = '+v for k,v in config.items())+'\n')
        rec['config']=config
        rec['stage']='startup'
        p=call([bindir/'pg_ctl','-D',data,'-l',dest/'server.log','-w','-t','30','start'],'start',40)
        if p['returncode']!=0: raise RuntimeError('server startup failed')
        started=True
        p=call([bindir/'psql','-X','-A','-t','-c',"SELECT version(), current_setting('server_version_num'), current_setting('debug_assertions');"],'identity')
        if p['returncode']!=0: raise RuntimeError('identity query failed')
        script=['\\set ON_ERROR_STOP on','\\pset null <NULL>']
        for i,part in enumerate(spec['parts']):
            script+=['\\echo __PG_PHASE_'+str(i)+'__']
            if i==len(spec['parts'])-1: script+=['\\set ON_ERROR_STOP off']
            script+=[part['text'],'\\echo __PG_PHASE_DONE_'+str(i)+'__']
        script+='\\echo __PG_SCRIPT_DONE__',
        sql='\n'.join(script)+'\n'
        (dest/'replay.sql').write_text(sql)
        rec['sql_sha256']=hashlib.sha256(sql.encode()).hexdigest()
        rec['stage']='replay'
        mode=spec.get('mode','psql')
        if mode=='psql':
            result=call([bindir/'psql','-X','-A','-t','-f',dest/'replay.sql'],'replay',spec.get('timeout',45))
        elif mode=='concurrent':
            setup=call([bindir/'psql','-X','-v','ON_ERROR_STOP=1','-c',spec['parts'][0]['text']],'setup')
            if setup['returncode']: raise RuntimeError('concurrent setup failed')
            outputs=[]
            for iteration in range(spec.get('iterations',1)):
                jobs=spec.get('workers',[])
                with concurrent.futures.ThreadPoolExecutor(max_workers=len(jobs)) as pool:
                    fs=[pool.submit(call,[bindir/'psql','-X','-A','-t','-c',spec['parts'][j]['text']],f'worker_{iteration}_{n}',spec.get('timeout',60)) for n,j in enumerate(jobs)]
                    outputs.extend(f.result() for f in fs)
                time.sleep(spec.get('iteration_delay',0.2))
                if re.search(r'terminated by signal (?:6|11)',(dest/'server.log').read_text(errors='replace')):break
            result={'stdout':f'__PG_PHASE_{len(spec["parts"])-1}__\n__PG_SCRIPT_DONE__','stderr':'\n'.join(p['stderr'] for p in outputs),'timed_out':any(p['timed_out'] for p in outputs)}
            rec['iterations_completed']=iteration+1
        elif mode=='signal_client':
            q=spec['parts'][0]['text']
            client_env=dict(env,PGAPPNAME='pg_report_17698',PGHOST='127.0.0.1')
            with (dest/'client.stdout').open('wb') as out, (dest/'client.stderr').open('wb') as err:
                client=subprocess.Popen([str(bindir/'psql'),'-X','-c',q],stdout=out,stderr=err,env=client_env,preexec_fn=limits)
                try:
                    for attempt in range(30):
                        probe=call([bindir/'psql','-X','-A','-t','-c',"select count(*) from pg_stat_activity where application_name='pg_report_17698' and state='active' and query like '%pg_sleep%';"],f'before_signal_{attempt}')
                        if probe['stdout'].strip()=='1':break
                        time.sleep(.1)
                    else:raise RuntimeError('query not observed active before signal')
                    client.send_signal(signal.SIGTERM);client.wait(timeout=10);time.sleep(1)
                    probe=call([bindir/'psql','-X','-A','-t','-c',"select count(*) from pg_stat_activity where application_name='pg_report_17698' and state='active' and query like '%pg_sleep%';"],'after_signal')
                    result={'stdout':'__PG_PHASE_0__\n'+probe['stdout']+'\n__PG_SCRIPT_DONE__','stderr':probe['stderr'],'timed_out':probe['timed_out']}
                    rec['client_returncode']=client.returncode
                finally:
                    if client.poll() is None:client.kill();client.wait()
        else:raise ValueError('unsupported mode '+mode)
        # Give the postmaster time to log child exit after a client disconnect.
        time.sleep(spec.get('observation_delay',.2))
        logs=(dest/'server.log').read_text(errors='replace')
        for log in sorted((dest/'data'/'log').glob('*.log')):
            logs+='\n'+log.read_text(errors='replace')
        (dest/'observed_server.log').write_text(logs)
        oracle=spec['oracle']; kind=oracle['kind']
        final=len(spec['parts'])-1
        reached=f'__PG_PHASE_{final}__' in result['stdout']
        trigger_out=result['stdout'].split(f'__PG_PHASE_{final}__',1)[-1]
        trigger_out=re.sub(r'(?m)^__PG_.*__\s*$', '',trigger_out).strip()
        haystack={'crash':logs,'log':logs,'error':result['stderr'],'stderr':result['stderr'],'output':trigger_out}[kind]
        matched=bool(re.search(oracle['pattern'],haystack,re.M))
        completed='__PG_SCRIPT_DONE__' in result['stdout']
        crash=bool(re.search(r'terminated by signal (?:6|11)',logs))
        rec.update(trigger_reached=reached,script_completed=completed,oracle_matched=matched,
                   trigger_output=trigger_out,crash_observed=crash,oracle=oracle)
        if not reached:
            rec.update(status='inconclusive',reason='setup failed before frozen trigger',stage='setup')
        elif result['timed_out']:
            rec.update(status='inconclusive',reason='bounded replay timeout; not an effective non-reproduction')
        elif matched and (kind=='crash' or completed):
            rec.update(status='reproduced',reason='observed report phenomenon matches frozen oracle')
        elif crash:
            rec.update(status='other_anomaly',reason='crash does not match frozen oracle')
        elif completed and (kind=='error' or not re.search(r'ERROR:|FATAL:',result['stderr'])):
            rec.update(status='not_reproduced',reason='complete replay did not match report phenomenon; cause not determined')
        else:
            rec.update(status='inconclusive',reason='unexpected error or incomplete trigger observation')
    except Exception as exc:
        rec.update(status='execution_failed',reason=str(exc))
    finally:
        if started or (data/'postmaster.pid').exists():
            stop=call([bindir/'pg_ctl','-D',data,'-m','immediate','-w','-t','20','stop'],'stop',30)
            rec['cleanup_confirmed']=stop['returncode']==0 or not (data/'postmaster.pid').exists()
        else: rec['cleanup_confirmed']=True
        rec['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
        (dest/'result.json').write_text(json.dumps(rec,indent=2))
    print(spec['scenario_id'],version,rec['status'],flush=True)
    if not rec['cleanup_confirmed']: raise RuntimeError('cluster stop not confirmed')
    return rec

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--batch',required=True);parser.add_argument('--specs',default='prepared_specs.json');args=parser.parse_args()
    assert re.fullmatch('[a-z0-9_]+',args.batch)
    specs=json.loads((ROOT/args.specs).read_text())
    results=[]
    for version in ['14.1','14.2','17.1','17.2','14.0','14.3','17.0','17.3']:
        manifest=ROOT/'builds'/version/'manifest.json'
        deadline=time.monotonic()+7200
        while not manifest.exists():
            if time.monotonic()>deadline: raise RuntimeError('build wait timeout '+version)
            time.sleep(10)
        if json.loads(manifest.read_text())['status']!='built':
            print(version,'BUILD FAILED',flush=True);continue
        for spec in specs:
            major,minor=map(int,spec['target_version'].split('.'))
            matrix=[f'{major}.{n}' for n in (minor-1,minor,minor+1)]
            if version not in matrix:continue
            dest=ROOT/'attempts'/args.batch/spec['scenario_id']/version/'result.json'
            if dest.exists():results.append(json.loads(dest.read_text()));continue
            results.append(run_case(spec,version,args.batch))
            (ROOT/(args.batch+'_results.json')).write_text(json.dumps(results,indent=2))

if __name__=='__main__': main()
