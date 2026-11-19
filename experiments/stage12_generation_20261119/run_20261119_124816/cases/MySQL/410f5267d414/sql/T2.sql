-- 准备
DROP TABLE IF EXISTS t2_src, t2_dst;
CREATE TABLE t2_src (a DECIMAL(10,2), b DECIMAL(10,2));
CREATE TABLE t2_dst (s VARCHAR(64), r DOUBLE);
INSERT INTO t2_src VALUES (1.00, 3.00), (2.00, 3.00), (5.00, 3.00);

-- 目标 SELECT：字符串形式
SELECT a, b, a / b AS str_form FROM t2_src ORDER BY a;

-- 对照：存入 DOUBLE 列（走 val_real）
INSERT INTO t2_dst (s, r)
SELECT CAST(a / b AS CHAR), a / b FROM t2_src ORDER BY a;
SELECT s, r FROM t2_dst ORDER BY s;

-- 清理
DROP TABLE t2_src, t2_dst;
