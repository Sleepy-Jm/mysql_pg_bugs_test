USE `replay_8e9bb22f410fc47fcf71f816`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #111421; source: cmain, c533592
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c1 NUMERIC CHECK (true));
SHOW CREATE TABLE t0;

-- Read-only postcheck appended after unchanged source SQL.
SELECT COUNT(*) AS t0_exists FROM information_schema.tables WHERE table_schema=DATABASE() AND table_name='t0';
