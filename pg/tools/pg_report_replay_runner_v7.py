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
    server_version=spec.get('server_version',version)
    build_root=ROOT/'builds'/server_version
    if spec.get('build_variant'):build_root=ROOT/'special_builds'/(server_version+'_'+spec['build_variant'])
    prefix=build_root/'install'
    bindir=prefix/'bin'
    data=dest/'data'
    sock=ROOT/'sock'; sock.mkdir(exist_ok=True,mode=0o700)
    env=dict(os.environ,PGHOST=str(sock),PGPORT='55483',PGUSER='postgres',PGDATABASE='postgres',LC_ALL='C',PGCONNECT_TIMEOUT='5')
    deps=ROOT/'continuation_deps/unpacked'
    env['LD_LIBRARY_PATH']=str(deps/'usr/lib/x86_64-linux-gnu')+':'+env.get('LD_LIBRARY_PATH','')
    env['VALGRIND_LIB']=str(deps/'usr/lib/x86_64-linux-gnu/valgrind')
    rec={'scenario_id':spec['scenario_id'],'report_id':spec['report_id'],'version':version,
         'target_version':spec['target_version'],'spec_sha256':spec['spec_sha256'],
         'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commands':[],'status':'execution_failed','stage':'initdb'}
    def call(args,label,timeout=60,input=None):
        start=time.monotonic()
        try:
            p=subprocess.run([str(a) for a in args],input=input,capture_output=True,env=env,timeout=timeout,preexec_fn=(None if label=='start' and spec.get('mode')=='valgrind_pgbench' else limits))
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
        assert actual=='postgres (PostgreSQL) '+server_version,actual
        rec['actual_version']=actual
        rec['build_manifest']=json.loads((build_root/'manifest.json').read_text())
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
        start_args=[bindir/'pg_ctl','-D',data,'-l',dest/'server.log','-w','-t','60','start']
        if spec.get('mode')=='valgrind_pgbench':
            wrapper=dest/'valgrind_postgres.sh'
            wrapper.write_text('#!/bin/sh\nexec '+str(deps/'usr/bin/valgrind')+' --tool=memcheck --trace-children=yes --log-file='+str(dest/'valgrind.%p.log')+' '+str(bindir/'postgres')+' "$@"\n')
            wrapper.chmod(0o700)
            start_args += ['-p',wrapper]
        p=call(start_args,'start',75)
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
        if spec.get('setup_dump'):
            packed=ROOT/'materials'/spec['setup_dump']
            dump=dest/'source_dump.sql'
            with dump.open('wb') as f:subprocess.run(['zstd','-dc',str(packed)],stdout=f,check=True)
            rec['dump_sha256']=hashlib.sha256(dump.read_bytes()).hexdigest()
            for role in spec.get('dump_owner_roles',[]):
                assert re.fullmatch('[a-z_][a-z0-9_]*',role)
                assert ('OWNER TO '+role+';') in dump.read_text()
                provision=call([bindir/'createuser','--no-superuser','--no-createdb','--no-createrole',role],'source_owner_'+role)
                if provision['returncode']:raise RuntimeError('cannot provision explicitly named dump owner')
            setup=call([bindir/'psql','-X','-v','ON_ERROR_STOP=1','-f',dump],'restore_dump',180)
            if setup['returncode']:raise RuntimeError('source dump restore failed')
        if mode=='jit_bitcode':
            before={str(p) for p in data.rglob('*.bc')}
            result=call([bindir/'psql','-X','-A','-t','-f',dest/'replay.sql'],'replay',120)
            after={str(p) for p in data.rglob('*.bc')}
            generated=sorted(after-before)
            rec['generated_bitcode_files']=generated
            rec['generated_bitcode_count']=len(generated)
            if result['returncode']==0 and '__PG_SCRIPT_DONE__' in result['stdout']:
                result['stdout']+='\nBITCODE_FILES='+str(len(generated))+'\n'
        elif mode=='valgrind_pgbench':
            setup=call([bindir/'pgbench','-i','-s','1'],'pgbench_init',120)
            if setup['returncode']:raise RuntimeError('source pgbench initialization failed')
            workload=call([bindir/'pgbench','-t','1000','-c','10','-j','10'],'pgbench_workload',900)
            rec['workload_completed']=workload['returncode']==0 and not workload['timed_out']
            result=dict(stdout='__PG_PHASE_0__\n'+workload['stdout']+('\n__PG_SCRIPT_DONE__' if rec['workload_completed'] else ''),stderr=workload['stderr'],timed_out=workload['timed_out'])
        elif mode=='psql':
            result=call([bindir/'psql','-X','-A','-t','-f',dest/'replay.sql'],'replay',spec.get('timeout',45))
        elif mode=='isolation':
            work=ROOT/'builds'/version/'work/src/test/isolation'
            built=call(['make','-j2','-C',work,'all'],'build_isolation',180)
            if built['returncode']:raise RuntimeError('isolationtester build failed')
            result=call([work/'isolationtester','dbname=postgres'],'isolation',90,input=spec['parts'][0]['text'].encode())
            result['stdout']='__PG_PHASE_0__\n'+result['stdout']+'\n__PG_SCRIPT_DONE__'
        elif mode=='python_source':
            setup=call([bindir/'psql','-X','-v','ON_ERROR_STOP=1','-c',spec['parts'][0]['text']],'setup')
            if setup['returncode']:raise RuntimeError('Python scenario setup failed')
            script='import psycopg2\nimport os\ndbconfig=dict(host=os.environ["PGHOST"],port=os.environ["PGPORT"],user="postgres",dbname="postgres")\n'+spec['parts'][1]['text']
            (dest/'source_client.py').write_text(script)
            result=call(['python3',dest/'source_client.py'],'python_client',60)
            result['stdout']='__PG_PHASE_1__\n'+result['stdout']+'\n__PG_SCRIPT_DONE__'
        elif mode=='ordered_sessions':
            import psycopg2
            setup=call([bindir/'psql','-X','-v','ON_ERROR_STOP=1','-c',spec['parts'][0]['text']],'setup')
            if setup['returncode']:raise RuntimeError('ordered session setup failed')
            connections=[psycopg2.connect(host=str(sock),port=55483,user='postgres',dbname='postgres') for _ in range(2)]
            for c in connections:c.autocommit=True
            cursors=[c.cursor() for c in connections];pending=None;out=[]
            try:
                with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
                    for step in spec['schedule']:
                        cur=cursors[step['session']];query=spec['parts'][step['part']]['text']
                        if step.get('async'):
                            pending=pool.submit(cur.execute,query)
                            for n in range(100):
                                p=call([bindir/'psql','-X','-At','-c',f"select wait_event_type from pg_stat_activity where pid={connections[step['session']].get_backend_pid()};"],f'blocked_{n}')
                                if p['stdout'].strip()=='Lock':break
                                time.sleep(.02)
                            else:raise RuntimeError('expected blocking not observed')
                        else:
                            cur.execute(query)
                            if step.get('await_pending'):pending.result(timeout=20)
                            if cur.description:out.extend('|'.join(str(v) for v in row) for row in cur.fetchall())
                result=dict(stdout=f'__PG_PHASE_{len(spec["parts"])-1}__\n'+'\n'.join(sorted(out))+'\n__PG_SCRIPT_DONE__',stderr='',timed_out=False)
            finally:
                for c in connections:c.close()
        elif mode=='pipeline_create':
            before={p.name for p in (data/'base').iterdir() if p.name.isdigit()}
            result=call([bindir/'pgbench','-t','1','-f',dest/'pipeline.sql','-M','extended'],'pipeline',60) if False else None
            (dest/'pipeline.sql').write_text(spec['parts'][0]['text'])
            p=call([bindir/'pgbench','-t','1','-f',dest/'pipeline.sql','-M','extended'],'pipeline',60)
            after={p.name for p in (data/'base').iterdir() if p.name.isdigit()}
            catalog=call([bindir/'psql','-X','-At','-c',"select oid from pg_database order by oid;"],'catalog')
            orphan=sorted((after-before)-set(catalog['stdout'].splitlines()))
            rec.update(before_directories=sorted(before),after_directories=sorted(after),new_orphan_directories=orphan)
            result=dict(stdout='__PG_PHASE_0__\n'+('ORPHAN' if orphan else 'NO_ORPHAN')+'\n__PG_SCRIPT_DONE__',stderr='',timed_out=p['timed_out'])
        elif mode=='concurrent':
            setup=call([bindir/'psql','-X','-v','ON_ERROR_STOP=1','-c',spec['parts'][0]['text']],'setup')
            if setup['returncode']: raise RuntimeError('concurrent setup failed')
            outputs=[]
            worker_files={}
            for j in set(spec.get('workers',[])):
                worker_files[j]=dest/f'worker_source_{j}.sql'
                worker_files[j].write_text(spec['parts'][j]['text']+'\n')
            for iteration in range(spec.get('iterations',1)):
                jobs=spec.get('workers',[])
                with concurrent.futures.ThreadPoolExecutor(max_workers=len(jobs)) as pool:
                    fs=[pool.submit(call,[bindir/'psql','-X','-A','-t','-f',worker_files[j]],f'worker_{iteration}_{n}',spec.get('timeout',60)) for n,j in enumerate(jobs)]
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
        else:
            from pg_report_special_modes_v2 import execute
            result=execute(spec,version,dest,bindir,data,sock,env,rec,call)
        # Give the postmaster time to log child exit after a client disconnect.
        time.sleep(spec.get('observation_delay',.2))
        logs=(dest/'server.log').read_text(errors='replace')
        for log in sorted((dest/'data'/'log').glob('*.log')):
            logs+='\n'+log.read_text(errors='replace')
        (dest/'observed_server.log').write_text(logs)
        for log in sorted(dest.glob('valgrind.*.log')):
            logs+='\n'+log.read_text(errors='replace')
        (dest/'observed_server.log').write_text(logs)
        oracle=spec['oracle']; kind=oracle['kind']
        final=len(spec['parts'])-1
        reached=f'__PG_PHASE_{final}__' in result['stdout']
        trigger_out=result['stdout'].split(f'__PG_PHASE_{final}__',1)[-1]
        trigger_out=re.sub(r'(?m)^__PG_.*__\s*$', '',trigger_out).strip()
        haystack={'crash':logs,'log':logs,'error':result['stderr'],'stderr':result['stderr'],'output':trigger_out}[kind]
        matched=bool(re.search(oracle['pattern'],haystack,re.M))
        for check in spec.get('additional_oracle_checks',[]):
            value={'stdout':result['stdout'],'stderr':result['stderr'],'log':logs}[check['stream']]
            matched=matched and len(re.findall(check['pattern'],value,re.M))==check['count']
        completed='__PG_SCRIPT_DONE__' in result['stdout']
        crash=bool(re.search(r'terminated by signal (?:6|11)',logs))
        rec.update(trigger_reached=reached,script_completed=completed,oracle_matched=matched,
                   trigger_output=trigger_out,crash_observed=crash,oracle=oracle)
        if not reached:
            rec.update(status='inconclusive',reason='setup failed before frozen trigger',stage='setup')
        elif result['timed_out']:
            rec.update(status='inconclusive',reason='bounded replay timeout; not an effective non-reproduction')
        elif matched and (kind=='crash' or completed or mode=='valgrind_pgbench'):
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
    for version in ['17.1','17.2','17.3','14.1','14.2','14.3','14.0','17.0']:
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
            if spec.get('build_variant'):
                special=ROOT/'special_builds'/((spec.get('server_version',version))+'_'+spec['build_variant'])/'manifest.json'
                deadline=time.monotonic()+7200
                while not special.exists():
                    if time.monotonic()>deadline:raise RuntimeError('special build wait timeout '+str(special))
                    time.sleep(5)
                if json.loads(special.read_text())['status']!='built':
                    results.append(dict(report_id=spec['report_id'],scenario_id=spec['scenario_id'],version=version,target_version=spec['target_version'],spec_sha256=spec['spec_sha256'],status='execution_failed',stage='build',reason='required special build failed',build_manifest=str(special)))
                    (ROOT/(args.batch+'_results.json')).write_text(json.dumps(results,indent=2))
                    continue
            dest=ROOT/'attempts'/args.batch/spec['scenario_id']/version/'result.json'
            if dest.exists():results.append(json.loads(dest.read_text()));continue
            results.append(run_case(spec,version,args.batch))
            (ROOT/(args.batch+'_results.json')).write_text(json.dumps(results,indent=2))

if __name__=='__main__': main()
