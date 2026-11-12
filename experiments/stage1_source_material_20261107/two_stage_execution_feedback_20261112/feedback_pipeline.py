"""Collect verified Stage2 execution feedback and prepare the next Stage2 request.

This adapter is deliberately offline.  It consumes an already archived execution
directory; it does not run MySQL or call DeepSeek.  The execution runner remains
responsible for producing result JSON and, when available, path/oracle evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


LABELS = {"PATH_REACHED", "ANOMALY_OBSERVED"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON object required: {path}")
    return value


def safe_ref(run_dir: Path, value: str) -> dict[str, str]:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"evidence path must be relative: {value}")
    resolved = (run_dir / path).resolve()
    if not resolved.is_relative_to(run_dir.resolve()) or not resolved.is_file():
        raise ValueError(f"evidence file is outside run or missing: {value}")
    return {"path": path.as_posix(), "sha256": sha256(resolved)}


def evidence_refs(run_dir: Path, value: Any) -> list[dict[str, str]]:
    if value is None:
        return []
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ValueError("evidence_files must be a list of relative paths")
    return [safe_ref(run_dir, item) for item in value]


def result_summary(result_path: Path | None) -> dict[str, Any]:
    if result_path is None or not result_path.is_file():
        return {"available": False}
    result = load_json(result_path)
    trials = result.get("trials", [])
    if not isinstance(trials, list):
        raise ValueError(f"trials must be a list: {result_path}")
    return {
        "available": True,
        "revision": result.get("revision"),
        "trials": [
            {
                "repeat": trial.get("repeat"),
                "returncode": trial.get("returncode"),
                "sql_errors": trial.get("sql_errors", []),
                "stdout_sha256": trial.get("stdout_sha256"),
                "stderr_sha256": trial.get("stderr_sha256"),
                "xml_parse": trial.get("xml_parse"),
            }
            for trial in trials
            if isinstance(trial, dict)
        ],
    }


def comparison_summary(path: Path | None) -> dict[str, Any]:
    if path is None or not path.is_file():
        return {"available": False}
    value = load_json(path)
    comparisons = value.get("comparisons", [])
    return {
        "available": True,
        "parent_revision": value.get("parent_revision"),
        "target_revision": value.get("target_revision"),
        "comparisons": comparisons,
    }


def load_observations(path: Path | None) -> dict[str, dict[str, Any]]:
    if path is None:
        return {}
    value = load_json(path)
    cases = value.get("cases", value.get("observations", []))
    if not isinstance(cases, list):
        raise ValueError("observations JSON needs cases or observations array")
    indexed: dict[str, dict[str, Any]] = {}
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError("each observation must be an object")
        key = case.get("candidate_id") or case.get("case") or case.get("sql")
        if not isinstance(key, str) or not key or key in indexed:
            raise ValueError("observations need unique candidate_id/case/sql")
        indexed[key] = case
    return indexed


def find_comparison(run_dir: Path, case_id: str, result_root: Path) -> dict[str, Any]:
    direct = result_root / "comparison.json"
    if direct.is_file():
        return comparison_summary(direct)
    archived = run_dir / "runtime" / "comparison.json"
    if archived.is_file():
        value = load_json(archived)
        for pair in value.get("pairs", []):
            if isinstance(pair, dict) and pair.get("name") == case_id:
                return {"available": True, "source": "runtime/comparison.json", "pair": pair}
    return {"available": False}


def result_root_for(run_dir: Path, case_id: str) -> Path:
    for candidate in (
        run_dir / "server_evidence" / "results" / case_id,
        run_dir / "results" / case_id,
        run_dir / "runtime" / "results" / case_id,
    ):
        if candidate.is_dir():
            return candidate
    return run_dir / "server_evidence" / "results" / case_id


def build_case(run_dir: Path, sql_path: Path, observation: dict[str, Any] | None) -> tuple[dict[str, Any], str | None]:
    case_id = sql_path.stem
    result_root = result_root_for(run_dir, case_id)
    comparison = find_comparison(run_dir, case_id, result_root)
    parent = result_summary(result_root / "parent" / "result.json")
    target = result_summary(result_root / "target" / "result.json")
    observation = observation or {}

    path_info = observation.get("path", observation.get("path_evidence", {}))
    if path_info is None:
        path_info = {}
    if not isinstance(path_info, dict):
        raise ValueError(f"path evidence must be an object: {case_id}")
    path_status = path_info.get("status", "unverified")
    if path_status not in {"confirmed", "not_observed", "unverified"}:
        raise ValueError(f"invalid path status for {case_id}: {path_status}")
    path_refs = evidence_refs(run_dir, path_info.get("evidence_files", []))

    oracle = observation.get("oracle", observation.get("outcome", {}))
    if oracle is None:
        oracle = {}
    if not isinstance(oracle, dict):
        raise ValueError(f"oracle evidence must be an object: {case_id}")
    oracle_status = oracle.get("status", "unknown")
    if oracle_status not in {"pass", "unknown", "anomaly", "runtime_anomaly"}:
        raise ValueError(f"invalid oracle status for {case_id}: {oracle_status}")
    oracle_refs = evidence_refs(run_dir, oracle.get("evidence_files", []))

    labels: list[str] = []
    rejection: str | None = None
    if path_status == "confirmed" and path_refs:
        labels.append("PATH_REACHED")
    elif path_status == "confirmed":
        rejection = "path claimed confirmed without evidence files"

    expected = oracle.get("expected")
    observed = oracle.get("observed")
    if oracle_status in {"anomaly", "runtime_anomaly"} and oracle_refs and expected is not None and observed is not None:
        labels.append("ANOMALY_OBSERVED")
    elif oracle_status in {"anomaly", "runtime_anomaly"}:
        rejection = rejection or "anomaly requires expected, observed, and evidence files"

    if not labels and rejection is None:
        if any(item.get("status") == "observed_difference" for item in comparison.get("comparisons", []) if isinstance(item, dict)):
            rejection = "parent/target discrepancy without path or independent oracle evidence"
        elif oracle_status == "pass":
            rejection = "oracle passed and path was not confirmed"
        else:
            rejection = "no verified path or anomaly evidence"

    sql = sql_path.read_text(encoding="utf-8-sig")
    record = {
        "candidate_id": case_id,
        "originating_run": run_dir.name,
        "labels": labels,
        "sql": sql,
        "sql_sha256": sha256(sql_path),
        "execution": {
            "comparison": comparison,
            "parent": parent,
            "target": target,
        },
        "path_evidence": {
            "status": path_status,
            "object": path_info.get("object"),
            "source_location": path_info.get("source_location"),
            "branch": path_info.get("branch"),
            "evidence_files": path_refs,
        },
        "outcome_evidence": {
            "status": oracle_status,
            "expected": expected,
            "observed": observed,
            "evidence_files": oracle_refs,
        },
        "target_change_attribution": observation.get("attribution", {"status": "unverified"}),
    }
    return record, rejection


def collect(run_dir: Path, output_dir: Path, observations_path: Path | None) -> dict[str, Any]:
    run_dir = run_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=False)
    observations = load_observations(observations_path)
    sql_files = sorted(run_dir.glob("sql_*.sql"))
    if not sql_files:
        sql_files = sorted((run_dir / "input" / "sql").glob("*.sql"))
    if not sql_files:
        raise ValueError(f"no sql_*.sql files found in {run_dir}")
    examples: list[dict[str, Any]] = []
    excluded: list[dict[str, str]] = []
    seen: set[str] = set()
    for sql_path in sql_files:
        case_id = sql_path.stem
        observation = observations.get(case_id)
        record, rejection = build_case(run_dir, sql_path, observation)
        seen.add(case_id)
        if record["labels"]:
            examples.append(record)
        else:
            excluded.append({"candidate_id": case_id, "reason": rejection or "no verified label"})
    unknown_observations = sorted(set(observations) - seen)
    if unknown_observations:
        raise ValueError(f"observations refer to unknown SQL cases: {', '.join(unknown_observations)}")
    feedback = {
        "schema_version": 1,
        "feedback_kind": "stage2_execution_feedback",
        "source_run": run_dir.name,
        "examples": examples,
        "excluded": excluded,
        "selection_rule": {
            "PATH_REACHED": "confirmed path status plus hashed evidence files",
            "ANOMALY_OBSERVED": "independent anomaly status plus expected/observed values and hashed evidence files",
            "discrepancy_only": "excluded until path or independent oracle evidence is supplied",
        },
    }
    (output_dir / "feedback.json").write_text(json.dumps(feedback, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# Stage2 execution feedback", "", f"Source run: `{run_dir.name}`", ""]
    if examples:
        lines += ["## Verified examples", ""]
        for record in examples:
            lines += [f"### {record['candidate_id']} — {', '.join(record['labels'])}", "", "Evidence-backed SQL:", "", "```sql", record["sql"].rstrip(), "```", "", f"SQL SHA256: `{record['sql_sha256']}`", f"Path status: `{record['path_evidence']['status']}`", f"Oracle status: `{record['outcome_evidence']['status']}`", "", "Execution evidence:", "", "```json", json.dumps(record["execution"], ensure_ascii=False, indent=2), "```", ""]
    else:
        lines += ["## Verified examples", "", "None. Parent/target output is not treated as a successful feedback example without path or independent oracle evidence.", ""]
    lines += ["## Excluded candidates", ""]
    for item in excluded:
        lines.append(f"- `{item['candidate_id']}`: {item['reason']}")
    (output_dir / "feedback.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return feedback


def prepare(template_dir: Path, stage1_output: Path, feedback: Path, output_dir: Path, model: str | None) -> None:
    stage1 = stage1_output.read_text(encoding="utf-8-sig")
    feedback_text = feedback.read_text(encoding="utf-8-sig")
    if not stage1.strip() or not feedback_text.strip():
        raise ValueError("Stage1 output and feedback must be non-empty")
    template = (template_dir / "stage2_sql_prompt_template.txt").read_text(encoding="utf-8")
    if template.count("{{STAGE1_OUTPUT}}") != 1 or template.count("{{EXECUTION_FEEDBACK}}") != 1:
        raise ValueError("Stage2 template must contain exactly one Stage1 and one execution-feedback placeholder")
    if "five target SQL" not in template or "T1-T5" not in template:
        raise ValueError("Stage2 five-test diversity requirement is missing")
    prompt = template.replace("{{STAGE1_OUTPUT}}", stage1).replace("{{EXECUTION_FEEDBACK}}", feedback_text)
    output_dir.mkdir(parents=True, exist_ok=False)
    (output_dir / "stage2_prompt.txt").write_text(prompt, encoding="utf-8")
    config_path = template_dir / "pipeline_config.json"
    config = load_json(config_path) if config_path.is_file() else {}
    stage = next((item for item in config.get("stages", []) if item.get("name") == "stage2_sql"), {})
    request = {
        "model": model or stage.get("model", "deepseek-v4-flash"),
        "max_tokens": stage.get("max_tokens", 16384),
        "temperature": stage.get("temperature", 0.7),
        "thinking": stage.get("thinking", {"type": "disabled"}),
        "messages": [{"role": "user", "content": prompt}],
    }
    (output_dir / "stage2_request.json").write_text(json.dumps(request, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Offline Stage2 execution-feedback adapter")
    sub = parser.add_subparsers(dest="command", required=True)
    collect_parser = sub.add_parser("collect", help="classify archived SQL execution evidence")
    collect_parser.add_argument("run_dir", type=Path)
    collect_parser.add_argument("--output-dir", type=Path, required=True)
    collect_parser.add_argument("--observations", type=Path)
    prepare_parser = sub.add_parser("prepare", help="insert Stage1 output and feedback into Stage2")
    prepare_parser.add_argument("stage1_output", type=Path)
    prepare_parser.add_argument("feedback", type=Path)
    prepare_parser.add_argument("--template-dir", type=Path, default=Path(__file__).resolve().parent)
    prepare_parser.add_argument("--output-dir", type=Path, required=True)
    prepare_parser.add_argument("--model")
    args = parser.parse_args()
    if args.command == "collect":
        feedback = collect(args.run_dir, args.output_dir, args.observations)
        print(json.dumps({"examples": len(feedback["examples"]), "excluded": len(feedback["excluded"]), "output": str(args.output_dir.resolve())}, ensure_ascii=False))
    else:
        prepare(args.template_dir, args.stage1_output, args.feedback, args.output_dir, args.model)
        print(args.output_dir.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
