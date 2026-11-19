-- 准备
DROP TABLE IF EXISTS t3_outer, t3_inner;
CREATE TABLE t3_outer (id INT PRIMARY KEY, v INT);
CREATE TABLE t3_inner (k INT, PRIMARY KEY(k));
INSERT INTO t3_outer VALUES (1, 10), (2, 20), (3, 30), (4, 40);
INSERT INTO t3_inner VALUES (10), (30), (NULL);

-- 目标：外层多行，非相关 IN 子查询，倾向 materialization
-- 期望：id=1 与 id=3 满足；id=2、id=4 因 NULL 语义为 UNKNOWN 被排除
SELECT o.id, o.v
FROM t3_outer o
WHERE o.v IN (SELECT k FROM t3_inner)
ORDER BY o.id;

-- 对照：聚合值核对
SELECT COUNT(*) AS matched
FROM t3_outer o
WHERE o.v IN (SELECT k FROM t3_inner);

-- 清理
DROP TABLE t3_outer, t3_inner;
