import sys
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from pg_report_version_comparison import compare


class VersionBoundaryTests(unittest.TestCase):
    def test_prior_phenomenon_excludes_target_minor_introduction(self):
        result,_ = compare('reproduced','reproduced','reproduced')
        self.assertIn('不支持目标小版本新引入',result)

    def test_prior_valid_negative_is_only_candidate_interval(self):
        result,_ = compare('not_reproduced','reproduced','reproduced')
        self.assertIn('候选引入区间',result)
        self.assertIn('尚未确认',result)

    def test_failed_or_incomplete_prior_is_never_negative(self):
        for status in ['inconclusive','execution_failed','not_run','other_anomaly']:
            with self.subTest(status=status):
                result,_ = compare(status,'reproduced','not_reproduced')
                self.assertIn('前版证据不足',result)
                self.assertNotIn('候选引入区间',result)

    def test_target_negative_cannot_establish_introduction(self):
        result,_ = compare('not_reproduced','not_reproduced','reproduced')
        self.assertIn('不能判断引入',result)

    def test_following_negative_is_not_confirmed_fix(self):
        _,result = compare('reproduced','reproduced','not_reproduced')
        self.assertIn('未确认修复提交',result)

    def test_following_inconclusive_is_not_disappearance(self):
        _,result = compare('reproduced','reproduced','inconclusive')
        self.assertEqual(result,'')


if __name__=='__main__':
    unittest.main()
