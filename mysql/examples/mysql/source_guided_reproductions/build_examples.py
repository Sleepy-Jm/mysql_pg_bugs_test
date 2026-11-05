"""Build/check completed demonstrations from immutable experiment artifacts (offline)."""
import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ARCHIVE = ROOT / "experiments/prompt_pipeline_20261104"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def render_example(prompt, answer, stage):
    # Teaching copies normalize newlines; archived evidence is never rewritten.
    current = prompt.split("### Current task\n")
    assert len(current) == 2, "Expected exactly one current task"
    if stage == "src2req":
        marker, ending = "# Target and source code\n", "# Description"
        instruction = (
            "Describe the high-level MySQL test requirements from the supplied source. "
            "Use: Target; Source-required conditions; Candidate construction; "
            "Correctness oracle; Coverage observation; Uncertainty."
        )
    else:
        marker, ending = "# Description of requirements\n", "# Test"
        instruction = (
            "Generate a complete MySQL test from the analysis-stage requirements. "
            "Use: Prerequisites; SQL; Expected results and oracle; "
            "Coverage observation; Execution status."
        )
    task = marker + current[1].split(marker, 1)[1]
    assert task.rstrip().endswith(ending), "Missing empty answer slot"
    return ("### Example task\n" + instruction + "\n\n" + task.rstrip()
            + "\n" + answer.rstrip() + "\n").encode("utf-8")


def expected_files():
    lineage = json.loads((ARCHIVE / "lineage.json").read_text(encoding="utf-8"))
    files, entries = {}, []
    for target in lineage["targets"]:
        name = target["name"]
        artifacts = target["artifacts"]
        for artifact in artifacts.values():
            assert digest((ARCHIVE / artifact["path"]).read_bytes()) == artifact["sha256"]
        examples = {}
        for stage in ("src2req", "req2test"):
            source = artifacts[stage + "_input"]
            answer = artifacts[stage + "_output"]
            data = render_example(
                (ARCHIVE / source["path"]).read_text(encoding="utf-8"),
                (ARCHIVE / answer["path"]).read_text(encoding="utf-8"), stage)
            path = f"{stage}/{name}.txt"
            files[path] = data
            examples[stage] = {"path": path, "sha256": digest(data)}
        observations = {}
        for role in ("parent", "target"):
            execution = target["execution"][role]
            data = (ARCHIVE / execution["result"]).read_bytes()
            assert digest(data) == execution["result_sha256"]
            trials = json.loads(data)["trials"]
            assert len(trials) == 3
            cases = [trial["evaluation"]["cases"] for trial in trials]
            status_maps = [{case["case_id"]: case["status"] for case in run} for run in cases]
            assert all(run == status_maps[0] for run in status_maps)
            observations[role] = status_maps[0]
        assert all(status == "pass" for status in observations["parent"].values())
        assert set(observations["parent"]) == set(observations["target"])
        assert set(observations["target"].values()) <= {"pass", "mismatch"}
        failures = [case for case, status in observations["target"].items() if status == "mismatch"]
        assert failures
        entries.append({
            "name": name,
            "mysql_revision": target["mysql_revision"],
            "parent_revision": target["parent_revision"],
            "evaluation_eligible": False,
            "require_full_sql_batch": True,
            "examples": examples,
            "original_artifacts": artifacts,
            "execution": target["execution"],
            "stable_mismatch_case_ids": failures,
            "target_passing_control_case_ids": [case for case, status in observations["target"].items() if status == "pass"],
        })
    manifest = {
        "role": "development_reference",
        "evaluation_eligible": False,
        "evidence_archive_relative_to_repository": "experiments/prompt_pipeline_20261104",
        "original_artifact_paths_relative_to": "evidence_archive_relative_to_repository",
        "example_paths_relative_to": "this manifest directory",
        "transformation": "Remove historical INTERSECT example; retain current source/requirements and append saved stage answer; replace task instruction with self-contained example instruction; normalize copies to LF. No new model generation or SQL execution.",
        "context": "Non-blind, same-assistant shared chat; confirmed prior exposure to another window AVG divisor implementation. See contamination_review.md in evidence archive.",
        "evaluation_exclusion_policy": "Exclude these targets and related fixes, adjacent parent/child revisions and semantically duplicate trigger families from held-out evaluation. Metadata is a policy declaration, not an implemented evaluation gate.",
        "targets": entries,
    }
    files["manifest.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check only; never write")
    args = parser.parse_args()
    files = expected_files()
    for name, data in files.items():
        path = HERE / name
        if args.check:
            assert path.read_bytes() == data, f"Stale or modified example: {name}"
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    print(f"{'Verified' if args.check else 'Built'} 6 completed examples + manifest; original artifact hashes and 18 trial status maps checked.")


if __name__ == "__main__":
    main()
