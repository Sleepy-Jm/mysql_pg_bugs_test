-- 准备：t1 有重复值，分组数少于行数
CREATE TABLE t1(x INTEGER);
CREATE TABLE t2(y INTEGER);
INSERT INTO t1 VALUES (1),(1),(2),(3),(3),(3);
INSERT INTO t2 VALUES (9);

-- 目标 SELECT：第一项带 GROUP BY
SELECT count(*)
FROM (
    SELECT x FROM t1 GROUP BY x
    UNION ALL
    SELECT y FROM t2
);

-- 对照：按原始语义手工等价形式
SELECT (SELECT count(*) FROM (SELECT x FROM t1 GROUP BY x))
     + (SELECT count(*) FROM t2);

-- 清理
DROP TABLE t1;
DROP TABLE t2;
