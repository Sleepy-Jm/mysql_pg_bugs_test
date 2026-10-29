USE `replay_1a9089930181cfcbe202d69f`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #114196; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE IF NOT EXISTS t0(c0 DECIMAL);
REPLACE INTO t0(c0) VALUES(0.1);

SELECT t0.c0 FROM t0 WHERE t0.c0 <= - 0.8;

SELECT (t0.c0 <= - 0.8) IS TRUE AS flag FROM t0;
SELECT * FROM t0;
