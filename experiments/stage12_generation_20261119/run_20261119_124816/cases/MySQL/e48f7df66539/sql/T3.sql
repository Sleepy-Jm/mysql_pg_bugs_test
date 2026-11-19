-- 准备
DROP TABLE IF EXISTS t3_distinct;
CREATE TABLE t3_distinct (
  id INT PRIMARY KEY,
  s  VARCHAR(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci
) ENGINE=InnoDB;
INSERT INTO t3_distinct VALUES
  (1,'a'),(2,'A'),(3,'a '),(4,' a'),(5,'b'),(6,NULL),(7,'B');

-- 目标 SELECT：DISTINCT 聚合，去重键为字符串字段
SELECT
  COUNT(DISTINCT s) AS cd,
  SUM(DISTINCT LENGTH(s)) AS sdl,
  GROUP_CONCAT(DISTINCT s ORDER BY s) AS gc
FROM t3_distinct;

-- 对照：显式去重后聚合（不依赖聚合 DISTINCT 内部临时表）
SELECT
  COUNT(*) AS cd,
  SUM(LENGTH(s)) AS sdl,
  GROUP_CONCAT(s ORDER BY s) AS gc
FROM (SELECT DISTINCT s FROM t3_distinct) AS d;

-- 清理
DROP TABLE IF EXISTS t3_distinct;
