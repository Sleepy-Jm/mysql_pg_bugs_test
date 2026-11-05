#!/usr/bin/env python3
"""Exact-revision isolated replay of three generated SQL scripts; standard library only."""
import argparse
import datetime
from decimal import Decimal, InvalidOperation
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import time
import uuid
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
OLD = Path('/CACHE_ROOT/mysql-intro-bisect-20261103')
IMAGE = 'sha256:b2f51e7795136616ef1b1a35c529fb290dfdfe8e5f7fdd348248b5991f38674d'
REPEATS = 3


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    tmp.replace(path)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command(args, timeout=120, data=None, check=True):
    result = subprocess.run([str(a) for a in args], input=data, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, timeout=timeout)
    if check and result.returncode:
        raise RuntimeError('%s\n%s' % (args, (result.stdout + result.stderr).decode('utf-8', errors='replace')[-4000:]))
    return result


def text(args, **kwargs):
    return command(args, **kwargs).stdout.decode('utf-8', errors='replace').strip()


def git(*args):
    return text(['git', '-C', ROOT/'repo', *args], timeout=900)


def progress(event, **fields):
    entry = {'time': now(), 'event': event, **fields}
    save(ROOT/'status.json', entry)
    print(json.dumps(entry, ensure_ascii=False), flush=True)


def verify_cache(runtime, revision):
    manifest = json.loads((runtime/'manifest.json').read_text())
    assert manifest['sha'] == revision and manifest['patch_mode'] is None and manifest['diff'] == ''
    hashes = {}
    for line in manifest['binary_hashes'].splitlines():
        expected, path = line.split(None, 1)
        binary = runtime/'bin'/Path(path).name
        assert sha(binary) == expected, str(binary)
        hashes[binary.name] = expected
    assert set(hashes) == {'mysqld','mysql','mysqladmin'}
    assert manifest['builder_image'] == IMAGE
    return manifest, hashes


def get_runtime(revision):
    label = revision[:12]
    cached = OLD/'runtime'/label
    if (cached/'manifest.json').exists():
        metadata, hashes = verify_cache(cached, revision)
        save(ROOT/'results/builds'/f'{label}.json', {'source':'existing_verified_cache', 'path':str(cached),
             'original_manifest':metadata, 'verified_binary_sha256':hashes, 'verified_at':now()})
        progress('runtime_cache_verified', revision=revision)
        return cached
    runtime = ROOT/'runtime'/label
    if (runtime/'manifest.json').exists():
        verify_cache(runtime, revision)
        return runtime
    assert not git('status', '--porcelain', '--untracked-files=no'), 'Owned source snapshot is dirty'
    git('checkout', '--detach', revision)
    assert git('rev-parse','HEAD') == revision
    metadata = {'sha':revision,'parents':git('show','-s','--format=%P',revision).split(),
                'tree':git('rev-parse',revision+'^{tree}'),'patch_mode':None,'diff':'',
                'builder_image':IMAGE,'started':now(),'mode':'Release','debug':False,
                'build_script_sha256':sha(ROOT/'build.sh')}
    save(ROOT/'results/builds'/f'{label}.json',metadata)
    progress('build_started', revision=revision)
    args = ['docker','run','--rm','--name','codex-three-build-'+label,'--network','none',
            '--cpus','8','--memory','24g','--user',f'{os.getuid()}:{os.getgid()}',
            '-v',str(ROOT)+':/work','-v',str(OLD/'downloads')+':/work/downloads:ro',
            IMAGE,'bash','/work/build.sh',label]
    metadata['command'] = args
    with (ROOT/'logs'/f'build-{label}.log').open('wb') as out:
        result = subprocess.run(args,stdout=out,stderr=subprocess.STDOUT,timeout=7200)
    metadata['returncode'] = result.returncode
    metadata['finished'] = now()
    save(ROOT/'results/builds'/f'{label}.json',metadata)
    if result.returncode:
        raise RuntimeError('Build failed; see logs/build-'+label+'.log')
    assert not git('status','--porcelain','--untracked-files=no')
    metadata['binary_hashes'] = ''.join(f'{sha(runtime/"bin"/b)}  runtime/{label}/bin/{b}\n'
                                        for b in ('mysql','mysqladmin','mysqld'))
    save(runtime/'manifest.json',metadata)
    save(ROOT/'results/builds'/f'{label}.json',metadata)
    verify_cache(runtime, revision)
    progress('build_finished', revision=revision)
    return runtime


def xml_results(raw):
    body = re.sub(r'<\?xml[^?]*\?>','',raw)
    root = ET.fromstring('<all>'+body+'</all>')
    parsed = []
    for rs in root.findall('resultset'):
        rows, columns = [], None
        for row in rs.findall('row'):
            fields = row.findall('field')
            names = [f.attrib['name'] for f in fields]
            if columns is None:
                columns = names
            assert columns == names
            rows.append([None if any(k.endswith('}nil') and v=='true' for k,v in f.attrib.items())
                         else f.text or '' for f in fields])
        parsed.append({'statement':rs.attrib.get('statement'), 'columns':columns or [], 'rows':rows})
    return parsed


def check_rows(actual, expected):
    differences = []
    if actual['columns'] != expected['columns']:
        differences.append({'kind':'columns','actual':actual['columns'],'expected':expected['columns']})
    if len(actual['rows']) != len(expected['rows']):
        differences.append({'kind':'row_count','actual':len(actual['rows']),'expected':len(expected['rows'])})
    tolerance = Decimal(expected.get('absolute_tolerance','0'))
    for ri,(got,want) in enumerate(zip(actual['rows'],expected['rows'])):
        if len(got) != len(want):
            differences.append({'kind':'row_width','row':ri,'actual':got,'expected':want})
            continue
        for ci,(a,e) in enumerate(zip(got,want)):
            if a is None or e is None:
                equal = a is None and e is None
            elif isinstance(e,(int,float)) or expected['comparison'].startswith('numeric'):
                try:
                    error = abs(Decimal(a)-Decimal(str(e)))
                    equal = error <= (tolerance if expected['columns'][ci]=='avg_v' else Decimal(0))
                except (InvalidOperation,TypeError):
                    equal = False
            else:
                equal = a == e
            if not equal:
                differences.append({'kind':'cell','row':ri,'column':expected['columns'][ci],
                                    'actual':a,'expected':e})
    return differences


def evaluate(stdout, stderr, expected):
    result = {'cases':[], 'sql_errors':re.findall(r'ERROR[^\n]*',stderr), 'parse_error':None}
    try:
        datasets = xml_results(stdout)
    except Exception as exc:
        datasets = []
        result['parse_error'] = str(exc)
    result['parsed_resultsets'] = datasets
    by_id, pending, order = {}, None, []
    for dataset in datasets:
        if dataset['columns'] == ['case_id'] and len(dataset['rows'])==1:
            pending = dataset['rows'][0][0]
            order.append(pending)
        elif pending is not None:
            if pending in by_id:
                result['parse_error'] = 'Duplicate result for '+pending
            by_id[pending] = dataset
            pending = None
    expected_order = [c['case_id'] for c in expected]
    result['label_order'] = order
    result['labels_complete_and_ordered'] = order == expected_order
    for case in expected:
        ident = case['case_id']
        if ident not in by_id:
            result['cases'].append({'case_id':ident,'status':'missing_result','expected_rows':case['rows']})
            continue
        observed = by_id[ident]
        diff = check_rows(observed,case)
        result['cases'].append({'case_id':ident,'status':'mismatch' if diff else 'pass',
                               'differences':diff,'actual_rows':observed['rows'],'expected_rows':case['rows']})
    return result


def trials(target, revision, role, runtime):
    run_id = revision[:12]+'-'+uuid.uuid4().hex[:8]
    name = 'codex-three-'+run_id
    dest = ROOT/'results'/target['name']/role
    dest.mkdir(parents=True,exist_ok=True)
    sql_path = ROOT/'input/sql'/(target['name']+'.sql')
    expected_path = ROOT/'input/expected'/(target['name']+'.json')
    sql = sql_path.read_bytes()
    expected = json.loads(expected_path.read_text())['cases']
    result = {'target':target['name'],'revision':revision,'role':role,'run_id':run_id,
              'started':now(),'sql_sha256':sha(sql_path),'expected_sha256':sha(expected_path),
              'runtime_path':str(runtime),'builder_image':IMAGE,'trials':[],
              'runtime_error':None,'runner_sha256':sha(Path(__file__)),
              'source_branch_coverage':'not_instrumented'}
    client = ['/runtime/bin/mysql','--no-defaults','--protocol=socket',
              '--socket=/work/data/'+run_id+'/mysql.sock','-uroot']
    container_id = None
    try:
        args = ['docker','run','-d','--name',name,'--label','experiment='+ROOT.name,
                '--network','none','--cpus','2','--memory','3g','--user',f'{os.getuid()}:{os.getgid()}',
                '-v',str(ROOT)+':/work','-v',str(runtime)+':/runtime:ro',IMAGE,
                'bash','/work/server.sh',run_id]
        result['launch_command'] = args
        container_id = text(args)
        result['container_id'] = container_id
        deadline = time.monotonic()+240
        while time.monotonic()<deadline:
            state = text(['docker','inspect',name,'--format','{{.State.Running}}'])
            if state!='true':
                raise RuntimeError('Container exited during initialization')
            ping = command(['docker','exec',name]+client+['-NBe','SELECT 1'],check=False)
            if ping.returncode==0 and text(['docker','exec',name,'cat','/proc/1/comm'])=='mysqld':
                break
            time.sleep(2)
        else:
            raise RuntimeError('Startup timed out')
        metadata_query = ('SELECT VERSION(),@@version_compile_os,@@version_compile_machine,'
                          '@@sql_mode,@@optimizer_switch,@@windowing_use_high_precision,'
                          '@@character_set_server,@@collation_server')
        result['server_metadata_tsv'] = text(['docker','exec',name]+client+['-NBe',metadata_query])
        result['mysqld_sha256'] = text(['docker','exec',name,'sha256sum','/runtime/bin/mysqld']).split()[0]
        assert result['mysqld_sha256']==sha(runtime/'bin/mysqld')
        progress('replay_started',target=target['name'],role=role,revision=revision)
        for repeat in range(1,REPEATS+1):
            schema = 'wf_three_'+revision[:12]+'_'+str(repeat)
            command(['docker','exec',name]+client+['-e','CREATE DATABASE '+schema+' CHARACTER SET utf8mb4 COLLATE utf8mb4_bin'])
            call = ['docker','exec','-i',name]+client+['--default-character-set=utf8mb4','--xml','--force','--binary-mode', '--database='+schema]
            entry = {'repeat':repeat,'started':now(),'command':call,'schema':schema,'timeout':False}
            stem = dest/f'trial-{repeat}'
            try:
                execution = command(call,data=sql,timeout=120,check=False)
                stdout,stderr = execution.stdout,execution.stderr
                entry['returncode'] = execution.returncode
            except subprocess.TimeoutExpired as exc:
                stdout,stderr = exc.stdout or b'',exc.stderr or b''
                entry['returncode'] = None
                entry['timeout'] = True
            stem.with_suffix('.stdout.xml').write_bytes(stdout)
            stem.with_suffix('.stderr.txt').write_bytes(stderr)
            entry['evaluation'] = evaluate(stdout.decode('utf-8',errors='replace'),stderr.decode('utf-8',errors='replace'),expected)
            entry['server_state'] = json.loads(text(['docker','inspect',name,'--format','{{json .State}}']))
            entry['finished'] = now()
            entry['stdout_sha256'] = hashlib.sha256(stdout).hexdigest()
            entry['stderr_sha256'] = hashlib.sha256(stderr).hexdigest()
            result['trials'].append(entry)
            save(dest/'result.json',result)
            statuses = {c['case_id']:c['status'] for c in entry['evaluation']['cases']}
            progress('trial_finished',target=target['name'],role=role,repeat=repeat,statuses=statuses,
                     sql_errors=entry['evaluation']['sql_errors'])
            if entry['timeout'] or not entry['server_state']['Running']:
                break
    except Exception as exc:
        result['runtime_error'] = str(exc)
        progress('replay_error',target=target['name'],role=role,error=str(exc))
    finally:
        if container_id:
            result['state_before_cleanup'] = json.loads(text(['docker','inspect',name,'--format','{{json .State}}']))
            logs = command(['docker','logs',name],check=False)
            (dest/'container.txt').write_bytes(logs.stdout+logs.stderr)
            command(['docker','stop','-t','10',name],check=False,timeout=45)
            logs = command(['docker','logs',name],check=False)
            (dest/'container.txt').write_bytes(logs.stdout+logs.stderr)
            source_log = ROOT/'data'/run_id/'server.log'
            if source_log.is_file():
                shutil.copyfile(source_log,dest/'server.txt')
            command(['docker','rm',name],check=False)
            result['container_removed'] = command(['docker','inspect',name],check=False).returncode!=0
        result['finished'] = now()
        save(dest/'result.json',result)
    return result


def workflow():
    assert (ROOT/'.owned-three-prompt-run').is_file()
    for folder in ('logs','results/builds','runtime','data'):
        (ROOT/folder).mkdir(parents=True,exist_ok=True)
    assert text(['docker','image','inspect',IMAGE,'--format','{{.Id}}'])==IMAGE
    provenance = json.loads((ROOT/'input/provenance.json').read_text())
    generated = json.loads((ROOT/'input/generation_manifest.json').read_text())
    for record in generated['targets']:
        assert sha(ROOT/'input'/record['sql'])==record['sql_sha256']
        assert sha(ROOT/'input'/record['expected'])==record['expected_sha256']
    targets = provenance['targets']
    # Reuse the two verified runtimes first, then build each other parent/child pair.
    targets.sort(key=lambda t: 0 if t['revision'].startswith('248c') else 1)
    results = []
    for target in targets:
        actual_parents = git('show','-s','--format=%P',target['revision']).split()
        assert target['parent'] in actual_parents
        for role,revision in (('parent',target['parent']),('target',target['revision'])):
            try:
                runtime = get_runtime(revision)
                outcome = trials(target,revision,role,runtime)
            except Exception as exc:
                outcome = {'target':target['name'],'role':role,'revision':revision,'error':str(exc),'trials':[]}
                save(ROOT/'results'/target['name']/role/'result.json',outcome)
                progress('pair_side_blocked',target=target['name'],role=role,error=str(exc))
            results.append(outcome)
            save(ROOT/'results/index.json',results)
    progress('workflow_finished',sides=len(results))


if __name__=='__main__':
    workflow()
