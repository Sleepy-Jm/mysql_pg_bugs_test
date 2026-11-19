-- 准备
DROP TABLE IF EXISTS t1_outer, t1_inner;
CREATE TABLE t1_outer (id INT PRIMARY KEY, v INT);
CREATE TABLE t1_inner (k INT, PRIMARY KEY(k));
INSERT INTO t1_outer VALUES (1, 10), (2, 20);
INSERT INTO t1_inner VALUES (30), (NULL);

-- 目标：外层两行，IN 子查询对每行重执行；内层含 NULL 且无匹配
-- 期望：两行都不满足 IN（NULL 语义），结果为空集
SELECT id, v FROM t1_outer
WHERE v IN (SELECT k FROM t1_inner)
ORDER BY id;

-- 对照：显式展示每行 IN 的布尔/UNKNOWN 语义
SELECT id, v,
       (v IN (SELECT k FROM t1_inner)) AS in_result
FROM t1_outer
ORDER BY id;

-- 清理
DROP TABLE t1_outer, t1_inner;
