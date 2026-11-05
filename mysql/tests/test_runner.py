import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import run_mysql_batch as runner


def fixture(folder):
    folder = Path(folder)
    sql = folder / 'case.sql'
    sql.write_text('SELECT 1;\n', encoding='utf8')
    manifest = {'run_id': 'sample_batch', 'cases': [{'case_id': 'case_1', 'report_id': '121512',
        'sql_file': 'case.sql', 'script_sha256': runner.sha(sql), 'runs': [
            {'run_id': 'run_1', 'target_version': '8.0.32', 'requested_version': '8.0.32',
             'role': 'target', 'repeat': 1, 'task_id': 'task_1', 'cohort': 'candidate_replay'}]}]}
    path = folder / 'batch_manifest.json'
    path.write_text(json.dumps(manifest), encoding='utf8')
    return path, manifest


class Tests(unittest.TestCase):
    def test_default_dry_run_never_calls_docker_or_creates_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            path, _ = fixture(temporary)
            out = Path(temporary) / 'output'
            with mock.patch.object(runner, 'command', side_effect=AssertionError('No subprocess in dry-run')):
                self.assertEqual(runner.main(['--manifest', str(path), '--output', str(out)]), 0)
            self.assertFalse(out.exists())

    def test_hash_change_is_rejected_before_execution(self):
        with tempfile.TemporaryDirectory() as temporary:
            path, _ = fixture(temporary)
            (Path(temporary) / 'case.sql').write_text('SELECT 2;', encoding='utf8')
            with self.assertRaisesRegex(ValueError, 'hash mismatch'):
                runner.validate_manifest(path)

    def test_path_traversal_and_duplicate_run_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            path, data = fixture(temporary)
            data['cases'][0]['sql_file'] = '../case.sql'
            path.write_text(json.dumps(data), encoding='utf8')
            with self.assertRaisesRegex(ValueError, 'contained'):
                runner.validate_manifest(path)
            data['cases'][0]['sql_file'] = 'case.sql'
            data['cases'][0]['runs'] *= 2
            path.write_text(json.dumps(data), encoding='utf8')
            with self.assertRaisesRegex(ValueError, 'Duplicate execution'):
                runner.validate_manifest(path)

    def test_unknown_versions_and_shell_names_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            path, data = fixture(temporary)
            data['cases'][0]['runs'][0]['requested_version'] = 'latest'
            path.write_text(json.dumps(data), encoding='utf8')
            with self.assertRaisesRegex(ValueError, 'Unsupported requested'):
                runner.validate_manifest(path)

    def test_candidate_role_must_use_corresponding_version(self):
        with tempfile.TemporaryDirectory() as temporary:
            path, data = fixture(temporary)
            data['cases'][0]['runs'][0]['role'] = 'adjacent_comparison'
            path.write_text(json.dumps(data), encoding='utf8')
            with self.assertRaisesRegex(ValueError, 'role/version mismatch'):
                runner.validate_manifest(path)
            data['run_id'] = 'x;echo dangerous'
            path.write_text(json.dumps(data), encoding='utf8')
            with self.assertRaisesRegex(ValueError, 'Unsafe'):
                runner.validate_manifest(path)

    def test_actual_version_mismatch_blocks(self):
        with tempfile.TemporaryDirectory() as temporary:
            path, _ = fixture(temporary)
            batch = runner.Batch(path, Path(temporary) / 'out')
            with mock.patch.object(batch, 'state', return_value={'Status': 'running'}), mock.patch.object(batch, 'query', return_value={'returncode': 0, 'stdout': '8.0.35\n'}):
                with self.assertRaisesRegex(RuntimeError, 'Actual version mismatch'):
                    batch.wait_ready('container', '8.0.32')

    def test_initialization_marker_required_before_query(self):
        with tempfile.TemporaryDirectory() as temporary:
            path, _ = fixture(temporary)
            batch = runner.Batch(path, Path(temporary) / 'out', ready_timeout=1)
            with mock.patch.object(batch, 'state', return_value={'Status': 'running'}), mock.patch.object(batch, 'docker', return_value={'stdout': 'temporary server ready', 'stderr': ''}), mock.patch.object(batch, 'query') as query, mock.patch.object(runner.time, 'sleep'):
                with mock.patch.object(runner.time, 'monotonic', side_effect=[0, 0, 2]):
                    with self.assertRaisesRegex(RuntimeError, 'Timed out'):
                        batch.wait_ready('container', '8.0.32', True)
                query.assert_not_called()

    def test_nonzero_exit_not_automatically_crash(self):
        result = {'returncode': 137, 'timed_out': False}
        status = runner.transport_status(result, {'OOMKilled': True}, '')
        self.assertFalse(status['server_crash_evidence'])
        self.assertTrue(status['oom_killed'])
        self.assertIsNone(status['oracle_outcome'])
        status = runner.transport_status(result, {}, 'mysqld got signal 11 ;')
        self.assertTrue(status['server_crash_evidence'])
        self.assertEqual(status['server_signal_from_log'], 11)

    def test_docker_has_no_network_no_publish_no_pull(self):
        cmd = runner.make_container_command('safe', 'token', 'run', 'sha256:abc', Path('data'))
        self.assertIn('--pull=never', cmd)
        self.assertEqual(cmd[cmd.index('--network') + 1], 'none')
        self.assertEqual(cmd[cmd.index('--cpus') + 1], '2')
        self.assertEqual(cmd[cmd.index('--memory') + 1], '2g')
        self.assertNotIn('-p', cmd)
        self.assertIn('sha256:abc', cmd)

    def test_timeout_preserves_partial_output(self):
        with mock.patch.object(runner.subprocess, 'run', side_effect=subprocess.TimeoutExpired(['docker'], 1, output=b'partial', stderr=b'err')):
            result = runner.command(['docker'], timeout=1)
        self.assertTrue(result['timed_out'])
        self.assertEqual(result['stdout'], 'partial')
        self.assertEqual(result['stderr'], 'err')

    def test_cannot_restart_foreign_container(self):
        with tempfile.TemporaryDirectory() as temporary:
            path, _ = fixture(temporary)
            batch = runner.Batch(path, Path(temporary) / 'out')
            with mock.patch.object(batch, 'docker', side_effect=AssertionError('No mutation')):
                with self.assertRaisesRegex(RuntimeError, 'not owned'):
                    batch.recover('existing_production_mysql', '8.0.32')

    def test_append_records_including_blocked(self):
        with tempfile.TemporaryDirectory() as temporary:
            path, _ = fixture(temporary)
            batch = runner.Batch(path, Path(temporary) / 'out')
            batch.output.mkdir()
            batch.blocked(batch.rows[0], 'Required local image missing')
            row = json.loads((batch.output / 'records.jsonl').read_text(encoding='utf8'))
            self.assertEqual(row['execution_status'], 'blocked')
            self.assertIsNone(row['actual_version'])
            self.assertIsNone(row['oracle_outcome'])
            self.assertEqual(batch.count, 1)


if __name__ == '__main__':
    unittest.main()
