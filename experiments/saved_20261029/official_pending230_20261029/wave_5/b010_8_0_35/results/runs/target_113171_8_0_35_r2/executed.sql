USE `replay_2fb031dc4fbaaa41dbd40f66`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113171; source: cmain, c538259, c544161
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SELECT @@SESSION.sql_mode;
SELECT SUM(SUBSTRING('text',1,3)) FROM dual;
SHOW WARNINGS;
SELECT SUM(DISTINCT SUBSTRING('text',1,3)) FROM dual;
SHOW WARNINGS;

-- Read-only postchecks for report 113171; run in the same disposable schema/session.
SELECT @@SESSION.sql_mode;
