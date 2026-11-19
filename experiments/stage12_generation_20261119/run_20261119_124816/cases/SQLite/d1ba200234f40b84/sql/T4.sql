-- 准备：t1 多行，t2 少量行
CREATE TABLE t1(x INTEGER);
CREATE TABLE t2(y INTEGER);
INSERT INTO t1 VALUES (1),(2),(3),(4),(5);
INSERT INTO t2 VALUES (10),(20);

-- 目标 SELECT：第一项带 LIMIT 0（边界：零行贡献）
SELECT count(*)
FROM (
    SELECT x FROM t1 LIMIT 0
    UNION ALL
    SELECT y FROM t2
);

-- 对照：按原始语义手工等价形式
SELECT (SELECT count(*) FROM (SELECT x FROM t1 LIMIT 0))
     + (SELECT count(*) FROM t2);

-- 清理
DROP TABLE t1;
DROP TABLE t2;
