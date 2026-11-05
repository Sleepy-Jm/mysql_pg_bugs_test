"""Snapshot the input package and render stage two from actual stage-one outputs."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    original = args.input.resolve()
    checks = []
    for line in (original / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        digest, name = line.split(None, 1)
        assert sha(original / name) == digest, name
        checks.append(name)
    snapshot = ROOT / "input_bundle"
    if not snapshot.exists():
        shutil.copytree(original, snapshot)
    for path in original.rglob("*"):
        if path.is_file():
            assert sha(path) == sha(snapshot / path.relative_to(original))
    manifest = json.loads((snapshot / "optim/mysql.json").read_text(encoding="utf-8"))
    example = manifest["example"]
    template = (snapshot / "template-mysql/req2test.txt").read_text(encoding="utf-8").strip()
    records = []
    for target in manifest["targets"]:
        name = target["name"]
        output = ROOT / "stage1_src2req" / f"{name}.txt"
        assert output.is_file(), output
        values = {
            "EXAMPLE_REQUIREMENTS": (snapshot / example["requirements"]).read_text(encoding="utf-8").strip(),
            "EXAMPLE_TEST": (snapshot / example["test"]).read_text(encoding="utf-8").strip(),
            "CURRENT_REQUIREMENTS": output.read_text(encoding="utf-8").strip(),
        }
        rendered = re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: values[m.group(1)], template) + "\n"
        dest = ROOT / "stage2_req2test/prompts" / f"{name}.txt"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(rendered.encode("utf-8"))
        stage1_input = snapshot / "Prompts/mysql/src2req" / f"{name}.txt"
        records.append({
            "target": name,
            "src2req_input": str(stage1_input.relative_to(ROOT)).replace("\\", "/"),
            "src2req_input_sha256": sha(stage1_input),
            "src2req_output": str(output.relative_to(ROOT)).replace("\\", "/"),
            "src2req_output_sha256": sha(output),
            "req2test_input": str(dest.relative_to(ROOT)).replace("\\", "/"),
            "req2test_input_sha256": sha(dest),
            "original_seed_replaced": True,
        })
    evidence = {
        "run_id": ROOT.name,
        "generation_date": "2026-11-04",
        "timezone": "Asia/Shanghai",
        "generator": "current Codex assistant, both stages, direct authored outputs in this chat",
        "external_model_api_called": False,
        "database_executed": False,
        "source_branch_coverage": "not_measured",
        "input_hash_entries_verified": len(checks),
        "template_policy": "Preserve the supplied package templates; replace only current requirements with the new stage-one output.",
        "context_policy": "Both stages share this chat context; this is not an isolated dual-model evaluation or a blinded benchmark.",
        "targets": records,
    }
    (ROOT / "generation_manifest.json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(f"Verified {len(checks)} input hashes; rendered {len(records)} stage-two prompts")


if __name__ == "__main__":
    main()
