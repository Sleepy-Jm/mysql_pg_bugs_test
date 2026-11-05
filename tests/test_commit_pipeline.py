"""Synthetic offline acceptance tests; no DeepSeek or database is contacted."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock

import commit_pipeline as cp


def fixture_material():
    content = "-  return n > 1;\n+  return n >= 1;\n"
    return dict(workflow="commit_analysis_v1", target_revision="a" * 40, parent_revision="b" * 40,
                version="unknown", commit_role="unknown", sources=[
                    dict(source_id="diff", kind="production_diff", path="sql/synthetic.cc",
                         revision="a" * 40, start_line=1, content=content,
                         content_sha256=hashlib.sha256(content.encode()).hexdigest())])


def fixture_analysis():
    return dict(version="unknown", target_revision="a" * 40, parent_revision="b" * 40,
        material_status="sufficient", missing_materials=[],
        changes=[dict(change_id="comparison", change_type="comparison_boundary", module="synthetic",
        locations=[dict(path="sql/synthetic.cc", functions=["synthetic"])], applicability="sql",
        reason="Synthetic condition for offline control flow testing, not a MySQL claim",
        facts=[dict(text="Comparison operator changed", evidence=[
            dict(source_id="diff", start_line=1, end_line=2, quote="-  return n > 1;\n+  return n >= 1;")])],
        affected_features=["unknown"], conditions=[
            dict(condition_id="rows", kind="data", status="hypothesis", description="Use one row", evidence=[])],
        unknowns=["SQL-to-source reachability unproven"])], unknowns=[])


def fixture_candidates(count=1, offset=0):
    return dict(candidates=[dict(candidate_id=f"seed_{i}", condition_ids=["rows"], execution_mode="serial",
        setup=[dict(session="s1", sql=f"CREATE TABLE t{i}(a INT); INSERT INTO t{i} VALUES ({offset+i});", condition_ids=["rows"])],
        operations=[dict(session="s1", sql=f"SELECT a FROM t{i};", condition_ids=["rows"])],
        cleanup=[dict(session="s1", sql=f"DROP TABLE t{i};", condition_ids=[])],
        configuration=[], session_order=["s1"], expected_observations=[
            dict(condition_id="rows", description="instrumented event; not measured by generation")],
        proposed_oracle=dict(description=f"one row {offset+i}", derivation="literal input"),
        capability_gaps=[]) for i in range(count)],
        shortfall_reasons=[] if count == 10 else ["Synthetic test intentionally emits a short batch"])


def fixture_contract(kind="target"):
    return dict(contract_id=kind, kind=kind, method="branch_coverage" if kind == "target" else "independent_expected",
                producer_sha256="c" * 64, description="Synthetic fixture predicate",
                evidence_basis="Synthetic test producer only; not a real experiment",
                pointer="/measurements/positive", operator="eq", expected=True)


class FakeClient:
    def __init__(self, response, model="deepseek-v4-pro", available=True):
        self.response, self.model, self.available = response, model, available
        self.calls = []

    def call(self, endpoint, payload=None):
        self.calls.append(endpoint)
        if endpoint == "models":
            return {"data": [{"id": self.model}] if self.available else []}
        return dict(model=self.model, created=0, id="synthetic-test", usage={"total_tokens": 0},
                    choices=[dict(finish_reason="stop", message={"content": json.dumps(self.response)})])


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.run = self.base / "run"
        cp.write(self.base / "material.json", fixture_material())
        cp.write(self.base / "contracts.json", [fixture_contract(), fixture_contract("oracle")])
        with mock.patch.object(cp, "git", return_value=""):
            cp.initialize(self.base / "material.json", self.run, "synthetic", self.base / "contracts.json")

    def analyze(self):
        result = cp.step(self.run, True, FakeClient(fixture_analysis()))
        self.assertEqual(result["status"], "accepted")

    def generate(self, count=1):
        result = cp.step(self.run, True, FakeClient(fixture_candidates(count)))
        self.assertEqual(result["status"], "accepted")
        return result

    def evidence(self, number=1, hit=True, anomaly=False, execution="completed"):
        seed = cp.read(self.run / "rounds" / f"{number:02d}" / "candidates.json")["candidates"][0]
        folder = self.base / f"external_{number}"
        folder.mkdir()
        cp.write(folder / "raw.json", {"synthetic_only": True, "stdout": "fixture"})
        raw = {"path": "raw.json", "sha256": cp.file_hash(folder / "raw.json")}
        binding = dict(run_id="synthetic", round=number, candidate_id=seed["candidate_id"],
                       candidate_sha256=cp.digest(seed), actual_revision="a" * 40)
        obs = dict(candidate_id=seed["candidate_id"], candidate_sha256=cp.digest(seed),
            execution=dict(status=execution, actual_revision="a" * 40,
                           environment={"synthetic": True}, command=["synthetic"],
                           runner_sha256="d" * 64, observed_at=cp.now(), evidence=raw),
            validity="valid", reason="Synthetic external evidence fixture")
        for kind, positive in (("target", hit), ("oracle", anomaly)):
            c = fixture_contract(kind)
            artifact = dict(**binding, contract_id=kind, method=c["method"],
                            producer_sha256=c["producer_sha256"], observed_at=cp.now(),
                            raw_evidence=[raw], measurements={"positive": positive})
            cp.write(folder / f"{kind}.json", artifact)
            obs[kind] = dict(contract_id=kind, evidence={"path": f"{kind}.json",
                                                       "sha256": cp.file_hash(folder / f"{kind}.json")})
        path = folder / "observations.json"
        cp.write(path, dict(run_id="synthetic", round=number, observations=[obs]))
        return path

    def test_default_preview_never_calls_network(self):
        with mock.patch.object(cp.DeepSeek, "call", side_effect=AssertionError("network")):
            self.assertFalse(cp.step(self.run)["model_called"])
        self.assertFalse((self.run / "analysis" / "attempt.json").exists())

    def test_source_quote_line_and_evidence_level(self):
        value = fixture_analysis()
        cp.validate_analysis(value, fixture_material())
        value["changes"][0]["facts"][0]["evidence"][0]["quote"] = "invented"
        with self.assertRaisesRegex(ValueError, "quote"):
            cp.validate_analysis(value, fixture_material())
        value = fixture_analysis()
        value["changes"][0]["conditions"][0]["status"] = "source_supported"
        with self.assertRaisesRegex(ValueError, "citation"):
            cp.validate_analysis(value, fixture_material())

    def test_analysis_needs_no_model_role_classification(self):
        cp.validate_analysis(fixture_analysis(), fixture_material())
        value = fixture_analysis()
        value.update(commit_status="fix", commit_status_reason="Legacy model judgment")
        original = deepcopy(value)
        cp.validate_analysis(value, fixture_material())
        view = cp.requirements_view(value)
        self.assertNotIn("commit_status", view)
        self.assertNotIn("commit_status_reason", view)
        self.assertEqual(value, original)

    def test_input_role_reaches_stage2_despite_legacy_model_judgment(self):
        material = fixture_material()
        material["commit_role"] = "introduce"
        cp.write(self.base / "manual_material.json", material)
        run = self.base / "manual_role_run"
        with mock.patch.object(cp, "git", return_value=""):
            cp.initialize(self.base / "manual_material.json", run, "manual_role")
        first = cp.read(run / "analysis/request.json")
        shape = json.loads(first["messages"][1]["content"])["output_shape"]
        self.assertNotIn("commit_status", shape)
        self.assertNotIn("commit_status_reason", shape)
        legacy = fixture_analysis()
        legacy.update(commit_status="fix", commit_status_reason="Legacy model judgment")
        self.assertEqual(cp.step(run, True, FakeClient(legacy))["status"], "accepted")
        cp.step(run)
        second = cp.read(run / "rounds/01/request.json")
        payload = json.loads(second["messages"][1]["content"])
        self.assertEqual(payload["commit_role"], "introduce")
        self.assertEqual(payload["commit_role_source"], "input_annotation")
        self.assertNotIn("commit_status", payload["analysis"])
        self.assertNotIn("commit_status_reason", payload["analysis"])
        self.assertEqual(cp.read(run / "analysis/analysis.json")["commit_status"], "fix")

    def test_stage2_receives_analysis_not_raw_sources(self):
        self.analyze()
        cp.step(self.run)
        request = cp.read(self.run / "rounds" / "01" / "request.json")
        payload = json.loads(request["messages"][1]["content"])
        self.assertNotIn("material", payload)
        self.assertNotIn("sources", payload)
        self.assertNotIn("quote", payload["analysis"]["changes"][0]["facts"][0]["evidence"][0])
        self.assertIn("quote", cp.read(self.run / "analysis" / "analysis.json")["changes"][0]["facts"][0]["evidence"][0])
        self.assertEqual(payload["requested_candidates"], 10)

    def test_shortfall_preserved_and_not_padded(self):
        self.analyze()
        result = self.generate(2)
        self.assertEqual(result["received_count"], 2)
        self.assertEqual(result["accepted_count"], 2)
        self.assertEqual(cp.report(self.run)["accepted_total"], 2)
        value = fixture_candidates(2)
        value["shortfall_reasons"] = []
        with self.assertRaisesRegex(ValueError, "shortfall"):
            cp.validate_candidates(value, fixture_analysis())

    def test_configuration_requires_supported_session_scoped_sql(self):
        value = fixture_candidates(1)
        value["candidates"][0]["configuration"] = [
            dict(session="s1", sql="SET SESSION sql_mode = '';")]
        cp.validate_candidates(value, fixture_analysis())
        value["candidates"][0]["configuration"] = [
            dict(session="s1", sql="SET GLOBAL sql_mode = '';")]
        with self.assertRaisesRegex(ValueError, "session-scoped SET"):
            cp.validate_candidates(value, fixture_analysis())

    def test_unknown_links_over_budget_and_duplicate_rejected(self):
        for change in ("link", "over", "duplicate"):
            value = fixture_candidates(11 if change == "over" else 2)
            if change == "link":
                value["candidates"][0]["condition_ids"] = ["missing"]
            elif change == "duplicate":
                value["candidates"][1] = deepcopy(value["candidates"][0])
                value["candidates"][1]["candidate_id"] = "different_id"
            with self.assertRaises(ValueError):
                cp.validate_candidates(value, fixture_analysis())

    def test_model_unavailable_is_not_run_and_no_completion(self):
        client = FakeClient({}, available=False)
        result = cp.step(self.run, True, client)
        self.assertEqual(client.calls, ["models"])
        self.assertEqual(result["candidate_generation"], "not_run")
        self.assertFalse(result["database_executed"])
        self.assertEqual(result["status"], "failed")
        with self.assertRaises(ValueError):
            cp.step(self.run, True, client)

    def test_model_mismatch_keeps_raw_without_accepting(self):
        client = FakeClient(fixture_analysis())
        original = client.call
        def call(endpoint, payload=None):
            raw = original(endpoint, payload)
            if endpoint == "chat/completions":
                raw["model"] = "other-model"
            return raw
        client.call = call
        result = cp.step(self.run, True, client)
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["returned_model"], "other-model")
        self.assertTrue((self.run / "analysis" / "response.json").exists())
        self.assertFalse((self.run / "analysis" / "analysis.json").exists())

    def test_truncated_response_is_not_accepted(self):
        client = FakeClient(fixture_analysis())
        original = client.call
        def call(endpoint, payload=None):
            raw = original(endpoint, payload)
            if endpoint == "chat/completions":
                raw["choices"][0]["finish_reason"] = "length"
            return raw
        client.call = call
        result = cp.step(self.run, True, client)
        self.assertEqual(result["status"], "failed")
        self.assertIn("truncated", result["reason"])

    def test_non_sql_analysis_does_not_force_generation(self):
        analysis = fixture_analysis()
        analysis["changes"][0]["applicability"] = "not_sql"
        analysis["changes"][0]["conditions"] = []
        cp.step(self.run, True, FakeClient(analysis))
        client = FakeClient({})
        result = cp.step(self.run, True, client)
        self.assertEqual(result["status"], "no_applicable_conditions")
        self.assertEqual(client.calls, [])
        self.assertEqual(cp.report(self.run)["requested_total"], 0)

    def test_insufficient_material_waits_for_source_not_sql_generation(self):
        analysis = fixture_analysis()
        analysis.update(material_status="insufficient", missing_materials=[dict(
            request_id="caller", kind="callers", revision="both", path=None, symbol="synthetic",
            needed="SQL entry caller", reason="Cannot map condition to SQL")])
        cp.step(self.run, True, FakeClient(analysis))
        client = FakeClient({})
        result = cp.step(self.run, True, client)
        self.assertEqual(result["status"], "awaiting_source_material")
        self.assertEqual(client.calls, [])
        self.assertFalse((self.run / "rounds").exists())

    def test_explicit_model_probe_is_discovery_not_generation(self):
        client = FakeClient({})
        result = cp.probe_models(self.base / "models.json", client=client)
        self.assertEqual(result["status"], "available")
        self.assertFalse(result["generation_called"])
        self.assertEqual(client.calls, ["models"])

    def test_interrupted_attempt_is_unknown_not_success(self):
        cp.write(self.run / "analysis" / "attempt.json", {"started_at": cp.now()})
        self.assertEqual(cp.report(self.run)["stage1"]["status"], "interrupted_unknown")
        with self.assertRaisesRegex(ValueError, "Attempt already exists"):
            cp.step(self.run, True, FakeClient(fixture_analysis()))

    def test_transport_failure_recorded_without_fake_sql(self):
        client = FakeClient({})
        original = client.call
        def call(endpoint, payload=None):
            if endpoint == "chat/completions":
                raise RuntimeError("transport failure")
            return original(endpoint, payload)
        client.call = call
        result = cp.step(self.run, True, client)
        self.assertEqual(result["failure_phase"], "completion")
        self.assertEqual(result["remote_completion"], "unknown")
        self.assertEqual(result["accepted_count"], 0)

    def test_feedback_requires_previous_round_record(self):
        self.analyze()
        self.generate()
        with self.assertRaisesRegex(ValueError, "preceding round feedback"):
            cp.step(self.run)

    def test_only_previous_round_hit_is_reused_then_fallback(self):
        self.analyze()
        self.generate()
        feedback = cp.record_feedback(self.run, 1, self.evidence(hit=True))
        self.assertEqual(feedback["records"][0]["target_status"], "hit")
        self.assertEqual(feedback["records"][0]["oracle_status"], "no_anomaly")
        self.assertEqual(feedback["records"][0]["bug_status"], "not_adjudicated")
        cp.step(self.run)
        selected = cp.read(self.run / "rounds" / "02" / "selection.json")
        self.assertEqual(selected["example_ids"], ["seed_0"])
        self.generate()
        cp.record_feedback(self.run, 2, self.evidence(2, hit=False))
        cp.step(self.run)
        selected = cp.read(self.run / "rounds" / "03" / "selection.json")
        self.assertEqual(selected["example_ids"], [])
        self.assertEqual(selected["reason"], "previous_round_no_verified_hit_default")

    def test_no_observation_is_not_a_miss(self):
        self.analyze()
        self.generate()
        feedback = cp.record_feedback(self.run, 1)
        self.assertEqual(feedback["records"][0]["target_status"], "not_run")
        self.assertEqual(feedback["records"][0]["validity"], "unknown")

    def test_execution_success_without_target_evidence_is_unobservable(self):
        self.analyze()
        self.generate()
        path = self.evidence()
        value = cp.read(path)
        del value["observations"][0]["target"]
        path.write_text(json.dumps(value), encoding="utf-8")
        feedback = cp.record_feedback(self.run, 1, path)
        self.assertEqual(feedback["records"][0]["target_status"], "unobservable")
        self.assertEqual(feedback["selected_for_next_round"], [])

    def test_anomaly_without_target_hit_is_not_feedback_or_confirmed_bug(self):
        self.analyze()
        self.generate()
        feedback = cp.record_feedback(self.run, 1, self.evidence(hit=False, anomaly=True))
        self.assertEqual(feedback["records"][0]["oracle_status"], "anomaly_candidate")
        self.assertEqual(feedback["selected_for_next_round"], [])
        self.assertIsNone(cp.report(self.run)["independent_bug_count"])

    def test_hash_revision_producer_and_absent_metric_rejected(self):
        self.analyze()
        self.generate()
        path = self.evidence()
        original_obs = cp.read(path)
        artifact_path = path.parent / "target.json"
        original_artifact = cp.read(artifact_path)
        for field, value in (("actual_revision", "e" * 40), ("producer_sha256", "e" * 64), ("measurements", {})):
            artifact = dict(original_artifact, **{field: value})
            artifact_path.write_text(json.dumps(artifact), encoding="utf-8")
            observations = deepcopy(original_obs)
            observations["observations"][0]["target"]["evidence"]["sha256"] = cp.file_hash(artifact_path)
            path.write_text(json.dumps(observations), encoding="utf-8")
            with self.assertRaises(ValueError):
                cp.record_feedback(self.run, 1, path)
        path.write_text(json.dumps(original_obs), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            cp.record_feedback(self.run, 1, path)

    def test_feedback_cannot_be_relabeled_to_create_hit(self):
        self.analyze()
        self.generate()
        cp.record_feedback(self.run, 1)
        path = self.run / "rounds" / "01" / "feedback.json"
        value = cp.read(path)
        value["records"][0]["target_status"] = "hit"
        path.write_text(json.dumps(value), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Feedback"):
            cp.step(self.run)

    def test_freeze_inputs_and_never_overwrite_runs(self):
        with self.assertRaises(FileExistsError):
            cp.initialize(self.base / "material.json", self.run, "again")
        path = self.run / "contracts.json"
        path.write_text("[]", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Frozen input"):
            cp.step(self.run)

    def test_ten_rounds_are_not_independent_repeats_and_budget_is_exact(self):
        self.analyze()
        for i in range(1, 11):
            self.generate(10)
            cp.record_feedback(self.run, i)
        result = cp.step(self.run)
        self.assertEqual(result["status"], "generation_budget_exhausted")
        self.assertEqual(result["report"]["accepted_total"], 100)
        self.assertEqual(len(result["report"]["rounds"]), 10)
        self.assertFalse((self.run / "rounds" / "11").exists())

    def test_version_difference_contract_accepted(self):
        contract = fixture_contract("oracle")
        contract["method"] = "version_difference"
        contract["kind"] = "target"
        contract["method"] = "version_differential"
        cp.validate_contracts([contract])

    def test_differential_status_selects_only_verified_differences(self):
        contracts = [fixture_contract(), fixture_contract("oracle")]
        contracts[0].update(method="version_differential", pointer="/measurements/version_diff_observed")
        self.assertEqual(cp.next_round_examples([
            dict(candidate_id="oracle_hit", differential_status="no_difference", target_status="hit"),
            dict(candidate_id="version_difference", differential_status="difference", target_status="not_measured"),
        ], contracts), ["version_difference"])
        contracts_path = self.base / "differential_contracts.json"
        cp.write(contracts_path, contracts)
        run = self.base / "differential_run"
        with mock.patch.object(cp, "git", return_value=""):
            cp.initialize(self.base / "material.json", run, "synthetic_diff", contracts_path, rounds=5)
        cp.step(run, True, FakeClient(fixture_analysis()))
        cp.step(run, True, FakeClient(fixture_candidates(3)))
        candidates = cp.read(run / "rounds" / "01" / "candidates.json")["candidates"]
        external = self.base / "differential_observations"
        external.mkdir()
        observations = []
        for seed, (difference, valid) in zip(candidates, ((True, True), (False, True), (False, False))):
            folder = external / seed["candidate_id"]
            folder.mkdir()
            cp.write(folder / "raw.json", {"synthetic_only": True, "stdout": "both revisions"})
            raw = {"path": f"{seed['candidate_id']}/raw.json", "sha256": cp.file_hash(folder / "raw.json")}
            binding = dict(run_id="synthetic_diff", round=1, candidate_id=seed["candidate_id"],
                           candidate_sha256=cp.digest(seed), actual_revision="a" * 40,
                           contract_id="target")
            artifact = dict(**binding, method="version_differential", producer_sha256="c" * 64,
                observed_at=cp.now(), raw_evidence=[raw], measurements={
                    "version_diff_observed": difference, "parent_revision": "b" * 40,
                    "target_revision": "a" * 40})
            cp.write(folder / "measurement.json", artifact)
            obs = dict(candidate_id=seed["candidate_id"], candidate_sha256=cp.digest(seed),
                reason="synthetic paired execution", validity="valid" if valid else "unknown",
                execution=dict(status="completed", actual_revision="a" * 40,
                    environment={"parent_revision": "b" * 40, "target_revision": "a" * 40},
                    command=["synthetic paired runner"], runner_sha256="d" * 64,
                    observed_at=cp.now(), evidence=raw),
                target=dict(contract_id="target", evidence={
                    "path": f"{seed['candidate_id']}/measurement.json",
                    "sha256": cp.file_hash(folder / "measurement.json")}))
            observations.append(obs)
        input_path = external / "observations.json"
        cp.write(input_path, dict(run_id="synthetic_diff", round=1, observations=observations))
        feedback = cp.record_feedback(run, 1, input_path)
        self.assertEqual([r["differential_status"] for r in feedback["records"]],
                         ["difference", "no_difference", "inconclusive"])
        self.assertEqual(feedback["records"][0]["target_status"], "not_measured")
        self.assertEqual(feedback["selected_for_next_round"], ["seed_0"])
        cp.step(run)
        selection = cp.read(run / "rounds" / "02" / "selection.json")
        self.assertEqual(selection["reason"], "previous_round_verified_differences")
        self.assertEqual(selection["example_ids"], ["seed_0"])
        self.assertEqual(cp.report(run)["planned_total"], 50)


class PreparationTests(unittest.TestCase):
    def test_real_local_git_diff_and_ranges_without_checkout(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            repo = folder / "repo"
            repo.mkdir()
            cp.git(repo, "init")
            cp.git(repo, "config", "user.name", "Offline Test")
            cp.git(repo, "config", "user.email", "offline@example.invalid")
            (repo / "sql").mkdir()
            source = repo / "sql" / "synthetic.cc"
            source.write_text("bool f(int n) {\n  return n > 1;\n}\n", encoding="utf-8")
            cp.git(repo, "add", ".")
            cp.git(repo, "commit", "-m", "synthetic parent")
            parent = cp.git(repo, "rev-parse", "HEAD").strip()
            source.write_text("bool f(int n) {\n  return n >= 1;\n}\n", encoding="utf-8")
            cp.git(repo, "commit", "-am", "synthetic boundary change")
            target = cp.git(repo, "rev-parse", "HEAD").strip()
            spec = dict(version="unknown", commit_role="unknown", sources=[
                dict(path="sql/synthetic.cc", role="production", functions=["f"], before=[[1, 3]], after=[[1, 3]])])
            cp.write(folder / "spec.json", spec)
            material = cp.prepare(repo, target, folder / "spec.json", folder / "material.json")
            self.assertEqual(material["parent_revision"], parent)
            self.assertEqual(material["target_revision"], target)
            self.assertEqual({s["kind"] for s in material["sources"]}, {"message", "production_diff", "before", "after"})
            self.assertEqual(cp.git(repo, "rev-parse", "HEAD").strip(), target)
            cp.validate_material(material)


if __name__ == "__main__":
    unittest.main()
