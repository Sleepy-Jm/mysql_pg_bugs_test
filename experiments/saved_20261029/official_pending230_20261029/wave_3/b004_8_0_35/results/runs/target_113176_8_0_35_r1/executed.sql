USE `replay_f50f16e811f2d81e7bfde2b7`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113176; source: cmain, c538265
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 DECIMAL  UNIQUE KEY DEFAULT 0.2921954450911477 CHECK((((NULL) NOT IN (NULL)) IS FALSE) IS NOT FALSE) , c1 DECIMAL  UNIQUE PRIMARY KEY NOT NULL) ;

-- Read-only postcheck appended after unchanged source SQL.
SELECT COUNT(*) AS t0_exists FROM information_schema.tables WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='t0';
