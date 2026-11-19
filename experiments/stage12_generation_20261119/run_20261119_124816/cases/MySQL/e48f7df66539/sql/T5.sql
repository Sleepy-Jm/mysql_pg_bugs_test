-- 准备
DROP TABLE IF EXISTS t5_grp;
CREATE TABLE t5_grp (
  id INT PRIMARY KEY,
  b  BIT(4),
  e  ENUM('x','y','z'),
  n  INT
) ENGINE=InnoDB;
INSERT INTO t5_grp VALUES
  (1, b'0001', 'x', 10),
  (2, b'0001', 'x', 20),
  (3, b'0010', 'y', 30),
  (4, b'0010', 'y', 40),
  (5, b'0001', 'z', 50),
  (6, NULL,    'x', 60);

-- 目标 SELECT：GROUP BY 临时表聚合，分组键为 BIT 与 ENUM
SELECT b, e, COUNT(*) AS c, SUM(n) AS s
FROM t5_grp
GROUP BY b, e
ORDER BY b, e;

-- 对照：显式 CAST 分组键后聚合（不依赖临时表分组键复制）
SELECT CAST(b AS UNSIGNED) AS b, CAST(e AS CHAR) AS e, COUNT(*) AS c, SUM(n) AS s
FROM t5_grp
GROUP BY CAST(b AS UNSIGNED), CAST(e AS CHAR)
ORDER BY b, e;

-- 清理
DROP TABLE IF EXISTS t5_grp;
