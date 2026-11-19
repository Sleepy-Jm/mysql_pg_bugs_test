-- 准备
DROP TABLE IF EXISTS t2_outer, t2_inner, t2_const;
CREATE TABLE t2_const (c INT PRIMARY KEY);
CREATE TABLE t2_outer (id INT PRIMARY KEY, v INT);
CREATE TABLE t2_inner (k INT, PRIMARY KEY(k));
INSERT INTO t2_const VALUES (1);
INSERT INTO t2_outer VALUES (1, 10), (2, 20), (3, 30);
INSERT INTO t2_inner VALUES (10), (30);

-- 目标：外层含 const table，非相关 IN 子查询
-- 期望：id=1 与 id=3 满足 IN，id=2 不满足
SELECT o.id, o.v
FROM t2_const c, t2_outer o
WHERE o.v IN (SELECT k FROM t2_inner)
ORDER BY o.id;

-- 对照：去掉 const table，验证 IN 语义本身
SELECT o.id, o.v
FROM t2_outer o
WHERE o.v IN (SELECT k FROM t2_inner)
ORDER BY o.id;

-- 清理
DROP TABLE t2_const, t2_outer, t2_inner;
