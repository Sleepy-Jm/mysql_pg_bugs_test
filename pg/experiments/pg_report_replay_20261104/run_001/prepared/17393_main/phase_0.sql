Steps in script:
psql -c 'CREATE DATABASE test'
# basebackup
pg_basebackup -D $backup_dir/0
sleep 5
rec_pit=`date +'%Y-%m-%d %H:%M:%S'`
sleep 5
# drop db
psql -c 'DROP DATABASE test'
# save backup
psql -c 'SELECT pg_switch_wal()'
sleep 5
# Stop db
pg_ctl -D $PGDATAstop
# recovery
rm -rf $PGDATA/*
cp -r $backup_dir/0/* $PGDATA/
touch $PGDATA/recovery.signal
echo "recovery_target_time='$rec_pit'" >> $inst_dir/postgresql.conf
# start
pg_ctl -D $PGDATA -l ${log_dir}/pgsql.log start
sleep 5
echo "\c test" | psql;
