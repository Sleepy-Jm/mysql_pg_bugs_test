-- MySQL report #111180; source: cmain, c532956, c532962, c532963
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t1(id INT,name VARCHAR(20));
SET @old_max_binlog_size=@@GLOBAL.max_binlog_size;
SET @old_slow_query_log=@@GLOBAL.slow_query_log;
SET @old_log_output=@@GLOBAL.log_output;
SET @old_long_query_time=@@GLOBAL.long_query_time;
SET GLOBAL max_binlog_size=4096;
SET GLOBAL slow_query_log=ON;
SET GLOBAL log_output='TABLE';
SET GLOBAL long_query_time=1;
SELECT @@GLOBAL.gtid_mode,@@GLOBAL.binlog_format,@@GLOBAL.log_bin;
