USE `replay_a2a76d82f983b5862f838218`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #114380; source anchors: cmain, c541693
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t0(c1 FLOAT) ;
INSERT INTO t0(c1) VALUES(0.1);

SELECT f1 FROM (SELECT (LEAST('-2',  EXISTS (SELECT 1 WHERE FALSE), CAST(t0.c1 AS SIGNED), TIMESTAMP('2024-03-17'))) AS f1 FROM t0) as t WHERE f1;

SELECT f1 FROM (SELECT (LEAST('-2',  EXISTS (SELECT 1 WHERE FALSE), CAST(t0.c1 AS SIGNED), TIMESTAMP('2024-03-17'))) AS f1, (LEAST('-2',  EXISTS (SELECT 1 WHERE FALSE), CAST(t0.c1 AS SIGNED), TIMESTAMP('2024-03-17'))) IS TRUE AS flag FROM t0) as t WHERE flag=1;

-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS loaded_rows FROM t0;
SELECT @@session.sql_mode;
