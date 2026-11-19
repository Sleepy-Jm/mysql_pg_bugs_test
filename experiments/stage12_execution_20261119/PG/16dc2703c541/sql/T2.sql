-- 准备
DROP TABLE IF EXISTS t2_l, t2_r;
CREATE TABLE t2_l (id int, k int);
CREATE TABLE t2_r (id int, k int);
INSERT INTO t2_l VALUES (1,10),(2,20),(3,30);
INSERT INTO t2_r VALUES (100,10),(101,NULL);

-- 目标：NOT IN，右表含 NULL 时整体结果为空
SELECT l.id, l.k
FROM t2_l l
WHERE l.k NOT IN (SELECT r.k FROM t2_r r)
ORDER BY l.id;

-- 对照：右表无 NULL 时的 NOT IN
SELECT l.id, l.k
FROM t2_l l
WHERE l.k NOT IN (SELECT r.k FROM t2_r r WHERE r.k IS NOT NULL)
ORDER BY l.id;

-- 清理
DROP TABLE t2_l;
DROP TABLE t2_r;
