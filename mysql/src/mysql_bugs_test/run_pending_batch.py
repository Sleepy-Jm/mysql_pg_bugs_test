#!/usr/bin/env python3
"""Bounded, target-only first-batch MySQL replay. Dry-run by default.

No image pulls, previous-version controls, reuse, restart/recovery, or deletion.
Only the frozen reports/versions may run; observations require separate oracles.
Compatible with Python 3.8+ and the standard library.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import uuid

VERSIONS = ('8.0.32', '8.0.33', '8.0.34', '8.0.35')
PURPOSE = 'mysql-official-pending230-20261029'
ID = re.compile(r'^[A-Za-z0-9][A-Za-z0-9_-]{0,119}$')
IMAGE = re.compile(r'^sha256:[0-9a-f]{64}$')
SYSTEM_DATABASES = {'information_schema', 'mysql', 'performance_schema', 'sys'}
SQL_TIMEOUT = 20
STARTUP_TIMEOUT = 180
BATCH_TIMEOUT = 600

def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf8')

def safe_id(value, label):
    if not isinstance(value, str) or not ID.fullmatch(value):
        raise ValueError('Unsafe or missing ' + label)
    return value

def contained(base, relative):
    rel = Path(relative)
    if rel.is_absolute() or '..' in rel.parts:
        raise ValueError('Path must be relative and contained')
    result = (base / rel).resolve()
    try:
        result.relative_to(base.resolve())
    except ValueError:
        raise ValueError('Path escapes manifest directory')
    return result

def validate_manifest(path):
    path = Path(path).resolve()
    m = json.loads(path.read_text(encoding='utf8'))
    safe_id(m.get('run_id'), 'run_id')
    kind = m.get('batch_kind', 'initial')
    if kind not in {'initial', 'confirmation'}:
        raise ValueError('Unsupported batch_kind')
    scope_reports = m.get('scope_report_ids', [])
    if not 1 <= len(scope_reports) <= 10 or len(set(scope_reports)) != len(scope_reports) or not all(isinstance(i, str) and i.isdigit() for i in scope_reports):
        raise ValueError('Frozen scope must contain 1..10 unique report IDs')
    scope_tasks = m.get('scope_task_ids', [])
    if not scope_tasks or len(set(scope_tasks)) != len(scope_tasks):
        raise ValueError('Missing or duplicate frozen scope_task_ids')
    for task in scope_tasks:
        if not any(task == 'mysql-' + rid + '-' + v for rid in scope_reports for v in VERSIONS):
            raise ValueError('Scope contains an unsupported report/version pair')
    images = m.get('image_ids', {})
    rows, cases_seen, runs_seen, pairs = [], set(), set(), set()
    for case in m.get('cases', []):
        cid = safe_id(case.get('case_id'), 'case_id')
        rid = str(case.get('report_id', ''))
        if cid in cases_seen or rid not in scope_reports:
            raise ValueError('Duplicate case or report outside frozen scope')
        cases_seen.add(cid)
        sql = contained(path.parent, case['sql_file'])
        if not sql.is_file() or sha(sql) != case.get('script_sha256'):
            raise ValueError('SQL hash mismatch: ' + rid)
        if case.get('source_sql_sha256', case['script_sha256']) != case['script_sha256']:
            raise ValueError('First batch must use the reviewed source SQL bytes')
        if not case.get('runs'):
            raise ValueError('Case has no runs')
        force = case.get('mysql_force', False)
        if type(force) is not bool or (force and not case.get('expected_error_contract')):
            raise ValueError('mysql_force requires a frozen reviewed expected-error contract')
        for run in case['runs']:
            run_id = safe_id(run.get('run_id'), 'execution run_id')
            version = run.get('requested_version')
            if version not in VERSIONS or run.get('target_version') != version:
                raise ValueError('Only matching 8.0.32..35 target versions are allowed')
            if run.get('role') != 'target' or run.get('cohort', 'candidate_replay') != 'candidate_replay':
                raise ValueError('Only target candidate replay is permitted')
            task_id = 'mysql-' + rid + '-' + version
            if run.get('task_id') != task_id or task_id not in scope_tasks:
                raise ValueError('Task outside frozen report/version scope')
            repeat = run.get('repeat')
            if type(repeat) is not int or repeat not in ((1,) if kind == 'initial' else (2, 3)):
                raise ValueError('Initial repeat must be 1; confirmation repeats only 2/3')
            if run_id in runs_seen or (task_id, repeat) in pairs:
                raise ValueError('Duplicate execution run or task/repeat')
            if not IMAGE.fullmatch(images.get(version, '')):
                raise ValueError('A frozen local image ID is required for ' + version)
            runs_seen.add(run_id)
            pairs.add((task_id, repeat))
            rows.append(dict(run, case_id=cid, report_id=rid, sql_file=case['sql_file'],
                             sql_path=str(sql), script_sha256=case['script_sha256'],
                             mysql_force=force,
                             source_sql_sha256=case.get('source_sql_sha256', case['script_sha256'])))
    if not rows:
        raise ValueError('No executions selected')
    if kind == 'initial':
        if set(r['report_id'] for r in rows) != set(scope_reports) or set(r['task_id'] for r in rows) != set(scope_tasks):
            raise ValueError('Initial batch must cover exactly the frozen selection')
    else:
        # A confirmation is one follow-up batch, bound to the immutable initial
        # records. Repeat numbers 2/3 plus the sole initial attempt cap each pair.
        history = m.get('initial_evidence', {})
        history_manifest = contained(path.parent, history.get('manifest_file', ''))
        history_records = contained(path.parent, history.get('records_file', ''))
        if not history_manifest.is_file() or sha(history_manifest) != history.get('manifest_sha256'):
            raise ValueError('Initial manifest evidence hash mismatch')
        if not history_records.is_file() or sha(history_records) != history.get('records_sha256'):
            raise ValueError('Initial records evidence hash mismatch')
        original = json.loads(history_manifest.read_text(encoding='utf8'))
        if original.get('batch_kind', 'initial') != 'initial' or original.get('scope_report_ids') != scope_reports or original.get('scope_task_ids') != scope_tasks:
            raise ValueError('Confirmation scope differs from the initial batch')
        original_cases = {str(c['report_id']): c['script_sha256'] for c in original['cases']}
        recorded = [json.loads(line) for line in history_records.read_text(encoding='utf8').splitlines() if line.strip()]
        for row in rows:
            prior = [r for r in recorded if r.get('task_id') == row['task_id']]
            if len(prior) != 1 or prior[0].get('repeat') != 1 or not prior[0].get('sql_submitted'):
                raise ValueError('Confirmation needs exactly one submitted initial execution')
            if original_cases.get(row['report_id']) != row['script_sha256']:
                raise ValueError('Confirmation SQL changed')
        if not m.get('confirmation_reason_by_task') or any(r['task_id'] not in m['confirmation_reason_by_task'] for r in rows):
            raise ValueError('Explicit confirmation reason required for each pair')
    by_case = {c['case_id']: c for c in m['cases']}
    for row in rows:
        case = by_case[row['case_id']]
        post = contained(path.parent, case['postcheck_file'])
        if not post.is_file() or sha(post) != case['postcheck_sha256']:
            raise ValueError('Read-only oracle check hash mismatch')
        row.update(postcheck_file=case['postcheck_file'], postcheck_path=str(post), postcheck_sha256=sha(post))
    return m, rows

def as_text(value):
    return value.decode('utf8', errors='replace') if isinstance(value, bytes) else value or ''

def command(args, input_text=None, timeout=30):
    start = time.monotonic()
    try:
        p = subprocess.run(args, input=input_text, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           encoding='utf8', errors='replace', timeout=timeout)
        return {'returncode': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr,
                'timed_out': False, 'elapsed_seconds': time.monotonic() - start}
    except subprocess.TimeoutExpired as exc:
        return {'returncode': None, 'stdout': as_text(exc.stdout), 'stderr': as_text(exc.stderr),
                'timed_out': True, 'elapsed_seconds': time.monotonic() - start}
    except OSError as exc:
        return {'returncode': None, 'stdout': '', 'stderr': str(exc), 'timed_out': False,
                'transport_error': True, 'elapsed_seconds': time.monotonic() - start}

def make_container_command(name, token, run_id, image_id, data):
    return ['docker', 'run', '-d', '--pull=never', '--name', name,
            '--network', 'none', '--cpus', '2', '--memory', '2g', '--memory-swap', '2g',
            '--pids-limit', '256', '--restart', 'no',
            '--label', 'purpose=' + PURPOSE, '--label', 'replay_token=' + token,
            '--label', 'replay_run_id=' + run_id,
            '--mount', 'type=bind,src=' + str(data.resolve()) + ',dst=/var/lib/mysql',
            '-e', 'MYSQL_ALLOW_EMPTY_PASSWORD=yes', image_id,
            '--skip-log-bin', '--innodb-buffer-pool-size=128M']

def observation(result, state, logs):
    signal = re.search(r'mysqld got signal (\d+)', logs)
    assertion = bool(re.search(r'Assertion .+ failed|assertion failure|Failing assertion', logs, re.I))
    errors = [{'code': int(a), 'sqlstate': b} for a, b in re.findall(r'ERROR\s+(\d+)\s+\(([^)]+)\)', result.get('stderr', ''))]
    return {'execution_status': 'timeout' if result.get('timed_out') else
            'transport_error' if result.get('transport_error') else
            'completed_with_sql_errors' if result.get('returncode') == 0 and errors else
            'completed' if result.get('returncode') == 0 else 'client_error',
            'server_signal_from_log': int(signal.group(1)) if signal else None,
            'server_crash_evidence': bool(signal or assertion), 'assertion_in_log': assertion,
            'oom_killed': bool(state.get('OOMKilled')),
            'error_codes': errors,
            'reproduction_result': None, 'introduction_result': None}

class Batch:
    def __init__(self, manifest_path, output):
        self.manifest_path = Path(manifest_path).resolve()
        self.manifest, self.rows = validate_manifest(self.manifest_path)
        self.output = Path(output).resolve()
        self.token = uuid.uuid4().hex[:12]
        self.owned = set()
        self.created_databases = set()
        self.count = 0
        self.halt_reason = None
        self.deadline = None
        self.current_data = None

    def halt(self, reason):
        if not self.halt_reason:
            self.halt_reason = reason

    def budget(self):
        if (self.manifest_path.parent.parent.parent / 'STOP_REQUESTED').exists():
            self.halt('Coordinator requested stop; no additional SQL submitted')
        if self.deadline is not None and time.monotonic() >= self.deadline:
            self.halt('Overall 600-second experiment budget reached')
        return not self.halt_reason

    def docker(self, *args, **kwargs):
        # Cleanup gets an independent short allowance so the time limit cannot
        # leave an owned running container behind.
        timeout = kwargs.pop('timeout', 30)
        if self.deadline is not None and args[0] not in {'stop', 'inspect', 'logs'}:
            timeout = min(timeout, max(0.1, self.deadline - time.monotonic()))
        return command(['docker'] + list(args), timeout=timeout, **kwargs)

    def inspect(self, name):
        r = self.docker('inspect', name)
        if r['returncode'] != 0:
            return None
        try:
            return json.loads(r['stdout'])[0]
        except (ValueError, IndexError):
            return None

    def owns(self, name, info=None):
        info = info if info is not None else self.inspect(name)
        labels = (info or {}).get('Config', {}).get('Labels') or {}
        return labels.get('purpose') == PURPOSE and labels.get('replay_token') == self.token and labels.get('replay_run_id') == self.manifest['run_id']

    def state(self, name):
        return (self.inspect(name) or {}).get('State', {})

    def verify_isolation(self, name):
        info = self.inspect(name)
        host = (info or {}).get('HostConfig', {})
        if name not in self.owned or not self.owns(name, info):
            raise RuntimeError('Isolation boundary: container ownership mismatch')
        mounts = info.get('Mounts', [])
        if (host.get('NetworkMode') != 'none' or host.get('PortBindings') or host.get('Privileged')
                or host.get('NanoCpus') != 2000000000 or host.get('Memory') != 2147483648
                or host.get('MemorySwap') != 2147483648 or host.get('PidsLimit') != 256
                or host.get('RestartPolicy', {}).get('Name') not in ('no', '')
                or len(mounts) != 1 or mounts[0].get('Type') != 'bind'
                or mounts[0].get('Destination') != '/var/lib/mysql'
                or Path(mounts[0].get('Source', '')).resolve() != self.current_data.resolve()):
            raise RuntimeError('Isolation boundary: runtime network/resource/mount settings differ')
        return info

    def query(self, name, sql, timeout=30, no_headers=False, verbose=False, force=False):
        args = ['exec', '-i', name, 'mysql', '-uroot', '--default-character-set=utf8mb4', '--batch', '--raw']
        if no_headers:
            args.append('--skip-column-names')
        if verbose:
            args += ['--verbose', '--show-warnings']
        if force:
            args.append('--force')
        return self.docker(*args, input_text=sql, timeout=timeout)

    def wait_ready(self, name, version):
        deadline = min(time.monotonic() + STARTUP_TIMEOUT, self.deadline or float('inf'))
        while time.monotonic() < deadline:
            state = self.state(name)
            if state.get('OOMKilled') or state.get('Status') in {'exited', 'dead'}:
                raise RuntimeError('Container stopped/OOM before readiness')
            logs = self.docker('logs', name)
            if 'init process done. Ready for start up.' in logs['stdout'] + logs['stderr']:
                r = self.query(name, 'SELECT VERSION();\n', no_headers=True)
                if r['returncode'] == 0:
                    if r['stdout'].strip() != version:
                        raise RuntimeError('Actual version mismatch: ' + r['stdout'].strip())
                    return version
            time.sleep(2)
        raise RuntimeError('Startup time limit reached')

    def verify_databases(self, name):
        r = self.query(name, 'SHOW DATABASES;\n', no_headers=True)
        schemas = set(r['stdout'].splitlines())
        if r['returncode'] != 0 or not SYSTEM_DATABASES <= schemas or schemas - SYSTEM_DATABASES - self.created_databases:
            raise RuntimeError('Isolation boundary: unexpected or unverifiable database contents')
        return {'schemas': sorted(schemas), 'query': r, 'only_system_and_this_batch_schemas': True}

    def environment(self, name, version, image_info):
        names = ['version', 'version_comment', 'version_compile_os', 'version_compile_machine',
                 'sql_mode', 'optimizer_switch', 'character_set_server', 'collation_server',
                 'character_set_client', 'character_set_connection', 'collation_connection',
                 'time_zone', 'default_storage_engine', 'transaction_isolation', 'lower_case_table_names',
                 'div_precision_increment', 'auto_increment_increment', 'auto_increment_offset']
        r = self.query(name, 'SELECT ' + ','.join('@@' + v for v in names) + ';\n')
        lines = r['stdout'].splitlines()
        variables = dict(zip(names, lines[1].split('\t'))) if r['returncode'] == 0 and len(lines) >= 2 else {}
        if variables.get('version') != version:
            raise RuntimeError('Cannot verify actual environment')
        if (variables.get('div_precision_increment') != '4' or variables.get('auto_increment_increment') != '1'
                or variables.get('auto_increment_offset') != '1'):
            raise RuntimeError('Arithmetic/auto-increment settings differ from the reviewed first-batch preconditions')
        engines = self.query(name, 'SHOW ENGINES;\n')
        binary = self.docker('exec', name, 'mysqld', '--version')
        debug = self.query(name, "SHOW VARIABLES LIKE 'debug';\n")
        if engines['returncode'] != 0 or binary['returncode'] != 0 or debug['returncode'] != 0:
            raise RuntimeError('Cannot verify storage engines/build')
        is_debug = 'debug' in (binary['stdout'] + variables.get('version_comment', '')).lower() or len(debug['stdout'].splitlines()) > 1
        if is_debug:
            raise RuntimeError('First batch requires ordinary release build; debug build found')
        db_check = self.verify_databases(name)
        return {'requested_version': version, 'actual_version': version,
                'image_id': image_info['Id'], 'image_repo_digests': image_info.get('RepoDigests', []),
                'image_architecture': image_info.get('Architecture'), 'container_name': name,
                'build_type': 'release', 'build_basis': 'mysqld --version/version_comment contain no debug marker and debug system variable absent',
                'binary_version_command': binary, 'debug_variable_probe': debug,
                'network': 'none', 'published_ports': [], 'cpus': 2, 'memory_bytes': 2147483648,
                'pids_limit': 256, 'variables': variables, 'show_engines': engines,
                'environment_query': r, 'database_precheck': db_check,
                'session_time_zone_for_test': '+00:00', 'recorded_at_utc': utc()}

    def append(self, row):
        with (self.output / 'records.jsonl').open('a', encoding='utf8') as f:
            f.write(json.dumps(row, ensure_ascii=False) + '\n')
            f.flush()
            os.fsync(f.fileno())
        self.count += 1
        print(json.dumps({'completed': self.count, 'total': len(self.rows), 'run_id': row['run_id'],
                          'status': row['execution_status'], 'sql_submitted': row.get('sql_submitted', False)}, ensure_ascii=False), flush=True)

    def blocked(self, row, reason):
        self.append(dict(row, execution_status='blocked', blocked_reason=reason,
                         sql_submitted=False, actual_version=None, reproduction_result=None,
                         introduction_result=None, recorded_at_utc=utc()))

    def run_one(self, row, name):
        if not self.budget():
            self.blocked(row, self.halt_reason)
            return
        self.verify_isolation(name)
        self.verify_databases(name)
        if sha(row['sql_path']) != row['script_sha256']:
            raise RuntimeError('SQL changed after manifest validation')
        folder = self.output / 'runs' / row['run_id']
        folder.mkdir(parents=True, exist_ok=False)
        db = 'replay_' + hashlib.sha256((self.token + row['run_id']).encode()).hexdigest()[:24]
        setup = self.query(name, 'CREATE DATABASE `' + db + '`;\n')
        save(folder / 'setup.json', setup)
        if setup['returncode'] != 0:
            self.halt('Fresh schema initialization failed: ' + setup['stderr'])
            self.blocked(row, self.halt_reason)
            return
        self.created_databases.add(db)
        prelude = 'USE `' + db + '`;\nSET time_zone="+00:00";\n'
        actual_session_probe = ('SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,'
                                '@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,'
                                '@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,'
                                '@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;\n')
        sql = prelude + actual_session_probe + Path(row['sql_path']).read_text(encoding='utf8')
        if sha(row['postcheck_path']) != row['postcheck_sha256']:
            raise RuntimeError('Read-only validation SQL changed')
        sql += '\n' + Path(row['postcheck_path']).read_text(encoding='utf8')
        (folder / 'executed.sql').write_text(sql, encoding='utf8')
        session_sql = ('SET time_zone="+00:00"; SELECT @@sql_mode,@@character_set_client,@@character_set_connection,'
                       '@@collation_connection,@@time_zone,@@default_storage_engine;\n')
        # This separate diagnostic connection uses identical client options and
        # prelude. Source scripts may subsequently change session variables.
        session_defaults = self.query(name, session_sql)
        save(folder / 'session_defaults.json', session_defaults)
        if session_defaults['returncode'] != 0:
            self.halt('Session environment recording failed before source SQL')
            self.blocked(row, self.halt_reason)
            return
        start = utc()
        result = self.query(name, sql, timeout=SQL_TIMEOUT, verbose=True, force=row['mysql_force'])
        finish = utc()
        state = self.state(name)
        logs = self.docker('logs', '--timestamps', '--since', start, name)
        logtext = logs['stdout'] + logs['stderr']
        obs = observation(result, state, logtext)
        for filename, text in [('stdout.txt', result['stdout']), ('stderr.txt', result['stderr']), ('server.log', logtext)]:
            (folder / filename).write_text(text, encoding='utf8')
        save(folder / 'container_state.json', state)
        alive = None
        if not result['timed_out'] and not obs['server_crash_evidence'] and not obs['oom_killed'] and state.get('Running'):
            alive = self.query(name, 'SELECT 1 AS server_alive;\n', timeout=5)
            save(folder / 'server_alive.json', alive)
        record = dict(row, sql_submitted=True, actual_version=row['requested_version'],
                      container_name=name, isolated_database=db, started_at_utc=start, finished_at_utc=finish,
                      elapsed_seconds=result['elapsed_seconds'], returncode=result['returncode'], timed_out=result['timed_out'],
                      environment_file='environment-' + row['requested_version'] + '.json',
                      environment_manifest_sha256=sha(self.output / ('environment-' + row['requested_version'] + '.json')),
                      stdout_file=str((folder / 'stdout.txt').relative_to(self.output)),
                      stderr_file=str((folder / 'stderr.txt').relative_to(self.output)),
                      server_log_file=str((folder / 'server.log').relative_to(self.output)),
                      executed_sql_file=str((folder / 'executed.sql').relative_to(self.output)),
                      executed_sql_sha256=sha(folder / 'executed.sql'), log_capture_returncode=logs['returncode'],
                      session_changes_note='Source SQL runs in one fresh client session after USE and UTC prelude; exact commands in executed.sql.',
                      **obs)
        self.append(record)
        if result['timed_out'] or obs['server_crash_evidence'] or obs['oom_killed'] or not state.get('Running') or result.get('transport_error') or (alive and alive['returncode'] != 0) or logs['returncode'] != 0:
            self.halt('Runtime boundary reached: timeout/crash/OOM/connection or evidence failure at ' + row['run_id'])

    def stop_owned(self, name, version):
        if name not in self.owned or not self.owns(name):
            self.halt('Ownership unavailable during cleanup; no action on unverified container')
            return
        stopped = self.docker('stop', '-t', '10', name, timeout=30)
        logs = self.docker('logs', '--timestamps', name, timeout=30)
        (self.output / ('container-' + version + '.log')).write_text(logs['stdout'] + logs['stderr'], encoding='utf8')
        state = self.state(name)
        save(self.output / ('cleanup-' + version + '.json'), {'container_name': name, 'stop': stopped, 'state': state,
            'action': 'Stop requested only for this owned container; use stop result and observed state to establish success. No deletion performed.',
            'data_preserved': str(self.current_data), 'schemas_created_by_batch': sorted(self.created_databases)})
        if stopped['returncode'] != 0 or state.get('Status') != 'exited':
            self.halt('Owned container could not be confirmed stopped')

    def run(self):
        self.output.mkdir(parents=True, exist_ok=False)
        if self.manifest.get('batch_kind', 'initial') == 'confirmation':
            # The same initial evidence location permits only one confirmation
            # invocation; never silently repeat slots 2/3 with a different output.
            history = self.manifest['initial_evidence']
            records = contained(self.manifest_path.parent, history['records_file'])
            claim = records.with_name(records.name + '.confirmation-claimed.json')
            with claim.open('x', encoding='utf8') as stream:
                json.dump({'confirmation_run_id': self.manifest['run_id'], 'manifest_sha256': sha(self.manifest_path),
                           'claimed_at_utc': utc(), 'output': str(self.output)}, stream)
        self.deadline = time.monotonic() + BATCH_TIMEOUT
        save(self.output / 'frozen_manifest.json', self.manifest)
        save(self.output / 'run_metadata.json', {'run_id': self.manifest['run_id'], 'token': self.token,
            'manifest_sha256': sha(self.manifest_path), 'runner_sha256': sha(__file__), 'started_at_utc': utc(),
            'limits': {'sql_seconds': SQL_TIMEOUT, 'startup_seconds': STARTUP_TIMEOUT, 'batch_seconds': BATCH_TIMEOUT,
                       'cpus': 2, 'memory_bytes': 2147483648, 'pids_limit': 256},
            'policy': 'Frozen target versions only; no pull, previous version, recovery, restart or deletion; stop on boundary failure.'})
        try:
            for version in VERSIONS:
                rows = [r for r in self.rows if r['requested_version'] == version]
                if not rows:
                    continue
                if not self.budget():
                    for row in rows:
                        self.blocked(row, self.halt_reason)
                    continue
                name = 'mysql-first-' + self.manifest['run_id'].lower()[:28] + '-' + version.replace('.', '-') + '-' + self.token
                self.created_databases = set()
                self.current_data = self.output / 'data' / version
                try:
                    image = self.docker('image', 'inspect', self.manifest['image_ids'][version])
                    if image['returncode'] != 0:
                        raise RuntimeError('Required frozen local image unavailable')
                    image_info = json.loads(image['stdout'])[0]
                    if image_info['Id'] != self.manifest['image_ids'][version]:
                        raise RuntimeError('Image ID mismatch')
                    if self.inspect(name) is not None:
                        raise RuntimeError('Refusing to reuse an existing container')
                    self.current_data.mkdir(parents=True, exist_ok=False)
                    if any(self.current_data.iterdir()):
                        raise RuntimeError('New data directory is not empty')
                    cmd = make_container_command(name, self.token, self.manifest['run_id'], image_info['Id'], self.current_data)
                    launch = command(cmd, timeout=min(30, max(0.1, self.deadline - time.monotonic())))
                    save(self.output / ('launch-' + version + '.json'), {'command': cmd, 'result': launch})
                    if self.owns(name):
                        self.owned.add(name)
                    if launch['returncode'] != 0 or name not in self.owned:
                        raise RuntimeError('New owned container launch failed')
                    self.verify_isolation(name)
                    self.wait_ready(name, version)
                    env = self.environment(name, version, image_info)
                    save(self.output / ('environment-' + version + '.json'), env)
                except Exception as exc:
                    self.halt('Environment/initialization boundary: ' + str(exc))
                    for row in rows:
                        self.blocked(row, self.halt_reason)
                    if name in self.owned:
                        self.stop_owned(name, version)
                    continue
                try:
                    for row in rows:
                        before = self.count
                        try:
                            self.run_one(row, name)
                        except Exception as exc:
                            self.halt('Isolation/execution boundary: ' + str(exc))
                            if self.count == before:
                                self.blocked(row, self.halt_reason)
                            save(self.output / 'run_errors' / (row['run_id'] + '.json'), {'error': str(exc), 'time': utc()})
                finally:
                    self.stop_owned(name, version)
        finally:
            # No restart or destructive cleanup. Any container still running is
            # stopped only if all ownership labels still match this execution.
            for name in self.owned:
                if self.owns(name) and self.state(name).get('Running'):
                    save(self.output / ('final-stop-' + name + '.json'), self.docker('stop', '-t', '10', name, timeout=30))
            save(self.output / 'completion.json', {'finished_at_utc': utc(), 'records_written': self.count,
                'planned_records': len(self.rows), 'all_rows_recorded': self.count == len(self.rows),
                'halt_reason': self.halt_reason, 'containers_preserved': sorted(self.owned),
                'no_deletion_performed': True, 'automatic_next_batch': False,
                'results_are_observations_not_confirmed_independent_bugs': True})
        return 0 if self.count == len(self.rows) and not self.halt_reason else 2

def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--manifest', required=True, type=Path)
    p.add_argument('--output', required=True, type=Path)
    p.add_argument('--execute', action='store_true')
    args = p.parse_args(argv)
    batch = Batch(args.manifest, args.output)
    print(json.dumps({'run_id': batch.manifest['run_id'], 'kind': batch.manifest.get('batch_kind', 'initial'),
                      'reports': len(set(r['report_id'] for r in batch.rows)), 'executions': len(batch.rows),
                      'execute': args.execute, 'versions': sorted(set(r['requested_version'] for r in batch.rows))}), flush=True)
    if not args.execute:
        return 0
    if os.name != 'posix':
        p.error('Execution requires the explicitly selected Linux Docker host; dry-run is portable')
    return batch.run()

if __name__ == '__main__':
    sys.exit(main())
