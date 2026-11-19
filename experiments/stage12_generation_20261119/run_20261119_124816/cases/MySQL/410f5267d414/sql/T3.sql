-- 准备
DROP TABLE IF EXISTS t3_src, t3_dst;
CREATE TABLE t3_src (a DECIMAL(10,2), d DOUBLE);
CREATE TABLE t3_dst (s VARCHAR(64), r DOUBLE);
INSERT INTO t3_src VALUES (1.00, 3.0), (2.00, 3.0), (5.00, 3.0);

-- 目标 SELECT：含 DOUBLE 操作数，hybrid_type 应为 REAL_RESULT
SELECT a, d, a / d AS str_form FROM t3_src ORDER BY a;

-- 对照：存入 DOUBLE 列
INSERT INTO t3_dst (s, r)
SELECT CAST(a / d AS CHAR), a / d FROM t3_src ORDER BY a;
SELECT s, r FROM t3_dst ORDER BY s;

-- 清理
DROP TABLE t3_src, t3_dst;
