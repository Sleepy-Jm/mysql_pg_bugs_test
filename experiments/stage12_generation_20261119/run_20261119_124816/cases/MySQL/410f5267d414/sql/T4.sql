-- 准备
DROP TABLE IF EXISTS t4_src, t4_dst;
CREATE TABLE t4_src (a INT, b INT);
CREATE TABLE t4_dst (s VARCHAR(64), i INT);
INSERT INTO t4_src VALUES (1, 3), (2, 3), (10, 3);

-- 目标 SELECT：INT 除法，hybrid_type 应为 INT_RESULT
SELECT a, b, a / b AS str_form FROM t4_src ORDER BY a;

-- 对照：存入 INT 列
INSERT INTO t4_dst (s, i)
SELECT CAST(a / b AS CHAR), a / b FROM t4_src ORDER BY a;
SELECT s, i FROM t4_dst ORDER BY s;

-- 清理
DROP TABLE t4_src, t4_dst;
