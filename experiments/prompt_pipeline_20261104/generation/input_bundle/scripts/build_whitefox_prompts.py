"""Render one-shot MySQL prompts offline; no LLM calls or database execution."""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r"\{\{([A-Z_]+)\}\}")


def read(path):
    return (ROOT / path).read_text(encoding="utf-8").strip()


def render(template, values):
    names = set(TOKEN.findall(template))
    if names != set(values):
        raise ValueError(f"Template fields differ: {names ^ set(values)}")
    # Single-pass substitution preserves braces inside SQL, JSON and source code.
    return TOKEN.sub(lambda match: values[match.group(1)], template).rstrip() + "\n"


def build():
    manifest = json.loads(read("optim/mysql.json"))
    example = manifest["example"]
    common = {"EXAMPLE_REQUIREMENTS": read(example["requirements"])}
    templates = {stage: read(f"template-mysql/{stage}.txt")
                 for stage in ("src2req", "req2test")}
    outputs = {}
    for target in manifest["targets"]:
        name = target["name"]
        if not re.fullmatch(r"[a-z0-9_]+", name):
            raise ValueError(f"Invalid target name: {name}")
        for stage, values in (
            ("src2req", {**common,
                         "EXAMPLE_SOURCE": read(example["source"]),
                         "CURRENT_SOURCE": read(target["source"])}),
            ("req2test", {**common,
                          "EXAMPLE_TEST": read(example["test"]),
                          "CURRENT_REQUIREMENTS": read(target["requirements"])}),
        ):
            path = ROOT / "Prompts" / "mysql" / stage / f"{name}.txt"
            if path in outputs:
                raise ValueError(f"Duplicate target: {name}")
            outputs[path] = render(templates[stage], values)
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="Check committed prompts without writing files")
    args = parser.parse_args()
    outputs = build()
    if args.check:
        actual = set((ROOT / "Prompts" / "mysql").glob("*/*.txt"))
        mismatched = [p for p, content in outputs.items()
                      if not p.exists() or p.read_bytes() != content.encode("utf-8")]
        extra = actual - outputs.keys()
        if mismatched or extra:
            for path in sorted(set(mismatched) | extra):
                print(f"MISMATCH: {path.relative_to(ROOT)}")
            raise SystemExit(1)
        print(f"PASS: {len(outputs)} prompts match templates and target inputs")
    else:
        for path, content in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content.encode("utf-8"))
        print(f"Rendered {len(outputs)} prompts")


if __name__ == "__main__":
    main()
