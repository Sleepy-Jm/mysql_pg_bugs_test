"""Offline boundary tests: no process, server or database access."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock
import run_pending_batch as runner

def fixture(directory):
    root=Path(directory)
    (root/'source.sql').write_text('SELECT 11 AS source_value;\n',encoding='utf-8')
    (root/'validation.sql').write_text('SELECT 22 AS validation_value;\n',encoding='utf-8')
    ids=['107337','110003','110125','110244','110256']
    m={'run_id':'test_reviewed','batch_kind':'initial','scope_report_ids':ids,
       'scope_task_ids':[f'mysql-{i}-8.0.32' for i in ids],
       'image_ids':{'8.0.32':'sha256:'+'a'*64},'cases':[]}
    for i in ids:
        m['cases'].append({'case_id':'report_'+i,'report_id':i,'sql_file':'source.sql',
            'script_sha256':runner.sha(root/'source.sql'),'source_sql_sha256':runner.sha(root/'source.sql'),
            'postcheck_file':'validation.sql','postcheck_sha256':runner.sha(root/'validation.sql'),
            'runs':[{'run_id':'run_'+i,'task_id':f'mysql-{i}-8.0.32','requested_version':'8.0.32',
                     'target_version':'8.0.32','role':'target','cohort':'candidate_replay','repeat':1}]})
    path=root/'manifest.json';runner.save(path,m)
    return path,m

OK={'returncode':0,'stdout':'','stderr':'','timed_out':False,'elapsed_seconds':0.01}

class ReviewedRunnerTests(unittest.TestCase):
    def setUp(self):
        self.guard=mock.patch.object(runner,'command',side_effect=AssertionError('No external processes permitted'))
        self.guard.start();self.addCleanup(self.guard.stop)

    def test_postcheck_tamper_before_manifest_load_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            path,_=fixture(td)
            (Path(td)/'validation.sql').write_text('SELECT 99;',encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'oracle check hash mismatch'):runner.validate_manifest(path)

    def test_postcheck_path_escape_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            path,m=fixture(td);m['cases'][0]['postcheck_file']='../outside.sql';runner.save(path,m)
            with self.assertRaisesRegex(ValueError,'contained'):runner.validate_manifest(path)

    def test_postcheck_tamper_after_manifest_load_prevents_source_submission(self):
        with tempfile.TemporaryDirectory() as td:
            path,_=fixture(td);b=runner.Batch(path,Path(td)/'out');b.output.mkdir()
            (Path(td)/'validation.sql').write_text('SELECT 99;',encoding='utf-8')
            with mock.patch.object(b,'verify_isolation'),mock.patch.object(b,'verify_databases'),mock.patch.object(b,'query',return_value=OK) as query:
                with self.assertRaisesRegex(RuntimeError,'validation SQL changed'):b.run_one(b.rows[0],'owned')
            self.assertEqual(query.call_count,1)
            self.assertTrue(query.call_args.args[1].startswith('CREATE DATABASE'))
            self.assertFalse((b.output/'runs'/b.rows[0]['run_id']/'executed.sql').exists())

    def test_source_then_postcheck_share_one_client_submission_and_hash_record(self):
        with tempfile.TemporaryDirectory() as td:
            path,_=fixture(td);b=runner.Batch(path,Path(td)/'out');b.output.mkdir()
            runner.save(b.output/'environment-8.0.32.json',{'actual_version':'8.0.32'})
            with mock.patch.object(b,'verify_isolation'),mock.patch.object(b,'verify_databases'),mock.patch.object(b,'query',return_value=OK) as query,mock.patch.object(b,'state',return_value={'Running':True,'OOMKilled':False}),mock.patch.object(b,'docker',return_value=OK):
                b.run_one(b.rows[0],'owned')
            submissions=[call for call in query.call_args_list if call.kwargs.get('verbose')]
            self.assertEqual(len(submissions),1)
            sql=submissions[0].args[1]
            self.assertTrue(sql.endswith('SELECT 11 AS source_value;\n\nSELECT 22 AS validation_value;\n'))
            record=json.loads((b.output/'records.jsonl').read_text())
            self.assertEqual(record['postcheck_sha256'],runner.sha(Path(td)/'validation.sql'))
            self.assertEqual(record['executed_sql_sha256'],runner.sha(b.output/record['executed_sql_file']))

    def test_unknown_cleanup_state_halts_even_when_stop_command_succeeds(self):
        with tempfile.TemporaryDirectory() as td:
            path,_=fixture(td);b=runner.Batch(path,Path(td)/'out');b.output.mkdir()
            b.owned.add('owned');b.current_data=Path(td)/'new_data'
            with mock.patch.object(b,'owns',return_value=True),mock.patch.object(b,'docker',return_value=OK),mock.patch.object(b,'state',return_value={}):
                b.stop_owned('owned','8.0.32')
            self.assertIn('could not be confirmed stopped',b.halt_reason)
            self.assertIn('Stop requested',json.loads((b.output/'cleanup-8.0.32.json').read_text())['action'])

    def test_explicit_exited_cleanup_state_is_accepted(self):
        with tempfile.TemporaryDirectory() as td:
            path,_=fixture(td);b=runner.Batch(path,Path(td)/'out');b.output.mkdir()
            b.owned.add('owned');b.current_data=Path(td)/'new_data'
            with mock.patch.object(b,'owns',return_value=True),mock.patch.object(b,'docker',return_value=OK),mock.patch.object(b,'state',return_value={'Status':'exited','Running':False}):
                b.stop_owned('owned','8.0.32')
            self.assertIsNone(b.halt_reason)

if __name__=='__main__':unittest.main()
