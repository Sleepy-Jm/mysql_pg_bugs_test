-- 准备
DROP TABLE IF EXISTS t5_outer, t5_inner;
CREATE TABLE t5_outer (id INT PRIMARY KEY, v INT);
CREATE TABLE t5_inner (k INT, PRIMARY KEY(k));
INSERT INTO t5_outer VALUES (1, 10), (2, 20), (3, 30), (4, 40), (5, 50);
INSERT INTO t5_inner VALUES (10), (30), (50);

-- 目标：单表内层 + 主键索引，倾向 unique_subquery
-- 期望：id=1、3、5 满足
SELECT o.id, o.v
FROM t5_outer o
WHERE o.v IN (SELECT k FROM t5_inner)
ORDER BY o.id;

-- 对照：聚合值
SELECT COUNT(*) AS matched, SUM(o.v) AS sum_v
FROM t5_outer o
WHERE o.v IN (SELECT k FROM t5_inner);

-- 清理
DROP TABLE t5_outer, t5_inner;
