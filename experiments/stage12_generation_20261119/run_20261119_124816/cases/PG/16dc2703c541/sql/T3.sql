-- 准备
DROP TABLE IF EXISTS t3_l, t3_r;
CREATE TABLE t3_l (id int, k int);
CREATE TABLE t3_r (id int, k int);
INSERT INTO t3_l VALUES (1,1),(2,2),(3,3);
-- 右表 200 行，k 从 1 到 200，仅 k=1,2,3 匹配左表
INSERT INTO t3_r SELECT g, g FROM generate_series(1,200) g;

-- 目标：反连接，左表 k 在右表无匹配
SET LOCAL work_mem = '64kB';
SELECT l.id, l.k
FROM t3_l l
WHERE NOT EXISTS (SELECT 1 FROM t3_r r WHERE r.k = l.k)
ORDER BY l.id;

-- 对照：标准 SQL 等价改写
SELECT l.id, l.k
FROM t3_l l
LEFT JOIN t3_r r ON r.k = l.k
WHERE r.id IS NULL
ORDER BY l.id;

-- 清理
DROP TABLE t3_l;
DROP TABLE t3_r;
