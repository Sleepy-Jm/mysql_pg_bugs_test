USE `replay_44f34ac75544d76a143994ea`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #110550; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
VALUES ROW(1,1,1), ROW(5,5,5), ROW(4,4,4) ORDER BY column_1;
VALUES ROW(1,1,1), ROW(5,5,5), ROW(4,4,4) UNION VALUES ROW(0,0,0) ORDER BY column_1;
