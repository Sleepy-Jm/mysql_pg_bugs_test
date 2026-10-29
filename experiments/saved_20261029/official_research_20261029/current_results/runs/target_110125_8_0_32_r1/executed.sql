USE `replay_1af9253bea27c3c72d470b78`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #110125; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE IF NOT EXISTS t0(c0 DOUBLE ZEROFILL) ;
CREATE INDEX i0 ON t0(c0 DESC);
INSERT DELAYED IGNORE INTO t0(c0) VALUES(0);

SELECT c0 FROM t0 WHERE (IFNULL(-1123870957, '')) IN (t0.c0); -- 0

-- Run after the unmodified source script, in the same owned schema; read-only evidence only.
SELECT COUNT(*) AS loaded_rows,MIN(c0+0) AS min_value,MAX(c0+0) AS max_value FROM t0;
