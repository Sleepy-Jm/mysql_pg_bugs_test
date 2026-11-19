-- 准备
DROP TABLE IF EXISTS t5_drv, t5_l, t5_r;
CREATE TABLE t5_drv (d int);
CREATE TABLE t5_l (id int, k int);
CREATE TABLE t5_r (id int, k int);
INSERT INTO t5_drv VALUES (1),(2);
INSERT INTO t5_l VALUES (1,10),(2,20),(3,30);
INSERT INTO t5_r VALUES (100,10),(101,20);

-- 目标：LATERAL 内反连接，驱动表两行触发重扫描
SELECT d.d, x.id, x.k
FROM t5_drv d
CROSS JOIN LATERAL (
  SELECT l.id, l.k
  FROM t5_l l
  WHERE NOT EXISTS (SELECT 1 FROM t5_r r WHERE r.k = l.k AND d.d > 0)
) x
ORDER BY d.d, x.id;

-- 对照：标准 SQL 等价改写
SELECT d.d, l.id, l.k
FROM t5_drv d
CROSS JOIN t5_l l
WHERE NOT EXISTS (SELECT 1 FROM t5_r r WHERE r.k = l.k AND d.d > 0)
ORDER BY d.d, l.id;

-- 清理
DROP TABLE t5_drv;
DROP TABLE t5_l;
DROP TABLE t5_r;
