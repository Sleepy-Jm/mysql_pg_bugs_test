-- 准备
DROP TABLE IF EXISTS t4_outer, t4_inner;
CREATE TABLE t4_outer (id INT PRIMARY KEY, v INT);
CREATE TABLE t4_inner (k INT, PRIMARY KEY(k));
INSERT INTO t4_outer VALUES (1, 10), (2, 20), (3, 30);
INSERT INTO t4_inner VALUES (10), (30);

-- 目标：prepared statement 多次执行，IN 子查询走 index_subquery
PREPARE stmt FROM
  'SELECT o.id, o.v FROM t4_outer o WHERE o.v IN (SELECT k FROM t4_inner) ORDER BY o.id';

EXECUTE stmt;
EXECUTE stmt;
EXECUTE stmt;

DEALLOCATE PREPARE stmt;

-- 对照：一次性执行
SELECT o.id, o.v FROM t4_outer o
WHERE o.v IN (SELECT k FROM t4_inner)
ORDER BY o.id;

-- 清理
DROP TABLE t4_outer, t4_inner;
