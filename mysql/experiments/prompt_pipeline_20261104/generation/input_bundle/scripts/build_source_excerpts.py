"""Build numbered excerpts from verified MySQL blobs; no network or SQL execution."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--git-dir", type=Path)
    source.add_argument("--snapshot-dir", type=Path,
                        help="Directory containing <revision>/<upstream path>")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))
    count = 0
    for target in manifest["targets"]:
        revision = target["revision"]
        output = [f'Target: {target["name"]}',
                  f'Target observation: {target["observation"]}',
                  f'Revision: {revision}',
                  f'Parent revision: {target["parent"]}',
                  'Source repository: https://github.com/mysql/mysql-server',
                  'Scope: local excerpts of the target revision; omitted callers/helpers are not assumed known.',
                  'Line numbers below refer to the upstream file at this revision.']
        for entry in target["files"]:
            path = entry["path"]
            if args.snapshot_dir:
                raw = (args.snapshot_dir / revision / path).read_bytes()
            else:
                env = dict(os.environ, GIT_NO_LAZY_FETCH="1")
                raw = subprocess.check_output(
                    ["git", "--git-dir=" + str(args.git_dir), "show", revision + ":" + path], env=env)
            if blob_sha(raw) != entry["blob"]:
                raise ValueError(f"Blob mismatch: {revision}:{path}")
            lines = raw.decode("utf-8").splitlines()
            output.extend(["", f"# Code: {path}", f'Blob: {entry["blob"]}',
                           f"Source: https://github.com/mysql/mysql-server/blob/{revision}/{path}"])
            for start, end in entry["ranges"]:
                if not 1 <= start <= end <= len(lines):
                    raise ValueError(f"Invalid range: {path}:{start}-{end}")
                output.append("```cpp")
                output.extend(f"{number}: {lines[number - 1]}" for number in range(start, end + 1))
                output.append("```")
        content = ("\n".join(output) + "\n").encode("utf-8")
        dest = ROOT / "source-code-data" / "mysql" / (target["name"] + ".txt")
        if args.check:
            if dest.read_bytes() != content:
                raise ValueError(f"Excerpt mismatch: {dest}")
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(content)
        count += 1
    print(f"PASS: {count} source excerpts {'verified' if args.check else 'built'} from exact Git blobs")


if __name__ == "__main__":
    main()
