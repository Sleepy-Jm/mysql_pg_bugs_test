"""Transfer this task's frozen bundle/evidence over the established SSH host."""
import argparse
import base64
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tarfile

SSH = ['ssh', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=15', '-o',
       'StrictHostKeyChecking=yes', '-o', 'ClearAllForwardings=yes', 'dufei@47.108.211.69']

def call(code, timeout=120):
    p = subprocess.run(SSH + ['python3 -'], input=code.encode(), capture_output=True, timeout=timeout)
    if p.returncode:
        raise RuntimeError(p.stderr.decode(errors='replace'))
    return p.stdout

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['upload', 'run', 'download'])
    parser.add_argument('--run', type=Path, required=True)
    args = parser.parse_args()
    bundle = args.run / 'bundle'
    manifest = json.loads((bundle/'batch_manifest.json').read_text(encoding='utf-8'))
    remote = manifest['remote_root']
    if not remote.startswith('/mnt/sdb/dufei/mysql_source_replay_') or any(c not in '/_-.0123456789abcdefghijklmnopqrstuvwxyz' for c in remote):
        raise ValueError('Unexpected remote task directory')
    if args.action == 'upload':
        files = {p.relative_to(bundle).as_posix(): base64.b64encode(p.read_bytes()).decode()
                 for p in bundle.rglob('*') if p.is_file()}
        code = "import base64,json\nfrom pathlib import Path\n"
        code += f"root=Path({remote!r});root.mkdir(exist_ok=True)\nfiles=json.loads({json.dumps(files)!r})\n"
        code += "for old in root.rglob('*'):\n if old.is_file():\n  key=old.relative_to(root).as_posix()\n  assert key in files and old.read_bytes()==base64.b64decode(files[key]), 'Existing remote content differs'\n"
        code += "for name,data in files.items():\n p=root/name\n assert root.resolve() in p.resolve().parents\n p.parent.mkdir(parents=True,exist_ok=True)\n if not p.exists():p.write_bytes(base64.b64decode(data))\nprint('Uploaded/verified',len(files),'files')\n"
        print(call(code).decode())
    elif args.action == 'run':
        # This stays attached; a dropped SSH session is not reported as success.
        p = subprocess.run(SSH + [f'python3 -u -B {remote}/run_batch.py'])
        raise SystemExit(p.returncode)
    else:
        code = "import io,sys,tarfile\nfrom pathlib import Path\n"
        code += f"root=Path({remote!r})\nbuf=io.BytesIO()\n"
        code += "with tarfile.open(fileobj=buf,mode='w:gz') as t:\n"
        code += " for p in root.rglob('*'):\n  if p.is_file() and '__pycache__' not in p.parts:t.add(p,arcname=p.relative_to(root),recursive=False)\nsys.stdout.buffer.write(buf.getvalue())\n"
        raw = call(code)
        dest = args.run / 'server_evidence'
        dest.mkdir(exist_ok=False)
        with tarfile.open(fileobj=io.BytesIO(raw),mode='r:gz') as t:
            for m in t.getmembers():
                p=dest/m.name
                if not m.isfile() or not p.resolve().is_relative_to(dest.resolve()):
                    raise ValueError('Unsafe evidence archive member')
                p.parent.mkdir(parents=True,exist_ok=True)
                p.write_bytes(t.extractfile(m).read())
        (args.run/'transfer_manifest.json').write_text(json.dumps({
            'server':manifest['server'],'remote_root':remote,
            'archive_sha256':hashlib.sha256(raw).hexdigest(),
            'files':{p.relative_to(dest).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in dest.rglob('*') if p.is_file()}},indent=2),encoding='utf-8')
        print('Evidence saved:',dest)

if __name__ == '__main__':
    main()
