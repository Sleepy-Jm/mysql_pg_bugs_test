-- 准备
DROP TABLE IF EXISTS t1_p CASCADE;
CREATE TABLE t1_p (k int, v int, s text) PARTITION BY RANGE (k);
CREATE TABLE t1_p1 PARTITION OF t1_p FOR VALUES FROM (0) TO (10);
INSERT INTO t1_p VALUES (1,30,'a'),(2,10,'b'),(3,20,'c'),(4,10,'d');
ANALYZE t1_p;

-- 目标 SELECT：单子 Append，ORDER BY 未输出列 v
SELECT s FROM t1_p WHERE k < 10 ORDER BY v, s;

-- 对照：直接查唯一 child
SELECT s FROM t1_p1 WHERE k < 10 ORDER BY v, s;

-- 清理
DROP TABLE t1_p CASCADE;
