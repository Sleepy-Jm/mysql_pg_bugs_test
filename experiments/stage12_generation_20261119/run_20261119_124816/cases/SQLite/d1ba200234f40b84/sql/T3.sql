-- 准备：正负值混合，使过滤改变计数
CREATE TABLE t1(x INTEGER);
CREATE TABLE t2(y INTEGER);
INSERT INTO t1 VALUES (1),(-1),(2),(-2);
INSERT INTO t2 VALUES (3),(-3);

-- 目标 SELECT：外层 WHERE 过滤
SELECT count(*)
FROM (
    SELECT x FROM t1
    UNION ALL
    SELECT y FROM t2
)
WHERE x > 0;

-- 对照：按原始语义手工等价形式
SELECT count(*) FROM (
    SELECT x FROM t1 WHERE x > 0
    UNION ALL
    SELECT y FROM t2 WHERE y > 0
);

-- 清理
DROP TABLE t1;
DROP TABLE t2;
