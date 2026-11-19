-- 准备
DROP TABLE IF EXISTS t4_l, t4_r;
CREATE TABLE t4_l (id int, k int);
CREATE TABLE t4_r (id int, k int);
INSERT INTO t4_l VALUES (1,10),(2,20),(3,30),(4,40);
INSERT INTO t4_r VALUES (100,10),(101,20),(102,50),(103,60);

-- 目标：反连接，强制 merge join
SET LOCAL enable_hashjoin = off;
SET LOCAL enable_nestloop = off;
SELECT l.id, l.k
FROM t4_l l
WHERE NOT EXISTS (SELECT 1 FROM t4_r r WHERE r.k = l.k AND true)
ORDER BY l.id;

-- 对照：标准 SQL 等价改写
SELECT l.id, l.k
FROM t4_l l
LEFT JOIN t4_r r ON r.k = l.k
WHERE r.id IS NULL
ORDER BY l.id;

-- 清理
DROP TABLE t4_l;
DROP TABLE t4_r;
