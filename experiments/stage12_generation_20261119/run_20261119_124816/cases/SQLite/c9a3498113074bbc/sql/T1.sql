-- 准备
CREATE TABLE t1(a INTEGER, b TEXT);
INSERT INTO t1 VALUES (1,'x'),(2,'y'),(3,'z'),(4,'w'),(5,'v');
CREATE TABLE t2(k INTEGER);
INSERT INTO t2 VALUES (2),(4);

-- 目标 SELECT：外层 WHERE 的 IN 可被下推进 FROM 子查询
SELECT a, b FROM (SELECT a, b FROM t1) AS s
WHERE a IN (SELECT k FROM t2)
ORDER BY a;

-- 对照：等价改写，逻辑上只有一个 IN 条件
SELECT a, b FROM t1
WHERE a IN (SELECT k FROM t2)
ORDER BY a;

-- 清理
DROP TABLE t1;
DROP TABLE t2;
