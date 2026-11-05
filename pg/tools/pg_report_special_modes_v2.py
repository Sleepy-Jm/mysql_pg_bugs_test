"""Explicit adapters for source-described operational/client scenarios."""
import concurrent.futures
import datetime
import json
import os
from pathlib import Path
import re
import shutil
import socket
import subprocess
import time

ROOT=Path('/mnt/sdb/dufei/pg_report_replay_20261104_run001')


def execute(spec,version,dest,bindir,data,sock,env,rec,call):
    mode=spec['mode'];last=len(spec['parts'])-1
    def finish(out,err='',timed_out=False):
        return dict(stdout=f'__PG_PHASE_{last}__\n'+out+'\n__PG_SCRIPT_DONE__',stderr=err,timed_out=timed_out)
    def sql(query,label,timeout=60):return call([bindir/'psql','-X','-At','-c',query],label,timeout)
    if mode=='ubsan_client':
        root=ROOT/'special_builds'/(version+'_ubsan_client')
        rec['client_build_manifest']=json.loads((root/'manifest.json').read_text())
        client=root/'work/src/bin/psql/psql'
        result=call([client,'-X','-c',spec['parts'][0]['text']],'ubsan_psql')
        return finish(result['stdout'],result['stderr'],result['timed_out'])
    if mode=='listen_probe':
        observations={}
        for host in ['127.0.0.1','::1']:
            try:
                with socket.create_connection((host,55483),timeout=3):observations[host]='connected'
            except OSError as e:observations[host]=str(e)
        rec['localhost_resolution']=socket.getaddrinfo('localhost',55483);rec['listener_probe']=observations
        return finish('IPV4_ONLY' if observations['127.0.0.1']=='connected' and observations['::1']!='connected' else 'BOTH' if all(v=='connected' for v in observations.values()) else 'OTHER')
    if mode=='window_compare':
        setup=sql(spec['parts'][0]['text'],'setup')
        if setup['returncode']:raise RuntimeError('window setup failed')
        a=sql(spec['parts'][1]['text'],'baseline');b=sql(spec['parts'][2]['text'],'filtered')
        aa=[l for l in a['stdout'].splitlines() if l.endswith('|3|1')];bb=b['stdout'].strip().splitlines()
        rec['baseline_selected']=aa;rec['filtered_selected']=bb
        if a['returncode'] or b['returncode'] or len(aa)!=1 or len(bb)!=1:raise RuntimeError('window observations incomplete')
        return finish('ROW_CHANGED' if aa!=bb else 'SAME_ROW')
    if mode=='hostname_reload':
        import psycopg2
        conn=psycopg2.connect(host='127.0.0.1',port=55483,user='postgres',dbname='postgres',application_name='report17538')
        pid=conn.get_backend_pid();rec['observed_backend_pid']=pid
        with (data/'postgresql.conf').open('a') as f:f.write('\nlog_hostname = on\n')
        reload=call([bindir/'pg_ctl','-D',data,'reload'],'reload')
        if reload['returncode']:raise RuntimeError('reload failed')
        time.sleep(1);conn.close();time.sleep(.2)
        logs=(dest/'server.log').read_text(errors='replace')
        lines=[l for l in logs.splitlines() if f'[{pid}]' in l and 'disconnection:' in l]
        if not lines:raise RuntimeError('missing matching disconnection log')
        return finish('\n'.join(lines))
    if mode=='config_reload':
        value=spec['reload_slot_value'];assert re.fullmatch('[a-z_]+',value)
        with (data/'postgresql.conf').open('a') as f:f.write("\nsynchronized_standby_slots='"+value+"'\n")
        result=call([bindir/'pg_ctl','-D',data,'reload'],'reload')
        if result['returncode']:raise RuntimeError('configuration reload failed')
        time.sleep(3)
        return finish('RELOAD_SENT')
    if mode=='dump_restore':
        setup=sql(spec['parts'][0]['text'],'setup')
        if setup['returncode']:raise RuntimeError('dump source setup failed')
        client=ROOT/'builds'/version/'install/bin/pg_dump'
        rec['client_version']=subprocess.check_output([str(client),'--version'],text=True).strip()
        dump=call([client,'postgres'],'dump');(dest/'dump.sql').write_text(dump['stdout'])
        if dump['returncode']:raise RuntimeError('pg_dump failed')
        create=call([bindir/'createdb','my_restore_db'],'create_restore_db')
        if create['returncode']:raise RuntimeError('create restore database failed')
        restored=call([bindir/'psql','-X','-d','my_restore_db','-f',dest/'dump.sql'],'restore')
        return finish(restored['stdout'],restored['stderr'],restored['timed_out'])
    if mode=='serial_suite':
        work=ROOT/'special_builds'/(version+'_serial')/'work/src/test/isolation'
        schedule=dest/'isolation_schedule';schedule.write_text('test: two-ids\n'*100)
        def worker(n):
            out=dest/f'results_{n}';out.mkdir()
            return call(['make','-C',work,'installcheck',f'EXTRA_REGRESS_OPTS=--dbname=regress_{n} --outputdir={out} --schedule={schedule}'],f'installcheck_{n}',600)
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(worker,[1,2]))
        rec['suite_returncodes']=[x['returncode'] for x in results]
        return finish('\n'.join(x['stdout'] for x in results),'\n'.join(x['stderr'] for x in results),any(x['timed_out'] for x in results))
    if mode=='pitr':
        archive=dest/'archive';archive.mkdir();backup=dest/'backup'
        with (data/'postgresql.conf').open('a') as f:
            f.write(f"\narchive_mode=on\narchive_command='test ! -f {archive}/%f && cp %p {archive}/%f'\nrestore_command='cp {archive}/%f %p'\n")
        p=call([bindir/'pg_ctl','-D',data,'-m','fast','-w','restart','-l',dest/'server.log'],'archive_restart',60)
        if p['returncode']:raise RuntimeError('archive restart failed')
        p=sql('CREATE DATABASE test','create_test')
        if p['returncode']:raise RuntimeError('create database failed')
        oid=sql("SELECT oid FROM pg_database WHERE datname='test'",'test_oid')['stdout'].strip()
        p=call([bindir/'pg_basebackup','-D',backup],'basebackup',180)
        if p['returncode']:raise RuntimeError('basebackup failed')
        time.sleep(5);target=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');time.sleep(5)
        sql('DROP DATABASE test','drop_test');sql('SELECT pg_switch_wal()','switch_wal');time.sleep(5)
        rec['recovery_target_time']=target;rec['test_oid']=oid
        p=call([bindir/'pg_ctl','-D',data,'-m','fast','-w','stop'],'stop_before_restore',60)
        if p['returncode']:raise RuntimeError('stop before restore failed')
        data.rename(dest/'original_data');shutil.copytree(backup,data)
        (data/'recovery.signal').touch()
        with (data/'postgresql.conf').open('a') as f:f.write(f"\nrecovery_target_time='{target}'\n")
        p=call([bindir/'pg_ctl','-D',data,'-l',dest/'server.log','-w','start'],'start_recovery',60)
        if p['returncode']:raise RuntimeError('recovery start failed')
        time.sleep(5)
        catalog=sql("SELECT oid FROM pg_database WHERE datname='test'",'restored_catalog')
        connection=call([bindir/'psql','-X','-d','test','-c','select 1'],'connect_test')
        exists=(data/'base'/oid).exists();rec['restored_test_directory_exists']=exists
        # Require the report's catalog-present / directory-missing mismatch, not any recovery error.
        return finish('CATALOG_WITHOUT_FILES' if catalog['stdout'].strip()==oid and not exists and connection['returncode'] else 'NO_CATALOG_FILE_MISMATCH',connection['stderr'])
    if mode=='attachment_plan':
        home=ROOT/'materials/17292_extracted/buggy'
        scripts=spec['attachment_scripts']
        for n,name in enumerate(scripts):
            # The source \i paths are relative to the supplied archive root.
            script='\\cd '+str(home)+'\n\\set ON_ERROR_STOP on\n\\i '+str(home/name)+'\n'
            result=call([bindir/'psql','-X','-At'],'attachment_setup_'+str(n),120,input=script.encode())
            if result['returncode']:raise RuntimeError('source attachment setup failed: '+name)
        result=sql(spec['parts'][0]['text'],'plan',180)
        return finish(result['stdout'],result['stderr'],result['timed_out'])
    raise ValueError('unsupported special mode '+mode)
