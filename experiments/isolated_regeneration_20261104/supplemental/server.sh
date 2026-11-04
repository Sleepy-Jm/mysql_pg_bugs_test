#!/bin/bash
set -euo pipefail
rid="$1"
[[ "$rid" =~ ^[0-9a-f]{12}$ ]]
test -f /work/.owned-isolated
datadir="/work/data/$rid"
mkdir -p "$datadir" /work/logs
/runtime/bin/mysqld --no-defaults --initialize-insecure --basedir=/runtime --datadir="$datadir" --lc-messages-dir=/runtime/share --innodb-buffer-pool-size=64M >"/work/logs/init-$rid.log" 2>&1
exec /runtime/bin/mysqld --no-defaults --basedir=/runtime --datadir="$datadir" --lc-messages-dir=/runtime/share --socket="$datadir/mysql.sock" --pid-file="$datadir/mysql.pid" --log-error="$datadir/server.log" --skip-networking --skip-log-bin --innodb-buffer-pool-size=64M --innodb-redo-log-capacity=64M
