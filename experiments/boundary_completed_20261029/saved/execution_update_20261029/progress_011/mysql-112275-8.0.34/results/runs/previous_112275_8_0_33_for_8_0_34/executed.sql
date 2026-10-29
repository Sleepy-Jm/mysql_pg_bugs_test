USE `replay_b3423290fc3a86b45e05c107`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #112275; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TEMPORARY TABLE temp(id INTEGER,name VARCHAR(100));
CREATE TABLE normal(id INTEGER,name VARCHAR(100));
SHOW COLUMNS FROM temp;
SHOW COLUMNS FROM normal;

-- No additional postcheck required by the reviewed oracle.
