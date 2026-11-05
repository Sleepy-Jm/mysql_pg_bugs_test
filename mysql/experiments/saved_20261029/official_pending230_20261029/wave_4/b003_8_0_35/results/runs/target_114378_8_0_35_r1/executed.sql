USE `replay_291a662e74205abe20b3a38a`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #114378; source: cmain, c542585
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 FLOAT);
INSERT INTO t0(c0) VALUES(-1);

SELECT f1 FROM (SELECT ((t0.c0) ^ (CONVERT_TZ('2001-10-22 16:13:59.9', '-01:00','+00:00'))) AS f1 FROM t0) as t WHERE (f1) > (1);

SELECT f1 FROM (SELECT ((t0.c0) ^ (CONVERT_TZ('2001-10-22 16:13:59.9', '-01:00','+00:00'))) AS f1 FROM t0) as t;

-- Read-only postcheck appended after unchanged source SQL.
SELECT c0 FROM t0; SELECT CONVERT_TZ('2001-10-22 16:13:59.9','-01:00','+00:00');
