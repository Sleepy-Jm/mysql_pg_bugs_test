USE `replay_6b1c72f245bbe1f845dd6d31`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
SET @@sql_mode = 'ANSI,TRADITIONAL';
SELECT @@sql_mode;
SELECT DATE('2022-04-31');
SELECT STR_TO_DATE('2022-04-31', '%Y-%m-%d');
SELECT DATE(STR_TO_DATE('2022-04-31', '%Y-%m-%d'));

-- No extra postcheck required by frozen oracle.
