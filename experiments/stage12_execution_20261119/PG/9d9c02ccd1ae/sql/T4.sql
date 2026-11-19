-- 准备
CREATE TEMP TABLE t4 (a int);
INSERT INTO t4 VALUES (1),(2),(3),(4),(5);

-- 目标 SELECT：无 ORDER BY 的 count(*) 为常量 5，外层 cnt = 5
SELECT a, cnt
FROM (
  SELECT a, count(*) OVER () AS cnt
  FROM t4
) s
WHERE cnt = 5
ORDER BY a;

-- 对照
WITH w AS MATERIALIZED (
  SELECT a, count(*) OVER () AS cnt FROM t4
)
SELECT a, cnt FROM w WHERE cnt = 5 ORDER BY a;

-- 清理
DROP TABLE t4;
