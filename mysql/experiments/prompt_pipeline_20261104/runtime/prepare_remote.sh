#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
test -f .owned-three-prompt-run
old=/CACHE_ROOT/mysql-intro-bisect-20261103
test -z "$(git -C "$old/repo" status --porcelain --untracked-files=no)"
test ! -e repo
test ! -e build
mkdir -p logs results runtime data
# Independent copy-on-write snapshots when supported; never hardlinks.
cp -a --reflink=auto "$old/repo" ./repo
cp -a --reflink=auto "$old/build" ./build
git -C repo status --porcelain --untracked-files=no
printf 'SOURCE_AND_BUILD_SNAPSHOT_READY\n'
