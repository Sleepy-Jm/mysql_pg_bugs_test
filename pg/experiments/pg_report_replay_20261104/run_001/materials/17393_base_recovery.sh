#!/bin/bash

rt="\n\e[31m"
wt="\e[0m"

# set base directory for testing
basis_dir=${HOME}/pg_test

pg_bin=/usr/pgsql-13/bin/

# Verzeichnisse
inst_dir=${basis_dir}/inst
backup_dir=${basis_dir}/backup
wal_backup_dir=${basis_dir}/wal_backup
log_dir=${basis_dir}/log_dir

# Path setzen
export PATH=$pg_bin:$PATH

# stop if it still running,  cleanup old files

echo -e $rt `date` "Cleanup ..." $wt
pg_ctl -D $inst_dir stop &> /dev/null
mkdir -p $inst_dir $backup_dir $wal_backup_dir $log_dir ${basis_dir}/run
rm -rf $inst_dir/* $backup_dir/* $wal_backup_dir/* $log_dir/*

echo -e $rt `date` "Create and start new postgres instance ..." $wt
# Init Postgresql
initdb -D $inst_dir

# Config for wal backup + recovery
echo "port=5555" >> $inst_dir/postgresql.conf
echo "archive_mode = on" >> $inst_dir/postgresql.conf
echo "archive_command = 'test ! -f $wal_backup_dir/%f && cp %p $wal_backup_dir/%f'" >> $inst_dir/postgresql.conf
echo "restore_command = 'cp $wal_backup_dir/%f %p'" >> $inst_dir/postgresql.conf
echo "unix_socket_directories = '${basis_dir}/run'" >> $inst_dir/postgresql.conf
echo "log_directory = '${log_dir}'" >> $inst_dir/postgresql.conf
echo "lc_messages = 'en_US.utf-8'" >> $inst_dir/postgresql.conf


# start database
pg_ctl -D $inst_dir -l ${basis_dir}/log_dir/pgsql.log start

# set env
export PGDATA=$inst_dir
export PGPORT=5555
export PGDATABASE=postgres
export PGUSER=${USER}
export PGHOST=${basis_dir}/run

#  create a db
echo -e $rt `date` "Create database test ..." $wt
psql -c 'CREATE DATABASE test'
echo -e $rt `date` "What is the oid for datafiles ? ..." $wt
psql -c "SELECT datname, oid FROM pg_database WHERE datname='test'"
echo -e $rt `date` "Looking for datafiles, oid in base-directory ..." $wt
ls -la $inst_dir/base

# basebackup
echo -e $rt `date` "Create basebackup ..." $wt
pg_basebackup -D $backup_dir/0
sleep 5

rec_pit=`date +'%Y-%m-%d %H:%M:%S'`
echo -e $rt `date` "saved date for Point-In-Time where database test still exists: $rec_pit" $wt
echo -e $rt `date` "wait some seconds ..." $wt
sleep 5

echo -e $rt `date` "drop the database test ..." $wt
# Drop DB
psql -c 'DROP DATABASE test'

# pg_switch_wal(); - to save latest log
echo -e $rt `date` "Switch wal to save all changes to wal-backup directory we need for complete recovery ..." $wt
psql -c 'SELECT pg_switch_wal()'
echo -e $rt `date` "The datafiles of database test are deleted - ok, it was dropped" $wt
ls -la $inst_dir/base
sleep 5

echo -e $rt `date` "Stop db ..." $wt
# Stop db
pg_ctl -D $inst_dir stop

echo -e $rt `date` "remove PGDATA and start recovery to $rec_pit (before deletion) ..." $wt
# recovery of basebackup
rm -rf $inst_dir/* # remove PGDATA
cp -r $backup_dir/0/* $inst_dir/ # copy back basebackup
touch $inst_dir/recovery.signal # set to start revovery aufter startup
echo "recovery_target_time='$rec_pit'" >> $inst_dir/postgresql.conf # set time whare all OK
# echo "recovery_target_name='stopping day 0'" >> $inst_dir/postgresql.conf # if I have a target name it works 
echo -e $rt `date` "Check datafiles of test (before start recover with wal) ... - ok there are the datafiles of our database test" $wt
ls -la $inst_dir/base

echo -e $rt `date` "Start restored instance which starts the recovery from wal files ..." $wt
# starten der Instanz
pg_ctl -D $inst_dir -l ${log_dir}/pgsql.log start

sleep 5 # wait to get finish start + recovery
echo -e $rt `date` "Show databases and try to connect to ..." $wt
echo "\l" | psql
echo "\c test" | psql

echo -e $rt `date` "Check datafiles of test ... - there are missing datafiles" $wt
ls -la $inst_dir/base

echo -e $rt `date` "Check the logs what's happened ..." $wt
cat ${log_dir}/*.log

echo -e $rt `date` "Postgresql knows the Database test but don't have the datafiles anymore." $wt
