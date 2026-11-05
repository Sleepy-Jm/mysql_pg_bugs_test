#!/usr/bin/env python3
"""Replay a frozen SQL batch in new, offline MySQL Docker containers.

Dry-run is the default. This program never pulls images, reuses an existing
container, deletes an existing database host directory, or labels observations
as confirmed bugs. Compatible with Python 3.8+.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import uuid
from pathlib import Path

VERSIONS = tuple('8.0.' + str(v) for v in range(31, 36))
IDENTIFIER = re.compile(r'^[A-Za-z0-9][A-Za-z0-9_-]{0,119}$')
PURPOSE = 'mysql-candidate-replay-20261028'


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf8')


def safe_id(value, field):
    if not isinstance(value, str) or not IDENTIFIER.fullmatch(value):
        raise ValueError('Unsafe or missing ' + field)
    return value


def validate_manifest(path):
    path = Path(path).resolve()
    manifest = json.loads(path.read_text(encoding='utf8'))
    safe_id(manifest.get('run_id'), 'run_id')
    if not isinstance(manifest.get('cases'), list) or not manifest['cases']:
        raise ValueError('No cases supplied')
    cases_seen, runs_seen, rows = set(), set(), []
    for case in manifest['cases']:
        cid = safe_id(case.get('case_id'), 'case_id')
        if cid in cases_seen:
            raise ValueError('Duplicate case_id ' + cid)
        cases_seen.add(cid)
        if not str(case.get('report_id', '')).isdigit():
            raise ValueError('report_id must be numeric')
        relative = Path(case['sql_file'])
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError('SQL path must be relative and contained in manifest directory')
        sql = (path.parent / relative).resolve()
        try:
            sql.relative_to(path.parent)
        except ValueError:
            raise ValueError('SQL path escapes manifest directory')
        if not sql.is_file() or sha(sql) != case.get('script_sha256'):
            raise ValueError('SQL hash mismatch: ' + cid)
        if not isinstance(case.get('runs'), list) or not case['runs']:
            raise ValueError('Case has no runs: ' + cid)
        for run in case['runs']:
            rid = safe_id(run.get('run_id'), 'execution run_id')
            if rid in runs_seen:
                raise ValueError('Duplicate execution run_id ' + rid)
            runs_seen.add(rid)
            if run.get('requested_version') not in VERSIONS:
                raise ValueError('Unsupported requested version')
            if run.get('target_version') not in VERSIONS:
                raise ValueError('Unsupported target version')
            if run.get('role') not in ('target', 'adjacent_comparison', 'historical_calibration', 'calibration'):
                raise ValueError('Unsupported role')
            if type(run.get('repeat')) is not int or not 1 <= run['repeat'] <= 3:
                raise ValueError('Repeat must be 1..3')
            if run.get('cohort') not in ('candidate_replay', 'historical_calibration'):
                raise ValueError('Unsupported cohort')
            if run['cohort'] == 'candidate_replay':
                expected = (run['target_version'] if run['role'] == 'target' else
                            '8.0.' + str(int(run['target_version'].split('.')[-1]) - 1)
                            if run['role'] == 'adjacent_comparison' else None)
                if expected != run['requested_version']:
                    raise ValueError('Candidate role/version mismatch')
            row = dict(run, case_id=cid, report_id=str(case['report_id']),
                       sql_file=case['sql_file'], script_sha256=case['script_sha256'],
                       sql_path=str(sql))
            rows.append(row)
    return manifest, rows


def text(value):
    if isinstance(value, bytes):
        return value.decode('utf8', errors='replace')
    return value or ''


def command(args, input_text=None, timeout=60):
    started = time.monotonic()
    try:
        proc = subprocess.run(args, input=input_text, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, encoding='utf8', errors='replace', timeout=timeout)
        return {'returncode': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr,
                'timed_out': False, 'elapsed_seconds': time.monotonic() - started}
    except subprocess.TimeoutExpired as exc:
        return {'returncode': None, 'stdout': text(exc.stdout), 'stderr': text(exc.stderr),
                'timed_out': True, 'elapsed_seconds': time.monotonic() - started}
    except OSError as exc:
        return {'returncode': None, 'stdout': '', 'stderr': str(exc),
                'timed_out': False, 'transport_error': True, 'elapsed_seconds': time.monotonic() - started}


def make_container_command(name, token, run_id, image_id, data):
    return ['docker', 'run', '-d', '--pull=never', '--name', name,
            '--network', 'none', '--cpus', '2', '--memory', '2g',
            '--label', 'purpose=' + PURPOSE, '--label', 'replay_token=' + token,
            '--label', 'replay_run_id=' + run_id,
            '--mount', 'type=bind,src=' + str(data.resolve()) + ',dst=/var/lib/mysql',
            '-e', 'MYSQL_ALLOW_EMPTY_PASSWORD=yes', image_id,
            '--skip-log-bin', '--innodb-buffer-pool-size=128M']


def transport_status(result, state, logs):
    signal = re.search(r'mysqld got signal (\d+)', logs)
    return {'execution_status': 'timeout' if result.get('timed_out') else
            'transport_error' if result.get('transport_error') else
            'completed' if result.get('returncode') == 0 else 'client_error',
            'server_signal_from_log': int(signal.group(1)) if signal else None,
            'server_crash_evidence': bool(signal),
            'oom_killed': state.get('OOMKilled'),
            'oracle_outcome': None, 'reproduction_result': None, 'introduction_result': None}


class Batch:
    def __init__(self, manifest_path, output, timeout=60, ready_timeout=360):
        self.manifest_path = Path(manifest_path).resolve()
        self.manifest, self.rows = validate_manifest(self.manifest_path)
        self.output = Path(output).resolve()
        self.timeout = timeout
        self.ready_timeout = ready_timeout
        self.token = uuid.uuid4().hex[:12]
        self.owned = set()
        self.count = 0

    def docker(self, *args, **kwargs):
        return command(['docker'] + list(args), **kwargs)

    def inspect(self, name):
        result = self.docker('inspect', name)
        if result['returncode'] != 0:
            return None
        try:
            return json.loads(result['stdout'])[0]
        except (ValueError, IndexError):
            return None

    def owns(self, name):
        info = self.inspect(name)
        if not info:
            return False
        labels = info.get('Config', {}).get('Labels') or {}
        return (labels.get('purpose') == PURPOSE and labels.get('replay_token') == self.token
                and labels.get('replay_run_id') == self.manifest['run_id'])

    def state(self, name):
        info = self.inspect(name)
        return info.get('State', {}) if info else {}

    def query(self, name, sql, timeout=30, no_headers=False):
        args = ['exec', '-i', name, 'mysql', '-uroot', '--default-character-set=utf8mb4', '--batch', '--raw']
        if no_headers:
            args.append('--skip-column-names')
        return self.docker(*args, input_text=sql, timeout=timeout)

    def wait_ready(self, name, version, require_initialization=False):
        deadline = time.monotonic() + self.ready_timeout
        initialized = not require_initialization
        while time.monotonic() < deadline:
            state = self.state(name)
            if state.get('Status') in ('exited', 'dead'):
                raise RuntimeError('Container stopped before readiness: ' + json.dumps(state))
            if not initialized:
                logs = self.docker('logs', name, timeout=30)
                initialized = 'init process done. Ready for start up.' in logs['stdout'] + logs['stderr']
            if initialized:
                result = self.query(name, 'SELECT VERSION();\n', no_headers=True)
                if result['returncode'] == 0:
                    actual = result['stdout'].strip()
                    if actual != version:
                        raise RuntimeError('Actual version mismatch: requested ' + version + ', got ' + actual)
                    return actual
            time.sleep(2)
        raise RuntimeError('Timed out waiting for final MySQL server')

    def environment(self, name, version, image_info):
        names = ['version', 'version_comment', 'sql_mode', 'optimizer_switch',
                 'character_set_server', 'collation_server', 'time_zone',
                 'default_storage_engine', 'transaction_isolation', 'lower_case_table_names']
        result = self.query(name, 'SELECT ' + ','.join('@@' + x for x in names) + ';\n')
        variables = {}
        lines = result['stdout'].splitlines()
        if result['returncode'] == 0 and len(lines) >= 2:
            variables = dict(zip(names, lines[1].split('\t')))
        if variables.get('version') != version or 'sql_mode' not in variables:
            raise RuntimeError('Cannot verify execution environment: ' + result['stderr'])
        return {'requested_version': version, 'actual_version': variables['version'],
                'image_id': image_info['Id'], 'image_repo_digests': image_info.get('RepoDigests', []),
                'image_architecture': image_info.get('Architecture'), 'container_name': name,
                'network': 'none', 'published_ports': [], 'cpus': 2, 'memory_bytes': 2147483648,
                'variables': variables, 'session_time_zone_for_test': '+00:00',
                'environment_query': result, 'recorded_at_utc': utc()}

    def append(self, row):
        with (self.output / 'records.jsonl').open('a', encoding='utf8') as stream:
            stream.write(json.dumps(row, ensure_ascii=False) + '\n')
            stream.flush()
            os.fsync(stream.fileno())
        self.count += 1
        print(json.dumps({'completed_records': self.count, 'total': len(self.rows),
                          'run_id': row['run_id'], 'version': row['requested_version'],
                          'status': row['execution_status'], 'returncode': row.get('returncode'),
                          'server_signal': row.get('server_signal_from_log')}, ensure_ascii=False), flush=True)

    def blocked(self, row, reason):
        self.append(dict(row, execution_status='blocked', blocked_reason=reason,
                         actual_version=None, started_at_utc=utc(), finished_at_utc=utc(),
                         returncode=None, oracle_outcome=None, reproduction_result=None,
                         introduction_result=None))

    def recover(self, name, version):
        if name not in self.owned or not self.owns(name):
            raise RuntimeError('Refusing to restart a container not owned by this execution')
        restart = self.docker('restart', '-t', '10', name, timeout=180)
        if restart['returncode'] != 0:
            raise RuntimeError('Cannot restart owned container: ' + restart['stderr'])
        return self.wait_ready(name, version)

    def run_one(self, row, name, environment):
        folder = self.output / 'runs' / row['run_id']
        folder.mkdir(parents=True, exist_ok=False)
        started = utc()
        db = 'replay_' + hashlib.sha256((self.token + row['run_id']).encode()).hexdigest()[:24]
        actual = self.wait_ready(name, row['requested_version'])
        mode = self.query(name, 'SELECT @@session.sql_mode;\n', no_headers=True)
        if mode['returncode'] != 0:
            raise RuntimeError('Could not record SQL mode before execution')
        setup = self.query(name, 'CREATE DATABASE `' + db + '`;\n')
        save(folder / 'setup.json', setup)
        if setup['returncode'] != 0:
            result = dict(setup)
            blocked = 'Fresh database initialization failed'
        else:
            # Recheck immutable SQL immediately before use.
            if sha(row['sql_path']) != row['script_sha256']:
                raise RuntimeError('SQL changed after manifest validation')
            sql = 'USE `' + db + '`;\nSET time_zone="+00:00";\n' + Path(row['sql_path']).read_text(encoding='utf8')
            (folder / 'executed.sql').write_text(sql, encoding='utf8')
            result = self.query(name, sql, timeout=self.timeout)
            blocked = None
        finished = utc()
        state = self.state(name)
        logs = self.docker('logs', '--timestamps', '--since', started, name, timeout=60)
        logtext = logs['stdout'] + logs['stderr']
        (folder / 'stdout.txt').write_text(result['stdout'], encoding='utf8')
        (folder / 'stderr.txt').write_text(result['stderr'], encoding='utf8')
        (folder / 'server.log').write_text(logtext, encoding='utf8')
        save(folder / 'container_state.json', state)
        record = dict(row, actual_version=actual, container_name=name, isolated_database=db,
                      started_at_utc=started, finished_at_utc=finished,
                      elapsed_seconds=result['elapsed_seconds'], returncode=result['returncode'],
                      timed_out=result['timed_out'], sql_mode=mode['stdout'].strip(),
                      environment_file='environment-' + actual + '.json',
                      environment_manifest_sha256=sha(self.output / ('environment-' + actual + '.json')),
                      stdout_file=str((folder / 'stdout.txt').relative_to(self.output)),
                      stderr_file=str((folder / 'stderr.txt').relative_to(self.output)),
                      server_log_file=str((folder / 'server.log').relative_to(self.output)),
                      state_file=str((folder / 'container_state.json').relative_to(self.output)),
                      log_capture_returncode=logs['returncode'],
                      **transport_status(result, state, logtext))
        if blocked:
            record.update(execution_status='blocked', blocked_reason=blocked)
        self.append(record)
        if result['timed_out'] or state.get('Running') is False or record['server_crash_evidence']:
            self.recover(name, actual)

    def run(self):
        self.output.mkdir(parents=True, exist_ok=False)
        save(self.output / 'frozen_manifest.json', self.manifest)
        save(self.output / 'run_metadata.json', {'run_id': self.manifest['run_id'], 'execution_token': self.token,
             'started_at_utc': utc(), 'manifest_sha256': sha(self.manifest_path),
             'runner_sha256': sha(__file__), 'planned_records': len(self.rows), 'timeout_seconds': self.timeout,
             'policy': 'New offline containers only; no image pull; observations require separate oracle review.'})
        try:
            for version in VERSIONS:
                rows = [row for row in self.rows if row['requested_version'] == version]
                if not rows:
                    continue
                name = 'mysql-replay-' + self.manifest['run_id'].lower()[:30] + '-' + version.replace('.', '-') + '-' + self.token
                version_started = utc()
                try:
                    image = self.docker('image', 'inspect', 'mysql:' + version)
                    if image['returncode'] != 0:
                        raise RuntimeError('Required local image missing: mysql:' + version)
                    image_info = json.loads(image['stdout'])[0]
                    if self.inspect(name) is not None:
                        raise RuntimeError('Container name already exists; refusing reuse')
                    data = self.output / 'data' / version
                    data.mkdir(parents=True, exist_ok=False)
                    launch = command(make_container_command(name, self.token, self.manifest['run_id'], image_info['Id'], data), timeout=180)
                    save(self.output / ('launch-' + version + '.json'), launch)
                    if self.owns(name):
                        self.owned.add(name)
                    if launch['returncode'] != 0 or name not in self.owned:
                        raise RuntimeError('New container launch failed: ' + launch['stderr'])
                    self.wait_ready(name, version, require_initialization=True)
                    environment = self.environment(name, version, image_info)
                    save(self.output / ('environment-' + version + '.json'), environment)
                except Exception as exc:
                    for row in rows:
                        self.blocked(row, str(exc))
                    if name in self.owned and self.owns(name):
                        stop = self.docker('stop', '-t', '15', name, timeout=180)
                        logs = self.docker('logs', '--timestamps', '--since', version_started, name, timeout=60)
                        (self.output / ('container-' + version + '.log')).write_text(logs['stdout'] + logs['stderr'], encoding='utf8')
                        save(self.output / ('stopped-' + version + '.json'), {'stop': stop, 'state': self.state(name), 'startup_error': str(exc)})
                    continue
                try:
                    for row in rows:
                        before = self.count
                        try:
                            self.run_one(row, name, environment)
                        except Exception as exc:
                            # A recovery failure occurs after append; never append the same key twice.
                            if self.count == before:
                                self.blocked(row, str(exc))
                            save(self.output / 'run_errors' / (row['run_id'] + '.json'), {'error': str(exc), 'time': utc()})
                finally:
                    if name in self.owned and self.owns(name):
                        stop = self.docker('stop', '-t', '15', name, timeout=180)
                        logs = self.docker('logs', '--timestamps', '--since', version_started, name, timeout=60)
                        (self.output / ('container-' + version + '.log')).write_text(logs['stdout'] + logs['stderr'], encoding='utf8')
                        save(self.output / ('stopped-' + version + '.json'), {'stop': stop, 'state': self.state(name)})
        finally:
            for name in self.owned:
                if self.owns(name) and self.state(name).get('Running'):
                    result = self.docker('stop', '-t', '15', name, timeout=180)
                    save(self.output / ('cleanup-' + name + '.json'), result)
            save(self.output / 'completion.json', {'finished_at_utc': utc(), 'records_written': self.count,
                 'planned_records': len(self.rows), 'all_rows_recorded': self.count == len(self.rows),
                 'containers_preserved': sorted(self.owned), 'results_are_observations_not_confirmed_bugs': True})
        return 0 if self.count == len(self.rows) else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--execute', action='store_true')
    parser.add_argument('--timeout', type=int, default=60)
    args = parser.parse_args(argv)
    if not 1 <= args.timeout <= 300:
        parser.error('timeout must be 1..300 seconds')
    batch = Batch(args.manifest, args.output, args.timeout)
    print(json.dumps({'run_id': batch.manifest['run_id'], 'cases': len(batch.manifest['cases']),
                      'planned_records': len(batch.rows), 'execute': args.execute}, ensure_ascii=False), flush=True)
    if not args.execute:
        return 0
    if os.name != 'posix':
        parser.error('Execution requires a Linux Docker host; dry-run is portable')
    return batch.run()


if __name__ == '__main__':
    sys.exit(main())
