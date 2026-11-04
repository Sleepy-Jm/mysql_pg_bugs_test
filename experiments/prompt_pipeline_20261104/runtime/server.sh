#!/usr/bin/env bash
set -euo pipefail
run_id="$1"
[[ "$run_id" =~ ^[a-zA-Z0-9_-]+$ ]]
test -f /work/.owned-three-prompt-run
datadir="/work/data/$run_id"
mkdir -p "$datadir"
/runtime/bin/mysqld --no-defaults --initialize-insecure \
  --basedir=/runtime --datadir="$datadir" --lc-messages-dir=/runtime/share \
  --innodb-buffer-pool-size=64M >"/work/logs/init-$run_id.log" 2>&1
exec /runtime/bin/mysqld --no-defaults \
  --basedir=/runtime --datadir="$datadir" --lc-messages-dir=/runtime/share \
  --socket="$datadir/mysql.sock" --pid-file="$datadir/mysql.pid" \
  --log-error="$datadir/server.log" --skip-networking --skip-log-bin \
  --innodb-buffer-pool-size=64M --innodb-redo-log-capacity=64M
