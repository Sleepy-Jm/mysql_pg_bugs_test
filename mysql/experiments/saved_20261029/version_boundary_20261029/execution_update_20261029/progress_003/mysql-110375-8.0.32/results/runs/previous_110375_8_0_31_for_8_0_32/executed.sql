USE `replay_a8ae6671176ef8e942ddfd43`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
SELECT * FROM (SELECT '中国' AS corporation UNION ALL SELECT '法国' AS corporation) t WHERE t.corporation LIKE '%中国%';
SHOW WARNINGS;

-- No extra postcheck required by frozen oracle.
