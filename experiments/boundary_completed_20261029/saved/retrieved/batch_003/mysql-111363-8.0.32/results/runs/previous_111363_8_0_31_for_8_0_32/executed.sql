USE `replay_d9d7bfa37d44df1a5f42dcce`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
SET NAMES utf8mb4;
SELECT @@optimizer_switch;
CREATE TABLE TEST01(A VARCHAR(4));
INSERT INTO TEST01(A) VALUES ('あ');
SELECT * FROM (SELECT A FROM TEST01 UNION ALL SELECT A FROM TEST01) SUB WHERE SUB.A='あ';
SHOW WARNINGS;
SET optimizer_switch='derived_condition_pushdown=off';
SELECT * FROM (SELECT A FROM TEST01 UNION ALL SELECT A FROM TEST01) SUB WHERE SUB.A='あ';

-- No extra postcheck required by frozen oracle.
