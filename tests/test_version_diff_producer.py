import unittest

import version_diff_producer as producer


class VersionDiffProducerTests(unittest.TestCase):
    def test_builds_complete_ordered_session_scripts(self):
        candidate = {
            "execution_mode": "serial",
            "session_order": ["s2", "s1"],
            "configuration": [{"session": "s2", "sql": "SET SESSION sql_mode='';"}],
            "setup": [
                {"session": "s1", "sql": "CREATE TABLE t(a INT);"},
                {"session": "s2", "sql": "INSERT INTO t VALUES (1);"},
            ],
            "operations": [
                {"session": "s2", "sql": "SELECT * FROM t;"},
                {"session": "s1", "sql": "SELECT COUNT(*) FROM t;"},
            ],
            "cleanup": [{"session": "s1", "sql": "DROP TABLE t;"}],
        }

        scripts = producer.build_session_sqls(candidate, "case_db")

        self.assertEqual(list(scripts), ["s2", "s1"])
        self.assertIn("USE `case_db`;", scripts["s2"])
        self.assertLess(scripts["s2"].index("SET SESSION"), scripts["s2"].index("INSERT INTO"))
        self.assertLess(scripts["s2"].index("INSERT INTO"), scripts["s2"].index("SELECT *"))
        self.assertLess(scripts["s1"].index("CREATE TABLE"), scripts["s1"].index("COUNT(*)"))
        self.assertIn("DROP TABLE t;", scripts["s1"])

    def test_rejects_concurrency_instead_of_serializing_it(self):
        with self.assertRaisesRegex(producer.UnsupportedCandidate, "concurrent"):
            producer.build_session_sqls({"execution_mode": "concurrent", "session_order": ["s1"]}, "case_db")

    def test_configuration_must_reference_a_declared_session(self):
        candidate = {"session_order": ["s1"], "configuration": [
            {"session": "s2", "sql": "SET SESSION sql_mode='';"}],
        }
        with self.assertRaisesRegex(ValueError, "undeclared session"):
            producer.build_session_sqls(candidate, "case_db")

    def test_rejects_server_level_configuration(self):
        candidate = {"session_order": ["s1"], "configuration": [
            {"session": "s1", "sql": "SET GLOBAL sql_mode='';"}]}
        with self.assertRaisesRegex(producer.UnsupportedCandidate, "session-scoped"):
            producer.build_session_sqls(candidate, "case_db")

    def test_result_comparison_ignores_row_order_but_preserves_duplicates(self):
        parent = self.result(stdout="a\nb\n")
        target = self.result(stdout="b\na\n")
        reordered = producer.classify_diff(parent, target)
        self.assertFalse(reordered["version_diff_observed"])
        self.assertTrue(reordered["row_order_differs"])

        duplicate = producer.classify_diff(self.result(stdout="a\na\n"), self.result(stdout="a\n"))
        self.assertTrue(duplicate["result_set_diff"])

    def test_connection_and_timeout_are_excluded(self):
        connection = self.result(connection_failed=True)
        result = producer.classify_diff(connection, self.result())
        self.assertFalse(result["version_diff_observed"])
        self.assertTrue(result["excluded"].startswith("connection_failure"))

        timeout = producer.classify_diff(self.result(timed_out=True), self.result())
        self.assertFalse(timeout["version_diff_observed"])
        self.assertTrue(timeout["excluded"].startswith("timeout"))

        cleanup = producer.classify_diff(self.result(cleanup_failed=True), self.result())
        self.assertFalse(cleanup["version_diff_observed"])
        self.assertTrue(cleanup["excluded"].startswith("cleanup_pending"))

    def test_error_and_crash_differences_are_separate(self):
        error = producer.classify_diff(
            self.result(returncode=1, stderr="ERROR 1054 (42S22): unknown column"),
            self.result(returncode=1, stderr="ERROR 1146 (42S02): missing table"),
        )
        self.assertEqual(error["diff_types"], ["error_diff"])

        crash = producer.classify_diff(self.result(server_crashed=True, returncode=1), self.result())
        self.assertIn("crash_diff", crash["diff_types"])

    @staticmethod
    def result(**updates):
        value = dict(startup_failed=False, connection_failed=False, preparation_failed=False,
                     cleanup_failed=False,
                     timed_out=False, server_crashed=False, returncode=0, stdout="", stderr="")
        value.update(updates)
        return value


if __name__ == "__main__":
    unittest.main()
