-- MySQL report #99578; source anchors: cmain, c516255
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE DATABASE test;
CREATE TABLESPACE bad ADD DATAFILE './test/../bad.ibd';
DROP DATABASE test;
set global innodb_buf_flush_list_now=1;
SELECT 1 AS server_alive;
