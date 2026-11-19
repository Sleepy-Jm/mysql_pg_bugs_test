-- 准备：两张小表，行数不同，含 NULL 与重复值
CREATE TABLE t1(x INTEGER);
CREATE TABLE t2(y INTEGER);
INSERT INTO t1 VALUES (1),(2),(2),(NULL);
INSERT INTO t2 VALUES (10),(20),(NULL);

-- 目标 SELECT：安全形态，预期等于 (count t1)+(count t2)
SELECT count(*)
FROM (
    SELECT x FROM t1
    UNION ALL
    SELECT y FROM t2
);

-- 对照：等价形式，独立给出预期
SELECT (SELECT count(*) FROM t1) + (SELECT count(*) FROM t2);

-- 清理
DROP TABLE t1;
DROP TABLE t2;
