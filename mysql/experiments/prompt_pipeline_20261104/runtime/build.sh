#!/usr/bin/env bash
set -euo pipefail
label="$1"
[[ "$label" =~ ^[0-9a-f]{12}$ ]]
test -f /work/.owned-three-prompt-run
cd /work
cmake -S repo -B build -G 'Unix Makefiles' \
  -DCMAKE_BUILD_TYPE=Release \
  -DWITH_BOOST=/work/downloads -DDOWNLOAD_BOOST=OFF \
  -DWITH_UNIT_TESTS=OFF -DWITH_ROUTER=OFF -DWITH_MYSQLX=OFF \
  -DWITH_NDBCLUSTER=OFF -DWITH_DEBUG=OFF \
  -DWITH_SSL=system -DWITH_ZLIB=bundled
cmake --build build --target mysqld mysql mysqladmin --parallel 8
mkdir -p "runtime/$label/bin"
cp build/runtime_output_directory/{mysqld,mysql,mysqladmin} "runtime/$label/bin/"
cp -a build/share "runtime/$label/"
"runtime/$label/bin/mysqld" --version
