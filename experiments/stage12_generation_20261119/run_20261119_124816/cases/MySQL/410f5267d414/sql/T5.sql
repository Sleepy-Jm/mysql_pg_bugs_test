-- 准备
DROP TABLE IF EXISTS t5_src, t5_dst;
CREATE TABLE t5_src (a DECIMAL(10,3), b DECIMAL(10,3));
CREATE TABLE t5_dst (s VARCHAR(64), d DECIMAL(10,2));
INSERT INTO t5_src VALUES (1.005, 1.000), (2.005, 1.000), (1.234, 1.000);

-- 目标 SELECT：DECIMAL 乘法，结果声明 scale 可能小于内部 scale
SELECT a, b, a * b AS str_form FROM t5_src ORDER BY a;

-- 对照：存入 DECIMAL(10,2) 列
INSERT INTO t5_dst (s, d)
SELECT CAST(a * b AS CHAR), a * b FROM t5_src ORDER BY a;
SELECT s, d FROM t5_dst ORDER BY s;

-- 清理
DROP TABLE t5_src, t5_dst;
