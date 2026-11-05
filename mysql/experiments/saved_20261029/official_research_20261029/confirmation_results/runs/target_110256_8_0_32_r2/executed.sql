USE `replay_3f785e089f1ff2c149f701ba`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #110256; source anchors: cmain, c530389
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t0(c0 DECIMAL) ;
INSERT DELAYED IGNORE INTO t0(c0) VALUES('');
CREATE INDEX i0 ON t0(c0 DESC);
SELECT ALL t0.c0 FROM t0 WHERE (t0.c0) = (LEAST('1507214118', "0W*-+	U0")); 
DROP INDEX i0 ON t0;
SELECT ALL t0.c0 FROM t0 WHERE (t0.c0) = (LEAST('1507214118', "0W*-+	U0"));

-- Run after the unmodified source script, in the same owned schema; read-only evidence only.
SELECT COUNT(*) AS loaded_rows,MIN(c0) AS min_value,MAX(c0) AS max_value FROM t0;
