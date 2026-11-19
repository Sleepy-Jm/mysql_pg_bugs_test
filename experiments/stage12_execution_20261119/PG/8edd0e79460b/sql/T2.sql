-- 准备
DROP TABLE IF EXISTS t2_p CASCADE;
CREATE TABLE t2_p (k int, g int, v int) PARTITION BY RANGE (k);
CREATE TABLE t2_p1 PARTITION OF t2_p FOR VALUES FROM (0) TO (10);
CREATE INDEX t2_p1_k_g ON t2_p1 (k, g);
INSERT INTO t2_p VALUES (1,1,10),(2,1,20),(3,2,5),(4,2,7),(5,1,1);
ANALYZE t2_p;

-- 目标 SELECT：单子 MergeAppend + GROUP BY
SELECT g, sum(v) AS sv FROM t2_p WHERE k < 10 GROUP BY g ORDER BY g;

-- 对照：直接查 child
SELECT g, sum(v) AS sv FROM t2_p1 WHERE k < 10 GROUP BY g ORDER BY g;

-- 清理
DROP TABLE t2_p CASCADE;
