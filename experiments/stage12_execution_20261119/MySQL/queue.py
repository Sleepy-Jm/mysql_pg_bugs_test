"""Execute frozen SQL as the exact builds become available on the project server."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
# Ubuntu 22 build image with Python 3 installed for evidence capture.
RUNTIME_IMAGE = "sha256:a97061e0f69e5a6a0c52e53b251758589c7d460778863a49cf944286d96a08b9"


def log_event(case, role, event, **values):
    timestamp = datetime.now(timezone.utc).isoformat()
    print(timestamp, json.dumps(dict(case=case, role=role, event=event, **values)), flush=True)


def run_role(case, role, prefix):
    runner = [str(ROOT / "execute.py"), case, role, str(prefix)]
    library_path = str(prefix / "lib")
    if case == "410f5267d414":
        command = [
            "docker", "run", "--rm", "--network", "none",
            "--cap-drop", "ALL", "--security-opt", "no-new-privileges",
            "--user", f"{os.getuid()}:{os.getgid()}", "--cpus", "2", "--memory", "2g",
            "--tmpfs", "/tmp:rw,nosuid,nodev,mode=1777,size=800m",
            "-v", f"{ROOT}:{ROOT}", "-v", f"{prefix}:{prefix}:ro",
            "-e", "LD_LIBRARY_PATH=" + library_path,
            "--entrypoint", "/usr/bin/python3", RUNTIME_IMAGE, *runner,
        ]
        env = os.environ.copy()
    else:
        command = ["python3", *runner]
        env = {**os.environ, "LD_LIBRARY_PATH": library_path}
    with (ROOT / f"{case}-{role}.log").open("ab") as output:
        process = subprocess.run(command, env=env, stdout=output, stderr=subprocess.STDOUT, timeout=1200)
    return process.returncode


def main():
    builds = Path(sys.argv[1]).resolve() / "runtime"
    plan = json.loads((ROOT / "plan.json").read_text())
    pending = {(entry["case"], role): sha for entry in plan for role, sha in entry["versions"].items()}
    failures = []
    for _ in range(4800):
        for (case, role), sha in list(pending.items()):
            receipt = ROOT / "evidence" / case / role / "results.json"
            if receipt.is_file():
                del pending[case, role]
                continue
            prefix = builds / sha[:12]
            if not (prefix / "SHA256SUMS").is_file():
                continue
            log_event(case, role, "start", commit=sha)
            exit_code = run_role(case, role, prefix)
            log_event(case, role, "finished", exit=exit_code)
            if exit_code or not receipt.is_file():
                failures.append((case, role))
            del pending[case, role]
        if not pending:
            break
        time.sleep(12)
    return int(bool(failures or pending))


if __name__ == "__main__":
    sys.exit(main())
