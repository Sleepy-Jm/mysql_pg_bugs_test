-- 准备
CREATE TEMP TABLE t2 (g int, a int);
INSERT INTO t2 VALUES
  (1,1),(1,2),(1,3),(1,4),
  (2,1),(2,2),(2,3),(2,4);

-- 目标 SELECT：分区内 row_number()，外层 rn <= 2
SELECT g, a, rn
FROM (
  SELECT g, a, row_number() OVER (PARTITION BY g ORDER BY a) AS rn
  FROM t2
) s
WHERE rn <= 2
ORDER BY g, a;

-- 对照
WITH w AS MATERIALIZED (
  SELECT g, a, row_number() OVER (PARTITION BY g ORDER BY a) AS rn FROM t2
)
SELECT g, a, rn FROM w WHERE rn <= 2 ORDER BY g, a;

-- 清理
DROP TABLE t2;
