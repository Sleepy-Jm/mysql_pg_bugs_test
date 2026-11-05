USE `replay_bb236a75b83b225a821fdd5d`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113301; source: cmain, c538587, c554594
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE test_time(id_col int,`time_6` time(6) DEFAULT '01:01:01.000000', `time_0` time);
insert into test_time(id_col,time_6,time_0) values
(31,'07:59:59.000000', '07:59:59'),
(32,'07:59:59.000000', '07:59:59'),
(51,'00:00:00.000000', '00:00:00'),
(52,'00:00:00.000000', '00:00:00'),
(71,'06:06:06.000000', '06:06:06'),
(72,'06:06:06.000000', '06:06:06');

prepare stmt from "SELECT id_col,time_6,time_0 FROM test_time WHERE test_time.time_6 IN (?, '06:06:06.000000','00:00:00');";
set @time_val='07:59:59';
execute stmt USING @time_val;
SELECT id_col,time_6,time_0 FROM test_time WHERE time_6 IN ('07:59:59','06:06:06.000000','00:00:00');
DEALLOCATE PREPARE stmt;
PREPARE stmt0 FROM "SELECT id_col,time_6,time_0 FROM test_time WHERE time_0 IN (?, '06:06:06.000000','00:00:00');";
EXECUTE stmt0 USING @time_val;
SELECT id_col,time_6,time_0 FROM test_time WHERE time_0 IN ('07:59:59','06:06:06.000000','00:00:00');
DEALLOCATE PREPARE stmt0;

-- Read-only postchecks for report 113301; run in the same disposable schema/session.
SELECT id_col,time_6,time_0 FROM test_time ORDER BY id_col; SELECT @@sql_mode;
