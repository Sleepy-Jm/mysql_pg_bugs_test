USE `replay_55c00e706b4b8bfb7dcd603e`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113302; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t0(c0 INT, c1 INT);
INSERT INTO t0(c1, c0) VALUES(0, 1);

SELECT * FROM t0 WHERE t0.c1 IN (GREATEST(0.1, 0.2)); -- empty result
CREATE INDEX i0 ON t0(c1);
SELECT * FROM t0 WHERE t0.c1 IN (GREATEST(0.1, 0.2)); -- {1|0}
