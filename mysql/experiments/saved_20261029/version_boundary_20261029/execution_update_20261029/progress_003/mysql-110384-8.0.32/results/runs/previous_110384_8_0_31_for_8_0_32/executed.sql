USE `replay_c36f0591b2e182c3b218d528`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
CREATE TABLE t1 (Name VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci);
CREATE TABLE t2 (Name VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci);
INSERT INTO t1(Name) VALUES ('valueテスト');
INSERT INTO t2(Name) VALUES ('テストvalue');
SELECT Name FROM (SELECT Name FROM t1 UNION SELECT Name FROM t2) derived WHERE Name LIKE '%テスト%';
SHOW WARNINGS;
SELECT Name FROM (SELECT Name FROM t1 UNION SELECT Name FROM t2) derived WHERE Name LIKE '%value%';

-- No extra postcheck required by frozen oracle.
