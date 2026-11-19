-- 准备
DROP TABLE IF EXISTS t1_l, t1_r;
CREATE TABLE t1_l (id int, k int);
CREATE TABLE t1_r (id int, k int);
INSERT INTO t1_l VALUES (1,10),(2,20),(3,30),(4,NULL),(5,10);
INSERT INTO t1_r VALUES (100,10),(101,10),(102,20),(103,NULL),(104,40);

-- 目标：反连接，返回 t1_l 中 k 在 t1_r 中无匹配的行
SELECT l.id, l.k
FROM t1_l l
WHERE NOT EXISTS (SELECT 1 FROM t1_r r WHERE r.k = l.k)
ORDER BY l.id;

-- 对照：标准 SQL 等价改写
SELECT l.id, l.k
FROM t1_l l
LEFT JOIN t1_r r ON r.k = l.k
WHERE r.id IS NULL
ORDER BY l.id;

-- 清理
DROP TABLE t1_l;
DROP TABLE t1_r;
