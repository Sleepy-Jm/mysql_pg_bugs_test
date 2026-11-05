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
