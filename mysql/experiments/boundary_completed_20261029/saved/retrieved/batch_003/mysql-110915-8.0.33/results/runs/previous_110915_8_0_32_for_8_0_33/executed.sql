USE `replay_3e4be7e698d9b5d522d5a4f6`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #110915; source anchors: cmain, c532281
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t0(c0 INT,c1 INT,c2 INT);
CREATE TABLE t7(c0 INT,c1 INT,c2 INT);
SELECT 1 FROM t0 JOIN t7 ON TRUE GROUP BY t7.c0,t0.c0 HAVING t7.c0=1;

-- Read-only postcheck appended after unchanged source SQL.
SELECT COUNT(*) AS n FROM t0; SELECT COUNT(*) AS n FROM t7;
