USE `replay_78ac1b034e509d60aabfbe01`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
SET NAMES utf8mb4;
CREATE TABLE TEST_01 (编号 INT(2),动物 VARCHAR(20));
INSERT INTO TEST_01(编号,动物) VALUES(1,'牛');
CREATE TABLE TEST_02 (编号 INT(2),动物 VARCHAR(20));
INSERT INTO TEST_02(编号,动物) VALUES(2,'羊');
CREATE VIEW TEST_V AS SELECT 编号,动物 FROM TEST_01 UNION ALL SELECT 编号,动物 FROM TEST_02;
SELECT * FROM TEST_V WHERE 动物='牛';
SET optimizer_switch='derived_condition_pushdown=off';
SELECT * FROM TEST_V WHERE 动物='牛';

-- No extra postcheck required by frozen oracle.
