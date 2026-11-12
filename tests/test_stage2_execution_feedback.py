"""Offline tests for the Stage2 execution-feedback adapter."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


MODULE_PATH = Path(__file__).resolve().parents[1] / "experiments" / "stage1_source_material_20261107" / "two_stage_execution_feedback_20261112" / "feedback_pipeline.py"
spec = importlib.util.spec_from_file_location("stage2_feedback", MODULE_PATH)
feedback = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(feedback)


class Stage2ExecutionFeedbackTests(unittest.TestCase):
    def make_run(self, with_observation=True):
        temp = tempfile.TemporaryDirectory()
        run = Path(temp.name) / "run_demo"
        (run / "server_evidence" / "results" / "sql_1" / "parent").mkdir(parents=True)
        (run / "server_evidence" / "results" / "sql_1" / "target").mkdir(parents=True)
        (run / "sql_1.sql").write_text("SELECT 'sensitive';\n", encoding="utf-8")
        comparison = {
            "case": "sql_1",
            "parent_revision": "p" * 40,
            "target_revision": "t" * 40,
            "comparisons": [{"repeat": 1, "status": "observed_difference"}],
        }
        result = {
            "revision": "p" * 40,
            "trials": [{"repeat": 1, "returncode": 0, "sql_errors": [], "xml_parse": "ok"}],
        }
        (run / "server_evidence" / "results" / "sql_1" / "comparison.json").write_text(json.dumps(comparison), encoding="utf-8")
        (run / "server_evidence" / "results" / "sql_1" / "parent" / "result.json").write_text(json.dumps(result), encoding="utf-8")
        result["revision"] = "t" * 40
        (run / "server_evidence" / "results" / "sql_1" / "target" / "result.json").write_text(json.dumps(result), encoding="utf-8")
        observations = None
        if with_observation:
            (run / "path_trace.json").write_text("{\"function\":\"parse_expression\"}\n", encoding="utf-8")
            (run / "oracle.json").write_text("{\"expected\":\"one row\",\"observed\":\"zero rows\"}\n", encoding="utf-8")
            observations = run / "observations.json"
            observations.write_text(json.dumps({"cases": [{
                "candidate_id": "sql_1",
                "path": {"status": "confirmed", "object": "Item_string", "source_location": "sql/item.cc:3464", "branch": "QT_TO_ARGUMENT_CHARSET", "evidence_files": ["path_trace.json"]},
                "oracle": {"status": "anomaly", "expected": "one row", "observed": "zero rows", "evidence_files": ["oracle.json"]},
                "attribution": {"status": "unverified"},
            }]}), encoding="utf-8")
        return temp, run, observations

    def test_verified_path_and_anomaly_are_backfilled(self):
        temp, run, observations = self.make_run()
        self.addCleanup(temp.cleanup)
        output = Path(temp.name) / "feedback"
        value = feedback.collect(run, output, observations)
        self.assertEqual(len(value["examples"]), 1)
        self.assertEqual(value["examples"][0]["labels"], ["PATH_REACHED", "ANOMALY_OBSERVED"])
        self.assertEqual(value["examples"][0]["sql"], "SELECT 'sensitive';\n")
        self.assertEqual(value["examples"][0]["path_evidence"]["evidence_files"][0]["path"], "path_trace.json")
        self.assertEqual(value["examples"][0]["outcome_evidence"]["evidence_files"][0]["path"], "oracle.json")

    def test_parent_target_difference_without_oracle_is_excluded(self):
        temp, run, observations = self.make_run(with_observation=False)
        self.addCleanup(temp.cleanup)
        value = feedback.collect(run, Path(temp.name) / "feedback", observations)
        self.assertEqual(value["examples"], [])
        self.assertIn("discrepancy", value["excluded"][0]["reason"])

    def test_prepare_replaces_both_placeholders_and_preserves_two_stages(self):
        temp, run, observations = self.make_run()
        self.addCleanup(temp.cleanup)
        feedback_dir = Path(temp.name) / "feedback"
        feedback.collect(run, feedback_dir, observations)
        stage1 = Path(temp.name) / "stage1.txt"
        stage1.write_text("Stage 1 handoff\n", encoding="utf-8")
        prepared = Path(temp.name) / "next_stage2"
        template_dir = MODULE_PATH.parent
        feedback.prepare(template_dir, stage1, feedback_dir / "feedback.json", prepared, None)
        prompt = (prepared / "stage2_prompt.txt").read_text(encoding="utf-8")
        self.assertNotIn("{{STAGE1_OUTPUT}}", prompt)
        self.assertNotIn("{{EXECUTION_FEEDBACK}}", prompt)
        self.assertIn("Stage 1 handoff", prompt)
        self.assertIn("ANOMALY_OBSERVED", prompt)
        self.assertIn("five target SQL", prompt)
        request = json.loads((prepared / "stage2_request.json").read_text(encoding="utf-8"))
        self.assertEqual(request["model"], "deepseek-v4-flash")
        self.assertEqual(len(request["messages"]), 1)


if __name__ == "__main__":
    unittest.main()
