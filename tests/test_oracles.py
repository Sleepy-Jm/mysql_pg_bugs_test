import unittest
import json
import tempfile
from pathlib import Path
from classify_results import classify, classify_all, load_records


def record(bid, stdout='', **extra):
    return dict(report_id=bid, stdout=stdout, stderr='', returncode=0,
                requested_version='8.0.32', actual_version='8.0.32', execution_status='completed', **extra)


class OracleTests(unittest.TestCase):
    def test_runner_file_interface_and_escape_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'stdout.txt').write_text('ref0\n1\n', encoding='utf8')
            (root / 'stderr.txt').write_text('', encoding='utf8')
            r = record('118625'); r.pop('stdout'); r.pop('stderr')
            r.update(stdout_file='stdout.txt', stderr_file='stderr.txt', timed_out=False, server_crash_evidence=False)
            (root / 'records.jsonl').write_text(json.dumps(r), encoding='utf8')
            self.assertEqual(classify(load_records(root / 'records.jsonl')[0])['oracle_outcome'], 'abnormal')
            r['stdout_file'] = '../outside.txt'
            (root / 'records.jsonl').write_text(json.dumps(r), encoding='utf8')
            with self.assertRaises(ValueError):
                load_records(root / 'records.jsonl')
    def test_version_mismatch_blocks_even_crash(self):
        r = record('121514', server_crash=True); r['actual_version'] = '8.0.35'
        self.assertEqual(classify(r)['oracle_outcome'], 'inconclusive')

    def test_absent_version_pair_is_not_a_match(self):
        r = record('118625'); r.pop('actual_version'); r.pop('requested_version')
        self.assertEqual(classify(r)['oracle_outcome'], 'inconclusive')

    def test_oom_not_crash_bug(self):
        self.assertEqual(classify(record('121514', server_crash=True, oom_killed=True))['oracle_kind'], 'resource_limit')

    def test_server_signal_is_separate_crash(self):
        r = record('121514', server_crash=True); r['returncode'] = 137
        self.assertEqual(classify(r)['oracle_kind'], 'crash')
        self.assertEqual(classify(r)['oracle_outcome'], 'abnormal')

    def test_nonzero_without_signal_not_bug(self):
        r = record('121514'); r.update(returncode=137, stderr='ERROR 2013 connection lost')
        self.assertEqual(classify(r)['oracle_outcome'], 'inconclusive')

    def test_timeout_not_wrong_result(self):
        self.assertEqual(classify(record('109699', timeout=True))['oracle_kind'], 'timeout')

    def test_constant_projection(self):
        self.assertEqual(classify(record('109699', '❤\nžlutý_😀\n'))['oracle_outcome'], 'normal')
        self.assertEqual(classify(record('109699', ''))['oracle_outcome'], 'abnormal')

    def test_window_arithmetic(self):
        output = 'n\tsum(n)\tcount(n)\tavg(n)\tsum(n)/count(n)\n1\t9\t3\t3.0000\t3.0000\n2\t7\t2\t3.5000\t3.5000\n3\t4\t1\t4.0000\t4.0000\n4\tNULL\t0\tNULL\tNULL\n'
        self.assertEqual(classify(record('109725', output))['oracle_outcome'], 'normal')
        self.assertEqual(classify(record('109725', output.replace('3.5000\t3.5000', '7.0000\t3.5000')))['oracle_outcome'], 'abnormal')

    def test_two_prepared_executions(self):
        output = 'result\n1\n1\nresult\nNULL\nNULL\nVERSION()\n8.0.32\n'
        self.assertEqual(classify(record('110847', output))['oracle_outcome'], 'abnormal')

    def test_window_plus_one(self):
        one = 'A\tAplus\tB\tBplus\n' + '6\t7\t12\t13\n' * 12
        self.assertEqual(classify(record('110983', one + one))['oracle_outcome'], 'normal')
        self.assertEqual(classify(record('110983', one + one.replace('6\t7', '6\t2')))['oracle_outcome'], 'abnormal')

    def test_procedure_sum(self):
        one = '1\t(SUM( 1 ) OVER()) + 0\n1\t1\nid\n1\n'
        self.assertEqual(classify(record('112231', one + one))['oracle_outcome'], 'normal')
        self.assertEqual(classify(record('112231', one + one.replace('1\t1\n', '1\t2\n')))['oracle_outcome'], 'abnormal')

    def test_case_identity(self):
        self.assertEqual(classify(record('112460', 'c_0\tc_1\nNULL\tNULL\nc_0\tc_1\nNULL\t17.61\n'))['oracle_outcome'], 'abnormal')

    def test_timestamp_identity_not_fixed_platform_value(self):
        self.assertEqual(classify(record('112524', 'c_6\n0\nc_6\n0\n'))['oracle_outcome'], 'normal')
        self.assertEqual(classify(record('112524', 'c_6\nNULL\nc_6\n0\n'))['oracle_outcome'], 'abnormal')

    def test_empty_result_permitted_with_or_without_header(self):
        for output in ('', 'ref0\n'):
            self.assertEqual(classify(record('118625', output))['oracle_outcome'], 'normal')
        self.assertEqual(classify(record('118625', 'ref0\n1\n'))['oracle_outcome'], 'abnormal')

    def test_pipes_mode_is_prerequisite(self):
        self.assertEqual(classify(record('119670'))['oracle_outcome'], 'inconclusive')
        self.assertEqual(classify(record('119670', sql_mode='PIPES_AS_CONCAT'))['oracle_outcome'], 'inconclusive')
        self.assertEqual(classify(record('119670', sql_mode='STRICT_TRANS_TABLES'))['oracle_outcome'], 'normal')
        self.assertEqual(classify(record('119670', 'c0\n0\n', sql_mode=''))['oracle_outcome'], 'abnormal')

    def test_time_type_difference_not_asserted_wrong_result(self):
        r = classify(record('120849', 'vc\n141:54:33\nvc\n141:54:33\n'))
        self.assertEqual(r['oracle_outcome'], 'inconclusive')
        self.assertEqual(r['oracle_kind'], 'semantic_difference_needs_review')

    def test_elt_null_propagation(self):
        output = 'ELT(4294967297,1,2,3) IS NULL\tELT(4294967297,1,2,3)+0\tELT(4294967297,1,2,3)|0\tELT(4294967297,1.1,1.2,1.3)+0\tELT(4,1,2,3)+0\n1\tNULL\tNULL\tNULL\tNULL\nELT(n,a,b,c) IS NULL\tELT(n,a,b,c)+0\n1\tNULL\nSUM(ELT(n,a,b,c))\nNULL\n'
        self.assertEqual(classify(record('121512', output))['oracle_outcome'], 'normal')
        self.assertEqual(classify(record('121512', output.replace('1\tNULL', '1\t10')))['oracle_outcome'], 'abnormal')

    def test_gis_bounds(self):
        output = 'ST_AsText(ST_PointN(...,3))\tST_AsText(ST_PointN(...,4294967297))\nNULL\tNULL\nST_AsText(ST_GeometryN(...))\nNULL\n'
        self.assertEqual(classify(record('121523', output))['oracle_outcome'], 'normal')
        self.assertEqual(classify(record('121523', output.replace('NULL\tNULL', 'NULL\tPOINT(0 0)')))['oracle_outcome'], 'abnormal')

    def test_unrecognized_header_not_silent_abnormal(self):
        self.assertEqual(classify(record('118625', 'unexpected\n1\n'))['oracle_outcome'], 'inconclusive')

    def test_stability_requires_three_unique_repeats(self):
        records = [record('118625', repeat=i, cohort='new', target_version='8.0.32', role='target') for i in (1, 1, 2)]
        summary = classify_all(records)
        self.assertFalse(summary['stability'][0]['three_repeats_complete'])
        self.assertIsNone(summary['summary']['independent_root_causes'])

    def test_candidate_pair_matches_target_adjacent_and_requires_script(self):
        records = []
        for role in ('target', 'adjacent_comparison'):
            for rep in (1, 2, 3):
                r = record('118625', 'ref0\n1\n' if role == 'target' else '', repeat=rep,
                           cohort='candidate_replay', role=role, target_version='8.0.32', script_sha256='frozen-case')
                if role == 'adjacent_comparison':
                    r.update(requested_version='8.0.31', actual_version='8.0.31')
                records.append(r)
        pair = classify_all(records)['candidate_version_pairs'][0]
        self.assertEqual(pair['observation'], 'release_behavior_difference')
        self.assertTrue(pair['needs_environment_comparability_review'])
        self.assertIsNone(pair['introducing_commit'])
        records[0]['script_sha256'] = 'different-case'
        self.assertEqual(classify_all(records)['candidate_version_pairs'][0]['observation'], 'inconclusive')

    def test_frozen_manifest_has_44_candidate_pairs(self):
        manifest_path = Path(__file__).resolve().parents[1] / 'experiments/saved_20261029/execution/batches/mysql_replay_20261028_a/batch_manifest.json'
        if not manifest_path.is_file():
            self.skipTest('Integration fixture not bundled')
        manifest = json.loads(manifest_path.read_text(encoding='utf8'))
        records = []
        for case in manifest['cases']:
            for run in case['runs']:
                r = dict(run, report_id=case['report_id'], script_sha256=case['script_sha256'],
                         actual_version=run['requested_version'], execution_status='blocked',
                         returncode=None, stdout='', stderr='Not executed: integration fixture')
                records.append(r)
        result = classify_all(records)
        self.assertEqual(len(records), 399)
        self.assertEqual(len(result['candidate_version_pairs']), 44)
        self.assertTrue(all(p['three_repeats_per_role'] for p in result['candidate_version_pairs']))
        self.assertTrue(all(p['observation'] == 'inconclusive' for p in result['candidate_version_pairs']))


if __name__ == '__main__':
    unittest.main()
