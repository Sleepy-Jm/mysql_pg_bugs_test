-- 准备
DROP TABLE IF EXISTS t5_t CASCADE;
CREATE TABLE t5_t (a int, b int, c text);
INSERT INTO t5_t VALUES (1,30,'x'),(2,10,'y'),(3,20,'z');
ANALYZE t5_t;

-- 目标 SELECT：平凡子查询 + 外层 ORDER BY 未输出列
SELECT c FROM (SELECT a, b, c FROM t5_t) sub ORDER BY b, c;

-- 对照：等价直接查询
SELECT c FROM t5_t ORDER BY b, c;

-- 清理
DROP TABLE t5_t CASCADE;
