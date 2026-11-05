USE `replay_e24f10305cbff577721d5e83`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #110341; source anchors: cmain, c530604, c530617
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SELECT VERSION(); 

SET @p1 = '2023-02-03', @p2='2023-02-25';

CREATE TABLE t1 (
    created_at DATE
) ;

INSERT INTO t1 VALUES (@p1), (@p2);

SET @s = "select * from t1 where created_at in (?, ?)";

PREPARE stmt FROM @s;

EXECUTE stmt USING @p1, @p2; -- returns 2 rows as expected

SELECT FOUND_ROWS(); -- returns count of 2 as expected

DEALLOCATE PREPARE stmt;

CREATE TABLE t2 (
    created_at DATE
) 
PARTITION BY RANGE (DAYOFMONTH(created_at)) (
    PARTITION p1 VALUES LESS THAN (16), 
    PARTITION p2 VALUES LESS THAN MAXVALUE
);

INSERT INTO t2 VALUES (@p1), (@p2);

SET @s = "select * from t2 where created_at in (?, ?)";

PREPARE stmt FROM @s;

EXECUTE stmt USING @p1, @p2; -- returns 2 rows as expected

SELECT FOUND_ROWS(); -- returns count of 0, this is incorrect

DEALLOCATE PREPARE stmt;

-- Read-only postcheck appended after unchanged source SQL.
SELECT COUNT(*) AS n,MIN(created_at) AS lo,MAX(created_at) AS hi FROM t1;
SELECT COUNT(*) AS n,MIN(created_at) AS lo,MAX(created_at) AS hi FROM t2;
