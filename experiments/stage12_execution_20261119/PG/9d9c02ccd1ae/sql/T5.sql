-- 准备
CREATE TEMP TABLE t5 (a int);
INSERT INTO t5 VALUES (1),(2),(3),(4),(5);

-- 目标 SELECT：两层窗口，外层过滤引用顶层 row_number()
SELECT a, rn1, rn2
FROM (
  SELECT a,
         row_number() OVER (ORDER BY a) AS rn1,
         row_number() OVER (ORDER BY a DESC) AS rn2
  FROM t5
) s
WHERE rn2 <= 3
ORDER BY a;

-- 对照
WITH w AS MATERIALIZED (
  SELECT a,
         row_number() OVER (ORDER BY a) AS rn1,
         row_number() OVER (ORDER BY a DESC) AS rn2
  FROM t5
)
SELECT a, rn1, rn2 FROM w WHERE rn2 <= 3 ORDER BY a;

-- 清理
DROP TABLE t5;
