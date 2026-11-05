"""Local Git fixtures verify source enrichment, never database behavior."""
from copy import deepcopy
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import commit_context as context
import commit_pipeline as cp
from test_commit_pipeline import FakeClient, fixture_analysis


class ContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.base = Path(cls.tmp.name)
        cls.repo = cls.base / "repo"
        cls.repo.mkdir()
        context.git(cls.repo, "init")
        context.git(cls.repo, "config", "user.name", "Offline Source Test")
        context.git(cls.repo, "config", "user.email", "offline@example.invalid")
        (cls.repo / "sql").mkdir()
        (cls.repo / "mysql-test").mkdir()
        (cls.repo / "sql" / "synthetic.cc").write_text(
            "int synthetic(int n) {\n  return helper(n) > 1;\n}\n", encoding="utf-8")
        (cls.repo / "sql" / "helper.cc").write_text(
            "int helper(int n) {\n  return n + 2;\n}\n\nint caller(int n) {\n  return synthetic(n);\n}\n", encoding="utf-8")
        (cls.repo / "mysql-test" / "answer.cc").write_text(
            "int helper(int n) {\n  return 999;\n}\n", encoding="utf-8")
        context.git(cls.repo, "add", ".")
        context.git(cls.repo, "commit", "-m", "synthetic parent")
        cls.parent = context.git(cls.repo, "rev-parse", "HEAD").strip()
        (cls.repo / "sql" / "synthetic.cc").write_text(
            "int synthetic(int n) {\n  return helper(n) >= 1;\n}\n", encoding="utf-8")
        (cls.repo / "sql" / "added.h").write_text("int newly_added(int n) {\n  return n;\n}\n", encoding="utf-8")
        (cls.repo / "mysql-test" / "answer.cc").write_text("int known_answer() { return 888; }\n", encoding="utf-8")
        context.git(cls.repo, "add", ".")
        context.git(cls.repo, "commit", "-m", "synthetic target")
        cls.target = context.git(cls.repo, "rev-parse", "HEAD").strip()
        (cls.repo / "sql" / "helper.cc").write_text("int helper(int n) { return 777; }\n", encoding="utf-8")
        context.git(cls.repo, "commit", "-am", "later change must not leak")
        cls.material = cp.prepare(cls.repo, cls.target, None, cls.base / "material.json")

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def requests(self, kind="definition", symbol="helper"):
        return dict(material_status="insufficient", missing_materials=[dict(
            request_id="req1", kind=kind, revision="both", path=None, symbol=symbol,
            needed="callee/caller context", reason="Map change to candidate SQL")])

    def test_auto_prepare_records_locations_module_and_function_hints(self):
        material = self.material
        cp.validate_material(material)
        self.assertEqual(material["context_selection"], "automatic_changed_regions")
        files = {f["path"]: f for f in material["commit_metadata"]["files"]}
        self.assertEqual(set(files), {"sql/synthetic.cc", "sql/added.h"})
        target = files["sql/synthetic.cc"]
        self.assertEqual(target["modification_locations"][0]["before"], {"start_line": 2, "line_count": 1})
        self.assertEqual(target["database_module"]["value"], "sql_server")
        self.assertEqual(target["database_module"]["certainty"], "heuristic")
        self.assertEqual({f["name"] for f in target["related_functions"]}, {"synthetic"})
        self.assertEqual(files["sql/added.h"]["change_type"]["file_operation"], "added")
        self.assertTrue(material["commit_metadata"]["excluded_files"])
        self.assertFalse(any("mysql-test" in s["path"] for s in material["sources"]))

    def test_definition_supplement_reads_frozen_revisions_not_head_or_tests(self):
        original = deepcopy(self.material)
        enriched = context.supplement(self.repo, self.material, self.requests())
        self.assertEqual(self.material, original)
        added = enriched["sources"][len(original["sources"]):]
        self.assertEqual({s["revision"] for s in added}, {self.parent, self.target})
        self.assertTrue(all(s["path"] == "sql/helper.cc" for s in added))
        self.assertTrue(all("n + 2" in s["content"] for s in added))
        self.assertFalse(any("777" in s["content"] or "999" in s["content"] for s in added))
        self.assertEqual(enriched["supplementation"]["semantic_sufficiency"], "requires_stage1_reanalysis")
        cp.validate_material(enriched)

    def test_callers_are_lexical_candidates_and_unknown_requests_stay_unresolved(self):
        enriched = context.supplement(self.repo, self.material, self.requests("callers", "synthetic"))
        added = enriched["sources"][len(self.material["sources"]):]
        self.assertTrue(any("caller(" in s["content"] for s in added))
        self.assertTrue(all(s["retrieval"]["relation"] == "lexical_call_site_candidate" for s in added))
        request = self.requests("unknown", None)
        unresolved = context.supplement(self.repo, self.material, request)
        self.assertEqual(unresolved["supplementation"]["outcomes"][0]["status"], "unresolved")

    def test_range_and_budget_are_explicit_and_missing_symbol_is_not_resolved(self):
        request = self.requests("source_range", None)
        request["missing_materials"][0].update(path="sql/helper.cc", start_line=1, end_line=7)
        enriched = context.supplement(self.repo, self.material, request, max_lines=2)
        self.assertEqual(len(enriched["supplementation"]["new_source_ids"]), 1)
        self.assertTrue(enriched["sources"][-1]["retrieval"]["truncated"])
        self.assertEqual(enriched["supplementation"]["outcomes"][0]["status"], "partial")
        missing = context.supplement(self.repo, self.material, self.requests(symbol="not_here"))
        self.assertEqual(missing["supplementation"]["outcomes"][0]["status"], "unresolved")

    def test_requests_exclude_tests_later_revisions_and_unbounded_paths(self):
        for field, value in (("path", "mysql-test/answer.cc"), ("path", "../helper.cc"), ("revision", "HEAD")):
            request = self.requests()
            request["missing_materials"][0][field] = value
            with self.assertRaises(ValueError):
                context.validate_requests(request)
        request = self.requests()
        request["material_status"] = "sufficient"
        with self.assertRaises(ValueError):
            context.validate_requests(request)

    def test_multiline_functions_ignore_braces_in_comments_and_literals(self):
        source = 'bool\nWidget::check(\n int n\n) const {\n // }\n const char *s = "}";\n if (n) { return true; }\n return false;\n}\n'
        functions = context.functions(source)
        self.assertEqual([f["name"] for f in functions], ["Widget::check"])
        self.assertEqual(functions[0]["start_line"], 1)
        self.assertEqual(functions[0]["end_line"], 9)

    def test_insufficient_to_supplement_to_new_analysis_keeps_original_run(self):
        run = self.base / "source_run"
        with mock.patch.object(cp, "git", wraps=cp.git):
            cp.initialize(self.base / "material.json", run, "source_run")
        analysis = fixture_analysis()
        analysis.update(version=self.material["version"], target_revision=self.target, parent_revision=self.parent,
                        **self.requests())
        analysis["changes"][0]["facts"] = []
        response = cp.step(run, True, FakeClient(analysis))
        self.assertEqual(response["status"], "accepted")
        original_hash = cp.file_hash(run / "material.json")
        output = self.base / "enriched.json"
        result = cp.supplement_run(run, self.repo, output)
        self.assertEqual(result["new_source_count"], 2)
        self.assertEqual(cp.file_hash(run / "material.json"), original_hash)
        fresh = self.base / "source_run_enriched"
        cp.initialize(output, fresh, "source_run_enriched")
        self.assertTrue((fresh / "analysis" / "request.json").exists())
        self.assertFalse((fresh / "analysis" / "response.json").exists())
        enriched = cp.read(output)
        self.assertEqual(enriched["supplementation"]["parent_run_id"], "source_run")
