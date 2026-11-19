-- 准备
DROP TABLE IF EXISTS t1_derived;
CREATE TABLE t1_derived (
  id INT PRIMARY KEY,
  s  VARCHAR(10)
) ENGINE=InnoDB;
INSERT INTO t1_derived VALUES
  (1,'10'),(2,'2'),(3,' 3'),(4,NULL),(5,'04');

-- 目标 SELECT：派生表物化，外层对派生列做数值比较与排序
SELECT d.id, d.s
FROM (SELECT id, s FROM t1_derived) AS d
WHERE d.s + 0 >= 3
ORDER BY d.s + 0, d.id;

-- 对照：等价但强制不同路径（直接基表，无派生物化）
SELECT id, s
FROM t1_derived
WHERE s + 0 >= 3
ORDER BY s + 0, id;

-- 清理
DROP TABLE IF EXISTS t1_derived;
