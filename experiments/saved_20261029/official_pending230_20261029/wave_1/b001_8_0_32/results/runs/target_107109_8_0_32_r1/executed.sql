USE `replay_ae1b94b3237146b227e8d0cc`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #107109; source anchors: cmain
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET SESSION optimizer_switch='semijoin=on';
SET NAMES utf8mb4;
SELECT /*+ SET_VAR(optimizer_switch='semijoin=off') */ @@optimizer_switch;
SHOW WARNINGS;
SET NAMES utf8mb3;
SELECT /*+ SET_VAR(optimizer_switch='semijoin=off') */ @@optimizer_switch;
SHOW WARNINGS;

-- Read-only postcheck appended after unchanged source SQL.
SELECT @@character_set_system AS system_charset,@@character_set_client AS final_client_charset;
