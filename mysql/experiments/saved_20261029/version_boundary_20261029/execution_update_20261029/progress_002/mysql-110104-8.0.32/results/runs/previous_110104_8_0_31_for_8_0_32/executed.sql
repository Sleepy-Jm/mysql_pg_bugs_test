USE `replay_860396cc8ec97c4ce6d34522`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
SET NAMES utf8mb4;
CREATE TABLE test_1(id INT,NAME VARCHAR(100));
CREATE TABLE test_2(id INT,NAME VARCHAR(100));
INSERT INTO test_1 VALUES(1,'aaa'),(2,'bbb'),(3,'ccc'),(4,'ddd'),(5,'测试');
INSERT INTO test_2 VALUES(11,'eee');
SELECT * FROM (SELECT * FROM test_1 WHERE NAME='测试' UNION SELECT * FROM test_2 WHERE NAME='bbb') tmp;
SELECT * FROM (SELECT * FROM test_1 WHERE NAME='测试' UNION SELECT * FROM test_2 WHERE NAME='bbb') tmp WHERE NAME='测试';
SET optimizer_switch='derived_condition_pushdown=off';
SELECT * FROM (SELECT * FROM test_1 WHERE NAME='测试' UNION SELECT * FROM test_2 WHERE NAME='bbb') tmp WHERE NAME='测试';

-- No extra postcheck required by frozen oracle.
