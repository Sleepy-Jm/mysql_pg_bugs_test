SET NAMES utf8mb4;
CREATE TABLE test_1(id INT,NAME VARCHAR(100));
CREATE TABLE test_2(id INT,NAME VARCHAR(100));
INSERT INTO test_1 VALUES(1,'aaa'),(2,'bbb'),(3,'ccc'),(4,'ddd'),(5,'测试');
INSERT INTO test_2 VALUES(11,'eee');
SELECT * FROM (SELECT * FROM test_1 WHERE NAME='测试' UNION SELECT * FROM test_2 WHERE NAME='bbb') tmp;
SELECT * FROM (SELECT * FROM test_1 WHERE NAME='测试' UNION SELECT * FROM test_2 WHERE NAME='bbb') tmp WHERE NAME='测试';
SET optimizer_switch='derived_condition_pushdown=off';
SELECT * FROM (SELECT * FROM test_1 WHERE NAME='测试' UNION SELECT * FROM test_2 WHERE NAME='bbb') tmp WHERE NAME='测试';
