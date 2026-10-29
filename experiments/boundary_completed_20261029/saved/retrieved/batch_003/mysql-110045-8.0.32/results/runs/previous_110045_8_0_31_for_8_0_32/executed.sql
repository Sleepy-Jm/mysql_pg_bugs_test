USE `replay_85f6396ffdf97cb2bdbfb5bf`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #110045; source: cmain, c554980
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SELECT STATEMENT_DIGEST_TEXT('SELECT -1 WHERE 1 = 1');
SELECT STATEMENT_DIGEST_TEXT('SELECT -1 WHERE 1 = -1');

-- No additional postcheck required by the reviewed oracle.
