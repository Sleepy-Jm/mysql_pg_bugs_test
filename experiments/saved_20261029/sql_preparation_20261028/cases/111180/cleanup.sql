-- MySQL report #111180; source: cmain, c532956, c532962, c532963
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET GLOBAL max_binlog_size=@old_max_binlog_size;
SET GLOBAL slow_query_log=@old_slow_query_log;
SET GLOBAL log_output=@old_log_output;
SET GLOBAL long_query_time=@old_long_query_time;
DROP PROCEDURE IF EXISTS insert_test;
DROP TABLE IF EXISTS t1;
