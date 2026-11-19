-- 准备
CREATE TABLE t3(a INTEGER);
INSERT INTO t3 VALUES (1),(2),(3),(4),(5),(6),(7),(8);

-- 目标 SELECT：RHS 含 random()，若被复用则只求值一次
SELECT count(*) FROM (SELECT a FROM t3) AS s
WHERE a IN (SELECT (abs(random()) % 8) + 1 FROM t3);

-- 对照：显式把 RHS 物化一次，再让 IN 使用同一结果集
WITH rhs AS MATERIALIZED (
  SELECT (abs(random()) % 8) + 1 AS k FROM t3
)
SELECT count(*) FROM t3
WHERE a IN (SELECT k FROM rhs);

-- 清理
DROP TABLE t3;
