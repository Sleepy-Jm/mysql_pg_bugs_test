"""Independent commit analysis -> candidate seeds. Offline by default.

Explicit models / step --execute-model commands access DeepSeek.
SQL execution is external. Feedback is evaluated against frozen measurement
contracts, never against claims in a model response.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import platform
import re
import subprocess
import sys
import urllib.error
import urllib.request
import commit_context

ROOT = Path(__file__).resolve().parents[2]
PROMPTS = ROOT / "Prompts" / "mysql_commit"
ROUNDS = BATCH_SIZE = 10
ANALYSIS_SHAPE = {
    "version": "copy material.version", "target_revision": "copy material.target_revision",
    "parent_revision": "copy material.parent_revision",
    "material_status": "sufficient|partial|insufficient",
    "missing_materials": [{"request_id": "context_1", "kind": "definition|callers|source_range|unknown",
        "revision": "before|after|both", "path": None, "symbol": "needed_function_or_null",
        "start_line": None, "end_line": None, "needed": "missing source context", "reason": "why needed for a candidate"}],
    "changes": [{"change_id": "change_1", "change_type": "unknown", "module": "unknown",
        "locations": [{"path": "sql/file.cc", "functions": ["unknown"]}],
        "applicability": "sql|not_sql|unknown", "reason": "explain",
        "facts": [{"text": "source-supported change", "evidence": [
            {"source_id": "source_1", "start_line": 1, "end_line": 1, "quote": "exact text"}]}],
        "affected_features": ["possible feature and execution stage"],
        "conditions": [{"condition_id": "condition_1", "kind": "data", "status": "hypothesis",
                        "description": "candidate condition", "evidence": []}],
        "unknowns": ["missing information"]}], "unknowns": []}
CANDIDATE_SHAPE = {
    "candidates": [{"candidate_id": "seed_1", "condition_ids": ["condition_1"], "execution_mode": "serial",
        "setup": [{"session": "s1", "sql": "complete SQL", "condition_ids": ["condition_1"]}],
        "operations": [{"session": "s1", "sql": "complete SQL", "condition_ids": ["condition_1"]}],
        "cleanup": [], "configuration": [{"session": "s1", "sql": "SET SESSION ..."}], "session_order": ["s1"],
        "expected_observations": [{"condition_id": "condition_1", "description": "event to measure"}],
        "proposed_oracle": {"description": "expected result", "derivation": "independent reasoning"},
        "capability_gaps": []}], "shortfall_reasons": []}


def now():
    return datetime.now(timezone.utc).isoformat()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def write(path, value):
    """Never replace a request, response, result or run."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def sha_value(value):
    return isinstance(value, str) and re.fullmatch(r"[a-f0-9]{64}", value) is not None


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          capture_output=True, encoding="utf-8").stdout


def prepare(repo, revision, spec_path, output, parent=None):
    """Discover production changes or use explicit ranges; no checkout."""
    spec = read(spec_path) if spec_path else {"version": "unknown", "commit_role": "unknown"}
    revision = git(repo, "rev-parse", "--verify", revision + "^{commit}").strip()
    parents = git(repo, "show", "-s", "--format=%P", revision).split()
    if parent:
        parent = git(repo, "rev-parse", "--verify", parent + "^{commit}").strip()
    else:
        require(len(parents) == 1, "Root/merge commit requires an explicit direct parent")
        parent = parents[0]
    require(parent in parents, "Selected parent is not a direct parent")
    require(spec.get("commit_role") in {"introduce", "fix", "other", "unknown"}, "commit_role required")
    require(nonempty(spec.get("version")), "version required; unknown is allowed")
    metadata, automatic_sources = commit_context.discover(repo, revision, parent)
    automatic = "sources" not in spec
    entries = automatic_sources if automatic else spec["sources"]
    require(isinstance(entries, list) and entries, "No production sources selected or discovered")
    sources, selected = [], []

    def add(kind, path, rev, start, content):
        sources.append(dict(source_id=f"source_{len(sources) + 1}", kind=kind, path=path,
                            revision=rev, start_line=start, content=content,
                            content_sha256=hashlib.sha256(content.encode()).hexdigest()))

    add("message", "COMMIT_MESSAGE", revision, 1, git(repo, "show", "-s", "--format=%B", revision))
    for original_entry in entries:
        entry = dict(original_entry)
        hint = next((e for e in automatic_sources if e["path"] == entry["path"]), None)
        if not entry.get("functions") or entry["functions"] == ["unknown"]:
            entry["functions"] = hint["functions"] if hint else ["unknown"]
        path = entry["path"]
        p = PurePosixPath(path)
        require(not p.is_absolute() and ".." not in p.parts and not path.startswith("-") and "\\" not in path,
                "Source path must be repository relative")
        require(entry.get("role") in {"production", "helper"}, "Only production/helper source allowed")
        require(not any(x.lower() in {"mysql-test", "tests", "unittest", ".secrets", ".git"} for x in p.parts),
                "Tests/reproducers/secrets are not generation input")
        require(path not in [s["path"] for s in selected], "Duplicate source path")
        require(isinstance(entry.get("functions"), list) and entry["functions"], "Record functions or ['unknown']")
        selected.append(entry)
        patch = git(repo, "diff", "--no-ext-diff", "--no-textconv", "--unified=3", parent, revision, "--", path)
        if patch:
            add("production_diff", path, revision, 1, patch)
        for side, rev in (("before", parent), ("after", revision)):
            ranges = entry.get(side, [])
            require(isinstance(ranges, list), "Source ranges must be a list")
            if not ranges:
                continue
            lines = git(repo, "show", f"{rev}:{path}").splitlines(keepends=True)
            for start, end in ranges:
                require(type(start) is int and type(end) is int and 1 <= start <= end <= len(lines), "Invalid source range")
                add(side, path, rev, start, "".join(lines[start - 1:end]))
    require(any(s["kind"] == "production_diff" for s in sources), "No selected production change")
    material = dict(schema_version=1, workflow="commit_analysis_v1", repository=str(Path(repo).resolve()),
        target_revision=revision, parent_revision=parent, version=spec["version"], commit_role=spec["commit_role"],
        selection=selected, sources=sources, prepared_at=now(), spec_sha256=file_hash(spec_path) if spec_path else None,
        commit_metadata=metadata, context_selection="automatic_changed_regions" if automatic else "explicit_source_ranges",
        input_boundary="message + selected production diff + before/after/helper ranges")
    write(output, material)
    return material


def validate_material(material):
    require(material.get("workflow") == "commit_analysis_v1", "Not commit-analysis material")
    for key in ("target_revision", "parent_revision"):
        require(re.fullmatch(r"[a-f0-9]{40}", material.get(key, "")) is not None, f"Exact {key} required")
    require(nonempty(material.get("version")), "Version metadata required")
    require(material.get("commit_role") in {"introduce", "fix", "other", "unknown"}, "Commit role required")
    ids = []
    for source in material["sources"]:
        ids.append(source["source_id"])
        require(source["kind"] in {"message", "production_diff", "before", "after"}, "Unsupported source kind")
        require(type(source["start_line"]) is int and source["start_line"] > 0, "Invalid source start")
        require(hashlib.sha256(source["content"].encode()).hexdigest() == source["content_sha256"], "Source hash mismatch")
    require(len(ids) == len(set(ids)) and ids, "Unique nonempty source IDs required")
    require(any(s["kind"] == "production_diff" for s in material["sources"]), "Production diff required")


def validate_citations(evidence, material, required=False):
    require(isinstance(evidence, list) and (evidence or not required), "Source citation required")
    sources = {s["source_id"]: s for s in material["sources"]}
    for anchor in evidence:
        source = sources.get(anchor.get("source_id"))
        require(source is not None and source["kind"] != "message", "Implementation evidence must reference supplied source")
        start, end = anchor["start_line"], anchor["end_line"]
        lines, offset = source["content"].splitlines(), source["start_line"]
        require(type(start) is int and type(end) is int and offset <= start <= end < offset + len(lines), "Citation outside source range")
        require(anchor.get("quote") == "\n".join(lines[start - offset:end - offset + 1]), "Citation quote differs from source")


def validate_analysis(value, material):
    require(isinstance(value, dict) and isinstance(value.get("changes"), list), "changes array required")
    require(isinstance(value.get("unknowns"), list), "unknowns array required")
    commit_context.validate_requests(value)
    for field in ("version", "target_revision", "parent_revision"):
        require(value.get(field) == material[field], f"Analysis identity mismatch: {field}")
    require(value["changes"] or value["unknowns"], "Explain an empty analysis")
    change_ids, condition_ids = set(), set()
    paths = {s["path"] for s in material["sources"] if s["kind"] != "message"}
    for change in value["changes"]:
        key = change.get("change_id")
        require(nonempty(key) and key not in change_ids, "Unique change_id required")
        change_ids.add(key)
        require(change.get("applicability") in {"sql", "not_sql", "unknown"}, "Invalid applicability")
        for field in ("change_type", "module", "reason"):
            require(nonempty(change.get(field)), f"{field} required (unknown allowed)")
        for field in ("facts", "locations", "affected_features", "conditions", "unknowns"):
            require(isinstance(change.get(field), list), f"{field} array required")
        for loc in change["locations"]:
            require(loc.get("path") in paths and isinstance(loc.get("functions"), list) and loc["functions"], "Location/functions not grounded")
        for fact in change["facts"]:
            require(nonempty(fact.get("text")), "Fact text required")
            validate_citations(fact.get("evidence"), material, required=True)
        for condition in change["conditions"]:
            key = condition.get("condition_id")
            require(nonempty(key) and key not in condition_ids, "Unique condition_id required")
            condition_ids.add(key)
            require(condition.get("kind") in {"schema", "data", "query", "session", "config"}, "Invalid condition kind")
            require(condition.get("status") in {"source_supported", "hypothesis", "unknown"}, "Invalid evidence level")
            require(nonempty(condition.get("description")), "Condition description required")
            validate_citations(condition.get("evidence"), material, condition["status"] == "source_supported")
    return condition_ids


def validate_candidates(value, analysis):
    require(isinstance(value, dict) and isinstance(value.get("candidates"), list), "candidates array required")
    require(isinstance(value.get("shortfall_reasons"), list), "shortfall_reasons required")
    seeds = value["candidates"]
    require(len(seeds) <= BATCH_SIZE, "More than 10 candidates")
    require(len(seeds) == BATCH_SIZE or any(nonempty(x) for x in value["shortfall_reasons"]), "Explain candidate shortfall")
    conditions = {c["condition_id"] for ch in analysis["changes"] for c in ch["conditions"] if ch["applicability"] != "not_sql"}
    ids, bodies = set(), set()
    for seed in seeds:
        key = seed.get("candidate_id")
        require(isinstance(key, str) and re.fullmatch(r"[a-zA-Z0-9_-]+", key) and key not in ids, "Unique safe candidate_id required")
        ids.add(key)
        links = seed.get("condition_ids")
        require(isinstance(links, list) and links and set(links) <= conditions, "Unknown condition link")
        for field in ("setup", "operations", "cleanup", "configuration", "session_order", "expected_observations", "capability_gaps"):
            require(isinstance(seed.get(field), list), f"{field} array required")
        require(seed["operations"], "Target operation required")
        sessions = seed["session_order"]
        require(sessions and all(nonempty(s) for s in sessions)
                and len(sessions) == len(set(sessions)), "Unique ordered sessions required")
        require(seed.get("execution_mode", "serial") in {"serial", "concurrent"},
                "execution_mode must be serial or concurrent")
        for item in seed["setup"] + seed["operations"] + seed["cleanup"]:
            require(isinstance(item, dict) and item.get("session") in sessions and nonempty(item.get("sql")), "SQL/session missing")
            require(isinstance(item.get("condition_ids"), list) and set(item["condition_ids"]) <= set(links), "Step condition link invalid")
        for item in seed["configuration"]:
            require(isinstance(item, dict) and item.get("session") in sessions and nonempty(item.get("sql")),
                    "Only session-scoped SQL configuration is supported")
            require(re.match(r"(?is)^\s*SET\s+(?:SESSION\b|@@SESSION\.|NAMES\b|CHARACTER\s+SET\b|TRANSACTION\b)", item["sql"])
                    and ";" not in item["sql"].rstrip().rstrip(";"),
                    "Configuration must be one supported session-scoped SET statement")
        for obs in seed["expected_observations"]:
            require(obs.get("condition_id") in links and nonempty(obs.get("description")), "Observation condition link invalid")
        require(seed["expected_observations"], "Expected target observation required")
        oracle = seed.get("proposed_oracle", {})
        require(nonempty(oracle.get("description")) and nonempty(oracle.get("derivation")), "Proposed oracle and derivation required")
        body = digest({k: seed[k] for k in ("setup", "operations", "cleanup", "configuration", "session_order")}
                      | {"execution_mode": seed.get("execution_mode", "serial")})
        require(body not in bodies, "Duplicate candidate test body")
        bodies.add(body)
    return seeds


def validate_contracts(contracts):
    require(isinstance(contracts, list), "Contracts must be an array")
    ids = set()
    for c in contracts:
        require(nonempty(c.get("contract_id")) and c["contract_id"] not in ids, "Unique contract ID required")
        ids.add(c["contract_id"])
        require(c.get("kind") in {"target", "oracle"}, "Invalid contract kind")
        methods = {"source_instrumentation", "branch_coverage", "semantic_event", "version_differential"} if c["kind"] == "target" else {"independent_expected", "metamorphic", "sanitizer", "assertion"}
        require(c.get("method") in methods, "Model judgment is not a supported detector; use an independent measurement method")
        require(sha_value(c.get("producer_sha256")), "Freeze independent producer code hash")
        require(nonempty(c.get("description")) and nonempty(c.get("evidence_basis")), "Describe detector and independent evidence basis")
        require(c.get("pointer", "").startswith("/measurements/"), "Detector pointer must address measurements")
        require(c.get("operator") in {"eq", "gt"} and "expected" in c, "Detector predicate required")
        if c["operator"] == "gt":
            require(type(c["expected"]) in (int, float), "gt requires numeric threshold")


def initialize(material_path, run, run_id, contracts_path=None, model="deepseek-v4-pro", max_tokens=16384, thinking="disabled", temperature=0.7, rounds=ROUNDS):
    material = read(material_path)
    validate_material(material)
    contracts = read(contracts_path) if contracts_path else []
    validate_contracts(contracts)
    require(nonempty(run_id) and nonempty(model), "run_id/model required")
    require(type(rounds) is int and 1 <= rounds <= ROUNDS, "rounds must be between 1 and the maximum budget")
    require(thinking in {"enabled", "disabled"} and type(max_tokens) is int and max_tokens > 0, "Invalid model parameters")
    require(type(temperature) in (int, float) and 0 <= temperature <= 2, "Invalid temperature")
    run = Path(run)
    run.mkdir(parents=True, exist_ok=False)
    write(run / "material.json", material)
    write(run / "contracts.json", contracts)
    for stage in ("stage1", "stage2"):
        (run / f"{stage}.txt").write_bytes((PROMPTS / f"{stage}.txt").read_bytes())
    (run / "pipeline_source.py").write_bytes(Path(__file__).read_bytes())
    (run / "context_source.py").write_bytes(Path(commit_context.__file__).read_bytes())
    try:
        code_commit = git(ROOT, "rev-parse", "HEAD").strip()
        code_dirty = bool(git(ROOT, "status", "--porcelain"))
    except (OSError, subprocess.SubprocessError):
        code_commit, code_dirty = "unknown", None
    write(run / "manifest.json", dict(workflow="commit_analysis_v1", run_id=run_id, created_at=now(),
        rounds=rounds, batch_size=BATCH_SIZE, model=model, base_url="https://api.deepseek.com",
        parameters={"max_tokens": max_tokens, "thinking": {"type": thinking}, "temperature": temperature,
                    "response_format": {"type": "json_object"}},
        code_commit=code_commit, code_dirty=code_dirty, python=sys.version, platform=platform.platform(), command=sys.argv,
        feedback_policy=("immediately_previous_round_differences_else_default"
                         if any(c["kind"] == "target" and c["method"] == "version_differential" for c in contracts)
                         else "immediately_previous_round_verified_hits_else_default"),
        files={p: file_hash(run / p) for p in ("material.json", "contracts.json", "stage1.txt", "stage2.txt", "pipeline_source.py", "context_source.py")},
        database_execution="external_only", mutator_status="not_assessed"))
    return step(run)


def load_run(run):
    run = Path(run)
    manifest = read(run / "manifest.json")
    require(manifest.get("workflow") == "commit_analysis_v1" and type(manifest.get("rounds")) is int
            and 1 <= manifest["rounds"] <= ROUNDS and manifest.get("batch_size") == BATCH_SIZE,
            "Unexpected workflow/budget")
    for path, expected in manifest["files"].items():
        require(file_hash(run / path) == expected, f"Frozen input changed: {path}")
    require(file_hash(__file__) == manifest["files"]["pipeline_source.py"], "Pipeline code changed; start a new run")
    require(file_hash(commit_context.__file__) == manifest["files"]["context_source.py"], "Context code changed; start a new run")
    return run, manifest, read(run / "material.json"), read(run / "contracts.json")


class DeepSeek:
    """Authenticated discovery and completions. No fallback model or retries."""
    def __init__(self, key, timeout=180):
        require(nonempty(key), "DEEPSEEK_API_KEY is absent")
        self.key, self.timeout = key, timeout

    def call(self, endpoint, payload=None):
        request = urllib.request.Request("https://api.deepseek.com/" + endpoint,
            data=canonical(payload) if payload is not None else None,
            headers={"Authorization": "Bearer " + self.key, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            raise RuntimeError(f"DeepSeek HTTP {error.code}; response body omitted") from None
        except (urllib.error.URLError, TimeoutError):
            raise RuntimeError("DeepSeek transport failure; remote completion unknown") from None


def probe_models(output, model="deepseek-v4-pro", client=None):
    output = Path(output)
    require(not output.exists(), "Model probe output already exists")
    result = dict(started_at=now(), model_requested=model, status="failed", generation_called=False,
                  database_executed=False, provider_version="unknown")
    try:
        if client is None:
            client = DeepSeek(os.environ.get("DEEPSEEK_API_KEY"), timeout=30)
        response = client.call("models")
        require(isinstance(response, dict) and isinstance(response.get("data"), list), "Invalid model catalog")
        matches = [m for m in response["data"] if m.get("id") == model]
        result.update(status="available" if matches else "unavailable", response=response,
                      selected_metadata=matches, provider_version="not_inferred_from_alias")
    except (ValueError, OSError, RuntimeError, TypeError, AttributeError) as error:
        result.update(failure_type=type(error).__name__, reason=str(error))
    result["finished_at"] = now()
    write(output, result)
    return result


def checked_artifact(folder, filename):
    result = read(folder / "result.json")
    require(result["status"] == "accepted", "Previous generation was not accepted; use a new run")
    require(file_hash(folder / filename) == result["output_sha256"], "Accepted generation changed")
    return read(folder / filename)


def feedback_examples(run, number):
    if number == 1:
        return [], "first_round_default"
    folder = run / "rounds" / f"{number - 1:02d}"
    require((folder / "feedback.json").exists(), "Record preceding round feedback before generating next round")
    value = checked_artifact(folder, "candidates.json")
    checked = classify_feedback(run, number - 1, value, read(folder / "observations.json"), folder / "evidence")
    require(checked == read(folder / "feedback.json"), "Feedback or evidence changed")
    by_id = {s["candidate_id"]: s for s in value["candidates"]}
    _, _, _, contracts = load_run(run)
    differential = any(c["kind"] == "target" and c["method"] == "version_differential" for c in contracts)
    if differential:
        examples = [by_id[r["candidate_id"]] for r in checked["records"]
                    if r["differential_status"] == "difference"]
        return examples, "previous_round_verified_differences" if examples else "previous_round_no_verified_difference_default"
    examples = [by_id[r["candidate_id"]] for r in checked["records"] if r["target_status"] == "hit"]
    return examples, "previous_round_verified_hits" if examples else "previous_round_no_verified_hit_default"


def requirements_view(analysis):
    """Keep analysis evidence; omit quoted code and legacy model role judgments."""
    view = json.loads(canonical(analysis))
    view.pop("commit_status", None)
    view.pop("commit_status_reason", None)
    for change in view["changes"]:
        for item in change["facts"] + change["conditions"]:
            for anchor in item["evidence"]:
                anchor.pop("quote", None)
    return view


def numbered_material(material):
    """Model-facing material view: prefix every source line with its absolute line
    number ("ABS | raw line") so citations do not require the model to count lines.
    Only the payload is numbered; the on-disk material and citation validation keep
    the raw content, and the model quotes the text after " | " (the raw line)."""
    view = json.loads(canonical(material))
    for source in view["sources"]:
        start = source["start_line"]
        source["content"] = "\n".join(
            f"{start + i} | {line}" for i, line in enumerate(source["content"].splitlines()))
    return view


def step(run, execute=False, client=None):
    run, manifest, material, contracts = load_run(run)
    stage1 = run / "analysis"
    if not (stage1 / "result.json").exists():
        folder, filename, number = stage1, "analysis.json", None
        payload = {"material": numbered_material(material), "output_shape": ANALYSIS_SHAPE}
        system = (run / "stage1.txt").read_text(encoding="utf-8")
        selection = {"reason": "stage1_commit_analysis", "example_ids": []}
    else:
        analysis = checked_artifact(stage1, "analysis.json")
        validate_analysis(analysis, material)
        if analysis["material_status"] == "insufficient":
            return {"status": "awaiting_source_material", "candidate_generation": "not_run",
                    "missing_materials": analysis["missing_materials"], "database_executed": False}
        if not any(ch["conditions"] for ch in analysis["changes"] if ch["applicability"] != "not_sql"):
            skipped = {"status": "no_applicable_conditions", "candidate_generation": "not_run",
                       "reason": "No SQL-mappable conditions; preserve unknown/not_sql analysis", "database_executed": False}
            if not (run / "generation_not_run.json").exists():
                write(run / "generation_not_run.json", skipped)
            return skipped
        round_budget = manifest["rounds"]
        number = next((i for i in range(1, round_budget + 1) if not (run / "rounds" / f"{i:02d}" / "result.json").exists()), None)
        if number is None:
            for i in range(1, round_budget + 1):
                checked_artifact(run / "rounds" / f"{i:02d}", "candidates.json")
            if not (run / "rounds" / f"{round_budget:02d}" / "feedback.json").exists():
                return {"status": "awaiting_final_feedback", "report": report(run)}
            return {"status": "generation_budget_exhausted", "report": report(run)}
        for i in range(1, number):
            checked_artifact(run / "rounds" / f"{i:02d}", "candidates.json")
        folder, filename = run / "rounds" / f"{number:02d}", "candidates.json"
        examples, reason = feedback_examples(run, number)
        selection = {"reason": reason, "source_round": number - 1 if number > 1 else None,
                     "example_ids": [s["candidate_id"] for s in examples], "example_hashes": [digest(s) for s in examples]}
        payload = {"analysis": requirements_view(analysis), "version": material["version"],
                   "commit_role": material["commit_role"], "commit_role_source": "input_annotation",
                   "round": number, "requested_candidates": BATCH_SIZE,
                   ("verified_difference_examples" if any(c["kind"] == "target" and c["method"] == "version_differential" for c in contracts)
                    else "verified_target_examples"): examples,
                   "output_shape": CANDIDATE_SHAPE}
        system = (run / "stage2.txt").read_text(encoding="utf-8")
    request = dict(model=manifest["model"], messages=[{"role": "system", "content": system},
                   {"role": "user", "content": canonical(payload).decode()}], **manifest["parameters"])
    for name, data in (("request.json", request), ("selection.json", selection)):
        path = folder / name
        if path.exists():
            require(read(path) == data, "Prepared request/selection changed")
        else:
            write(path, data)
    if not execute:
        return {"status": "preview_only", "request": str(folder / "request.json"), "round": number,
                "model_called": False, "database_executed": False}
    require(not (folder / "attempt.json").exists(), "Attempt already exists; no silent retry/overwrite")
    write(folder / "attempt.json", {"started_at": now(), "request_sha256": file_hash(folder / "request.json"),
                                   "model_requested": manifest["model"], "round": number})
    result = {"status": "failed", "round": number, "candidate_generation": "not_run", "database_executed": False,
              "accepted_count": 0, "received_count": None, "model_requested": manifest["model"], "returned_model": None}
    phase = "model_discovery"
    try:
        if client is None:
            client = DeepSeek(os.environ.get("DEEPSEEK_API_KEY"))
        models = client.call("models")
        write(folder / "models.json", {"observed_at": now(), "response": models})
        require(isinstance(models, dict) and isinstance(models.get("data"), list), "Invalid model catalog")
        require(any(m.get("id") == manifest["model"] for m in models.get("data", [])), "Requested model unavailable; no fallback")
        phase = "completion"
        result["candidate_generation"] = "requested"
        raw = client.call("chat/completions", request)
        write(folder / "response.json", raw)
        require(isinstance(raw, dict), "Invalid completion envelope")
        result.update(returned_model=raw.get("model"), provider_created=raw.get("created"), response_id=raw.get("id"),
                      usage=raw.get("usage"), response_sha256=file_hash(folder / "response.json"))
        require(raw.get("model") == manifest["model"], "Returned model identity differs or absent; response not accepted")
        phase = "parse_and_validate"
        choice = raw["choices"][0]
        require(choice.get("finish_reason") == "stop", "Completion truncated or incomplete")
        value = json.loads(choice["message"]["content"])
        if number is None:
            validate_analysis(value, material)
            result.update(material_status=value["material_status"], missing_materials=value["missing_materials"])
        else:
            if isinstance(value, dict) and isinstance(value.get("candidates"), list):
                result["received_count"] = len(value["candidates"])
            validate_candidates(value, analysis)
        write(folder / filename, value)
        result.update(status="accepted", candidate_generation="completed" if number else "not_applicable",
                      accepted_count=len(value["candidates"]) if number else 0,
                      output_sha256=file_hash(folder / filename), semantic_accuracy="not_evaluated", remote_completion="response_received")
    except (ValueError, KeyError, TypeError, IndexError, AttributeError, OSError, RuntimeError) as error:
        result.update(failure_phase=phase, failure_type=type(error).__name__, reason=str(error),
                      candidate_generation="not_run" if phase == "model_discovery" else "failed",
                      remote_completion="response_received" if (folder / "response.json").exists() else (
                          "unknown" if phase == "completion" else "not_requested"))
    result["finished_at"] = now()
    write(folder / "result.json", result)
    return result


def supplement_run(run, repo, output):
    run, manifest, material, _ = load_run(run)
    analysis = checked_artifact(run / "analysis", "analysis.json")
    validate_analysis(analysis, material)
    require(analysis["missing_materials"], "No missing source materials requested")
    for revision in (material["parent_revision"], material["target_revision"]):
        require(git(repo, "rev-parse", "--verify", revision + "^{commit}").strip() == revision,
                "Source repository does not contain the frozen commit")
    enriched = commit_context.supplement(repo, material, analysis)
    enriched["supplementation"].update(parent_run_id=manifest["run_id"],
        parent_material_sha256=file_hash(run / "material.json"),
        analysis_sha256=file_hash(run / "analysis" / "analysis.json"), collected_at=now())
    validate_material(enriched)
    write(output, enriched)
    return {"status": "source_supplement_saved", "output": str(output),
            "new_source_count": len(enriched["supplementation"]["new_source_ids"]),
            "outcomes": enriched["supplementation"]["outcomes"],
            "next_step": "Initialize a new run with the enriched material and reanalyze stage 1",
            "model_called": False, "database_executed": False}


def reference_file(base, reference):
    require(isinstance(reference, dict) and sha_value(reference.get("sha256")), "Evidence reference needs sha256")
    base = Path(base).resolve()
    require(not Path(reference["path"]).is_absolute() and ".." not in Path(reference["path"]).parts,
            "Evidence reference must be relative without traversal")
    path = (base / reference["path"]).resolve()
    require(path.is_relative_to(base) and path.is_file(), "Evidence path must be a contained file")
    require(file_hash(path) == reference["sha256"], "Evidence hash mismatch")
    return path


def measure(base, reference, contract, binding):
    artifact = read(reference_file(base, reference))
    for key, expected in binding.items():
        if key in {"expected_parent_revision", "expected_target_revision"}:
            continue
        require(artifact.get(key) == expected, f"Measurement binding mismatch: {key}")
    require(artifact.get("producer_sha256") == contract["producer_sha256"], "Measurement producer differs from frozen contract")
    require(artifact.get("method") == contract["method"], "Measurement method mismatch")
    require(nonempty(artifact.get("observed_at")), "Measurement time required")
    require(isinstance(artifact.get("raw_evidence"), list) and artifact["raw_evidence"], "Raw evidence required")
    for ref in artifact["raw_evidence"]:
        reference_file(base, ref)
    if contract["method"] == "version_differential":
        measured = artifact.get("measurements", {})
        require(measured.get("parent_revision") == binding.get("expected_parent_revision"),
                "Differential evidence parent revision mismatch")
        require(measured.get("target_revision") == binding.get("expected_target_revision"),
                "Differential evidence target revision mismatch")
    value = artifact
    for token in contract["pointer"].split("/")[1:]:
        key = token.replace("~1", "/").replace("~0", "~")
        require(isinstance(value, dict) and key in value, "Measured field absent; cannot classify as miss")
        value = value[key]
    if contract["operator"] == "eq":
        require(type(value) is type(contract["expected"]), "Measured value type differs")
        return value == contract["expected"]
    require(type(value) in (int, float), "Measured value must be numeric")
    return value > contract["expected"]


def next_round_examples(records, contracts):
    differential = any(c["kind"] == "target" and c["method"] == "version_differential"
                       for c in contracts)
    status = "differential_status" if differential else "target_status"
    selected = "difference" if differential else "hit"
    return [r["candidate_id"] for r in records if r[status] == selected]


def classify_feedback(run, number, candidates, observations, evidence_base):
    _, manifest, material, contracts = load_run(run)
    require(observations.get("run_id") == manifest["run_id"] and observations.get("round") == number, "Feedback run/round mismatch")
    items = observations.get("observations")
    require(isinstance(items, list), "observations array required")
    indexed = {x["candidate_id"]: x for x in items}
    seeds = candidates["candidates"]
    require(len(indexed) == len(items) and set(indexed) <= {s["candidate_id"] for s in seeds}, "Duplicate/unknown observed candidate")
    by_contract = {c["contract_id"]: c for c in contracts}
    records = []
    for seed in seeds:
        cid, fingerprint = seed["candidate_id"], digest(seed)
        obs = indexed.get(cid)
        row = dict(candidate_id=cid, candidate_sha256=fingerprint, execution_status="not_run", validity="unknown",
                   target_observable=False, target_status="not_run", oracle_status="not_run", bug_status="not_adjudicated",
                   differential_status="not_run",
                   reason="No execution evidence supplied")
        if obs is not None:
            require(obs.get("candidate_sha256") == fingerprint, "Observed candidate hash mismatch")
            require(nonempty(obs.get("reason")), "Observation reason required")
            execution = obs["execution"]
            status = execution.get("status")
            require(status in {"not_run", "failed", "completed"}, "Invalid execution status")
            row.update(execution_status=status, reason=obs["reason"])
            if status != "not_run":
                require(execution.get("actual_revision") == material["target_revision"], "Execution revision mismatch")
                require(isinstance(execution.get("environment"), dict) and execution["environment"], "Execution environment required")
                require(nonempty(execution.get("observed_at")) and execution.get("command"), "Execution time/command required")
                require(sha_value(execution.get("runner_sha256")), "Actual runner hash required")
                reference_file(evidence_base, execution["evidence"])
                require(obs.get("validity") in {"valid", "invalid", "unknown"}, "Validity state required")
                differential_run = any(c["kind"] == "target" and c["method"] == "version_differential" for c in contracts)
                row.update(validity=obs["validity"], target_status="not_measured" if differential_run else "unobservable",
                           oracle_status="unknown", differential_status="inconclusive" if differential_run else "not_run")
            for kind in ("target", "oracle"):
                measurement = obs.get(kind)
                if not measurement:
                    continue
                require(status != "not_run", "Cannot measure unexecuted test")
                c = by_contract.get(measurement.get("contract_id"))
                require(c is not None and c["kind"] == kind, "Measurement needs predeclared contract of same kind")
                binding = dict(run_id=manifest["run_id"], round=number, candidate_id=cid,
                               candidate_sha256=fingerprint, actual_revision=material["target_revision"], contract_id=c["contract_id"])
                if c["method"] == "version_differential":
                    binding.update(expected_parent_revision=material["parent_revision"],
                                   expected_target_revision=material["target_revision"])
                positive = measure(evidence_base, measurement["evidence"], c, binding)
                if kind == "target" and c["method"] == "version_differential":
                    row["differential_status"] = (
                        "inconclusive" if obs["validity"] != "valid" or status != "completed"
                        else "difference" if positive else "no_difference")
                    row["differential_contract_id"] = c["contract_id"]
                else:
                    row[kind + "_status"] = ("hit" if positive else "miss") if kind == "target" else ("anomaly_candidate" if positive else "no_anomaly")
                    row[kind + "_contract_id"] = c["contract_id"]
                    if kind == "target":
                        row["target_observable"] = True
        records.append(row)
    return dict(run_id=manifest["run_id"], round=number, generated_count=len(seeds), records=records,
                counts={key: dict(Counter(r[key] for r in records)) for key in ("execution_status", "validity", "target_status", "oracle_status", "differential_status")},
                selected_for_next_round=next_round_examples(records, contracts))


def record_feedback(run, number, input_path=None):
    run, manifest, _, _ = load_run(run)
    require(1 <= number <= manifest["rounds"], "Round outside budget")
    folder = run / "rounds" / f"{number:02d}"
    require(not (folder / "feedback.json").exists(), "Feedback already frozen")
    require(not (run / "rounds" / f"{number + 1:02d}" / "request.json").exists(), "Next round already prepared")
    value = checked_artifact(folder, "candidates.json")
    observations = read(input_path) if input_path else {"run_id": manifest["run_id"], "round": number, "observations": []}
    base = Path(input_path).resolve().parent if input_path else folder
    classified = classify_feedback(run, number, value, observations, base)
    references = []
    for obs in observations["observations"]:
        if obs["execution"]["status"] != "not_run":
            references.append(obs["execution"]["evidence"])
        for kind in ("target", "oracle"):
            if obs.get(kind):
                ref = obs[kind]["evidence"]
                references.append(ref)
                references.extend(read(reference_file(base, ref))["raw_evidence"])
    for ref in references:
        source = reference_file(base, ref)
        dest = folder / "evidence" / source.relative_to(base.resolve())
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            require(file_hash(dest) == ref["sha256"], "Copied evidence conflicts")
        else:
            with dest.open("xb") as stream:
                stream.write(source.read_bytes())
    write(folder / "observations.json", observations)
    write(folder / "feedback.json", classified)
    return classified


def report(run):
    run, manifest, material, _ = load_run(run)
    rounds = []
    for i in range(1, manifest["rounds"] + 1):
        folder = run / "rounds" / f"{i:02d}"
        result = read(folder / "result.json") if (folder / "result.json").exists() else {
            "status": "interrupted_unknown" if (folder / "attempt.json").exists() else "not_run",
            "received_count": None, "accepted_count": 0}
        requested = None if result["status"] == "interrupted_unknown" else (
            BATCH_SIZE if result.get("candidate_generation") in {"requested", "completed", "failed"} else 0)
        row = {"round": i, "planned_count": BATCH_SIZE, "requested_count": requested, "generation_status": result["status"],
               "received_count": result.get("received_count"), "accepted_count": result["accepted_count"],
               "feedback_status": "not_recorded", "reason": result.get("reason")}
        if (folder / "feedback.json").exists():
            value = checked_artifact(folder, "candidates.json")
            feedback = classify_feedback(run, i, value, read(folder / "observations.json"), folder / "evidence")
            require(feedback == read(folder / "feedback.json"), "Feedback changed")
            row.update(feedback_status="recorded", counts=feedback["counts"])
        rounds.append(row)
    return dict(run_id=manifest["run_id"], target_revision=material["target_revision"], model_requested=manifest["model"],
                stage1=read(run / "analysis" / "result.json") if (run / "analysis" / "result.json").exists() else {
                    "status": "interrupted_unknown" if (run / "analysis" / "attempt.json").exists() else "not_run"},
                planned_total=manifest["rounds"] * BATCH_SIZE,
                requested_total=None if any(r["requested_count"] is None for r in rounds) else sum(r["requested_count"] for r in rounds),
                accepted_total=sum(r["accepted_count"] for r in rounds), rounds=rounds,
                generation_not_run=read(run / "generation_not_run.json") if (run / "generation_not_run.json").exists() else None,
                mutator_status="not_assessed", independent_bug_count=None)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--repository", required=True, type=Path)
    p.add_argument("--commit", required=True)
    p.add_argument("--parent")
    p.add_argument("--spec", type=Path, help="Optional version/role and explicit source selection; omit for automatic extraction")
    p.add_argument("--output", required=True, type=Path)
    p = sub.add_parser("init")
    p.add_argument("--material", required=True, type=Path)
    p.add_argument("--run", required=True, type=Path)
    p.add_argument("--run-id", required=True)
    p.add_argument("--rounds", type=int, default=ROUNDS)
    p.add_argument("--contracts", type=Path)
    p.add_argument("--model", default="deepseek-v4-pro")
    p.add_argument("--max-tokens", type=int, default=16384)
    p.add_argument("--thinking", choices=("enabled", "disabled"), default="disabled")
    p.add_argument("--temperature", type=float, default=0.7)
    p = sub.add_parser("models", help="Explicit authenticated model discovery; no generation")
    p.add_argument("--output", required=True, type=Path)
    p.add_argument("--model", default="deepseek-v4-pro")
    p = sub.add_parser("step")
    p.add_argument("--run", required=True, type=Path)
    p.add_argument("--execute-model", action="store_true")
    p = sub.add_parser("supplement", help="Read requested source from frozen revisions; write new material for reanalysis")
    p.add_argument("--run", required=True, type=Path)
    p.add_argument("--repository", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    p = sub.add_parser("feedback")
    p.add_argument("--run", required=True, type=Path)
    p.add_argument("--round", required=True, type=int)
    p.add_argument("--input", type=Path)
    p = sub.add_parser("report")
    p.add_argument("--run", required=True, type=Path)
    args = parser.parse_args(argv)
    if args.action == "prepare":
        prepare(args.repository, args.commit, args.spec, args.output, args.parent)
        result = {"status": "material_prepared", "output": str(args.output), "model_called": False}
    elif args.action == "init":
        result = initialize(args.material, args.run, args.run_id, args.contracts, args.model, args.max_tokens, args.thinking, args.temperature, args.rounds)
    elif args.action == "models":
        result = probe_models(args.output, args.model)
    elif args.action == "step":
        result = step(args.run, args.execute_model)
    elif args.action == "supplement":
        result = supplement_run(args.run, args.repository, args.output)
    elif args.action == "feedback":
        result = record_feedback(args.run, args.round, args.input)
    else:
        result = report(args.run)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(result.get("status") == "failed")


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError, subprocess.SubprocessError) as error:
        raise SystemExit(f"ERROR: {error}")
