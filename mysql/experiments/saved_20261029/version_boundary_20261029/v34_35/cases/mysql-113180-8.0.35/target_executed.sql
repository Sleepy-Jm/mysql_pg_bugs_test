USE `replay_6af4785fcd6fe5ee54e89fe1`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113180; source: cmain, c538271, c538297
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 INT, c1 INT, PRIMARY KEY(c0));
INSERT INTO t0(c0, c1) VALUES (1, 0);
CREATE UNIQUE INDEX i1 ON t0(c1 , c0 );

SELECT * FROM t0 WHERE SIN(1150199883)=c1; -- 1 0
SELECT * FROM t0 WHERE NOT SIN(1150199883)=c1; -- 1 0

-- Run after the unmodified source script, in the same owned schema; read-only evidence only.
SELECT c0,c1,SIN(1150199883) AS sin_value,SIN(1150199883) IS NULL AS sin_is_null FROM t0;
