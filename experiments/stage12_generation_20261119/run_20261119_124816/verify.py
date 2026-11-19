"""Verify the completed two-stage run offline, without importing the generator."""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


RUN = Path(__file__).resolve().parent
REPO = RUN.parents[2]
INPUTS = Path("experiments/stage1_commit_inputs_20261119/model-inputs")
PIN = "52c57a9dc837e78b40cd401ef453521766774948"
MODELS = ("deepseek-v4-pro", "deepseek-flash")
DBS = {"MySQL": "MySQL", "PG": "PostgreSQL", "SQLite": "SQLite"}


def check(condition, message):
    if not condition:
        raise ValueError(message)


def same_set(actual, expected, label):
    check(actual == expected, f"{label}: missing={sorted(expected - actual)}, extra={sorted(actual - expected)}")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output([
        "git", "--no-lazy-fetch", "-c", f"safe.directory={REPO.as_posix()}", "-C", str(REPO), *args,
    ])


def read_json(path):
    return json.loads(path.read_bytes())


def verify_stage(case, stage, user):
    receipt = read_json(case / f"stage{stage}-receipt.json")
    output = (case / f"stage{stage}-output.md").read_bytes()
    model = MODELS[stage - 1]
    label = f"{case.parent.name}/{case.name} stage {stage}"
    options = receipt["options"]
    returned = receipt["returned"]
    check(receipt["stage"] == stage and receipt["status"] == "success", f"{label}: unsuccessful receipt")
    check(options["model"] == returned["model"] == model, f"{label}: requested or returned model")
    check(returned["finish_reason"] == "stop" and returned["stream_done"] is True, f"{label}: incomplete stream")
    check(receipt["input_sha256"] == sha(user.encode("utf-8")), f"{label}: input hash")
    request = {**options, "messages": [{"role": "user", "content": user}]}
    wire_bytes = json.dumps(request, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    check(receipt["request_sha256"] == sha(wire_bytes), f"{label}: request body hash")
    check(output.strip() and receipt["output_sha256"] == sha(output), f"{label}: output hash or empty output")
    attempt = case / "attempts" / f"stage{stage}-{receipt['attempt']:02d}.json"
    check(read_json(attempt) == receipt, f"{label}: successful attempt differs from final receipt")
    return output


def sql_blocks(output):
    """Read Markdown line by line, preserving all bytes between each SQL fence."""
    blocks = {}
    heading = fence_length = 0
    body = []
    for line in output.splitlines(keepends=True):
        stripped = line.strip(b" \t\r\n")
        if fence_length:
            if len(stripped) >= fence_length and stripped == b"`" * len(stripped):
                sql = b"".join(body)
                check(sql.strip(), f"T{heading}: empty SQL fence")
                blocks[f"T{heading}.sql"] = sql
                fence_length = 0
            else:
                body.append(line)
            continue
        title = re.match(rb"^#{1,6}[ \t]+\**T([0-9]+)\b", line, re.I)
        if title:
            check(heading == len(blocks), f"T{heading}: missing SQL fence")
            heading += 1
            check(title[1] == str(heading).encode() and heading <= 5, "unexpected T heading")
        opener = re.fullmatch(rb"(`{3,})sql", stripped, re.I)
        if opener:
            check(heading == len(blocks) + 1, "extra SQL fence or missing T heading")
            fence_length = len(opener[1])
            body = []
    check(not fence_length and heading == len(blocks) and blocks, "missing or unfinished SQL fence")
    return blocks


def verify():
    manifest = read_json(RUN / "run.json")
    template = (RUN / "stage2-template.md").read_bytes()
    check(manifest["run_id"] == RUN.name and manifest["frozen_input_commit"] == PIN, "run ID or frozen commit")
    check(manifest["requested_models"] == list(MODELS), "manifest models")
    check(manifest["ended_utc"] and not manifest["errors"] and manifest["sql_executed"] is False, "manifest status")
    check(manifest["stage2_template_sha256"] == sha(template), "stage 2 template hash")
    template = template.decode("utf-8")
    check(template.count("{{STAGE1_OUTPUT}}") == 1 and "{{DB}}" in template, "stage 2 template placeholders")

    tree = git("ls-tree", "-rz", "--name-only", PIN, "--", INPUTS.as_posix()).split(b"\0")
    paths = [Path(name.decode("utf-8")).relative_to(INPUTS) for name in tree if name]
    check(len(paths) == 12 and all(len(p.parts) == 2 and p.suffix == ".md" for p in paths), "frozen input file set")
    check(all(sum(p.parent.name == db for p in paths) == 4 for db in DBS), "expected four frozen inputs per database")
    input_root = REPO / INPUTS
    same_set({p.relative_to(input_root) for p in input_root.rglob("*.md")}, set(paths), "input files")
    expected_cases = {p.with_suffix("").as_posix() for p in paths}
    cases = RUN / "cases"
    same_set({p.relative_to(cases).as_posix() for p in cases.glob("*/*") if p.is_dir()}, expected_cases, "case directories")
    same_set(set(manifest["case_counts"]), expected_cases, "manifest cases")

    scripts = set()
    for path in sorted(paths):
        tag = path.with_suffix("").as_posix()
        case = cases / tag
        frozen = git("show", f"{PIN}:{(INPUTS / path).as_posix()}")
        check((input_root / path).read_bytes() == frozen, f"{tag}: local input differs from pinned blob")
        first = verify_stage(case, 1, frozen.decode("utf-8"))
        handoff = template.replace("{{DB}}", DBS[path.parent.name]).replace("{{STAGE1_OUTPUT}}", first.decode("utf-8"))
        second = verify_stage(case, 2, handoff)
        try:
            blocks = sql_blocks(second)
        except ValueError as exc:
            raise ValueError(f"{tag}: {exc}") from exc
        check(manifest["case_counts"][tag] == len(blocks), f"{tag}: manifest script count")
        for name, expected in blocks.items():
            script = case / "sql" / name
            check(script.read_bytes() == expected, f"{tag}/{name}: differs from fenced bytes")
            scripts.add(script.relative_to(RUN).as_posix())
    same_set({p.relative_to(RUN).as_posix() for p in RUN.rglob("*") if p.is_file() and p.suffix.lower() == ".sql"}, scripts, "SQL files")
    print(f"Verified {len(paths)} pinned inputs, {2 * len(paths)} completed calls, {len(paths)} full handoffs and {len(scripts)} SQL files.")


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    try:
        verify()
    except (ValueError, KeyError, TypeError, OSError, subprocess.CalledProcessError) as error:
        sys.exit(f"Verification failed: {error}")
