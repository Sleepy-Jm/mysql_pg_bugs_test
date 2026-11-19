-- 准备
DROP TABLE IF EXISTS t1_src, t1_dst;
CREATE TABLE t1_src (a DECIMAL(10,2), b DECIMAL(10,2));
CREATE TABLE t1_dst (s VARCHAR(64), d DECIMAL(10,2));
INSERT INTO t1_src VALUES (1.00, 3.00), (2.00, 3.00), (10.00, 3.00);

-- 目标 SELECT：同一表达式分别以字符串和 DECIMAL 消费
SELECT a, b,
       a / b            AS str_form,
       CAST(a / b AS DECIMAL(10,2)) AS cast_form
FROM t1_src ORDER BY a;

-- 对照：存入 DECIMAL 列
INSERT INTO t1_dst (s, d)
SELECT CAST(a / b AS CHAR), a / b FROM t1_src ORDER BY a;
SELECT s, d FROM t1_dst ORDER BY s;

-- 清理
DROP TABLE t1_src, t1_dst;
