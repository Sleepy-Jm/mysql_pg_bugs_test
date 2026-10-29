USE `replay_ed28f50def5ca1453b2c3a7c`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #110562; source anchors: cmain, c531648
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
VALUES ROW(1,4),ROW(2,1),ROW(3,3) ORDER BY column_1;
SELECT * FROM (VALUES ROW(1,4),ROW(2,1),ROW(3,3)) AS t ORDER BY column_1;

-- No additional postcheck required by the reviewed oracle.
