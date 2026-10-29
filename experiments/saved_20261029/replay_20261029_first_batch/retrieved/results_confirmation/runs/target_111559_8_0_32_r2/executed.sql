USE `replay_2c7bf3f61e934940db810ef7`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #111559; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE VIEW v0 (c0) AS (WITH x(x) AS (SELECT 1), y(y) AS (SELECT 1) SELECT 1 FROM x);
SELECT 1 FROM v0;
SHOW CREATE VIEW v0;
