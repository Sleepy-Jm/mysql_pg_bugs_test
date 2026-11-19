-- 准备
DROP TABLE IF EXISTS outer_t;
DROP TABLE IF EXISTS inner_t;
CREATE TABLE outer_t (id INT PRIMARY KEY, a INT NOT NULL, b INT NOT NULL);
CREATE TABLE inner_t (id INT PRIMARY KEY, p INT NOT NULL, q INT NOT NULL);
INSERT INTO outer_t VALUES (1,1,10),(2,2,20),(3,3,30),(4,4,40);
INSERT INTO inner_t VALUES (1,1,10),(2,2,20),(3,9,90);

-- 目标 SELECT：多列 IN 子查询，可能转换为相关 EXISTS
SELECT a, b, a+b AS s
FROM outer_t
WHERE (a, b) IN (SELECT p, q FROM inner_t)
ORDER BY a;

-- 对照：显式 EXISTS 改写，语义等价
SELECT a, b, a+b AS s
FROM outer_t o
WHERE EXISTS (SELECT 1 FROM inner_t i WHERE i.p = o.a AND i.q = o.b)
ORDER BY a;

-- 清理
DROP TABLE IF EXISTS outer_t;
DROP TABLE IF EXISTS inner_t;
