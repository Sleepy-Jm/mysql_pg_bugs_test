USE `replay_7bfa2cf7dabb219bce9e65d8`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #110984; source anchors: cmain, c544757
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET NAMES utf8mb4 COLLATE utf8mb4_0900_ai_ci;
CREATE TABLE t1(flowid VARCHAR(32)) CHARSET=gbk COLLATE=gbk_bin;
INSERT INTO t1 VALUES('xxx');
SELECT CONCAT(abc,flowid) FROM (SELECT 'yyy-' AS abc,flowid FROM t1) AS alias;
SELECT CONCAT(abc,flowid) FROM (SELECT 'yyy-' AS abc,flowid FROM t1 LIMIT 1) AS alias;

-- Read-only postcheck appended after unchanged source SQL.
SELECT flowid,CHARSET(flowid) AS cs,COLLATION(flowid) AS coll FROM t1;
