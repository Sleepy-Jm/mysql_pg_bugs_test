-- 准备
CREATE TEMP TABLE t1 (a int);
INSERT INTO t1 VALUES (1),(2),(3),(4),(5);

-- 目标 SELECT：row_number() 递增，外层 rn <= 3
SELECT a, rn
FROM (
  SELECT a, row_number() OVER (ORDER BY a) AS rn
  FROM t1
) s
WHERE rn <= 3
ORDER BY a;

-- 对照：物化后过滤，语义真值
WITH w AS MATERIALIZED (
  SELECT a, row_number() OVER (ORDER BY a) AS rn FROM t1
)
SELECT a, rn FROM w WHERE rn <= 3 ORDER BY a;

-- 清理
DROP TABLE t1;
