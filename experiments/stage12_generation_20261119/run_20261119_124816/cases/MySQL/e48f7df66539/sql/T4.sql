-- 准备
DROP TABLE IF EXISTS t4_win;
CREATE TABLE t4_win (
  id INT PRIMARY KEY,
  grp INT,
  v   INT
) ENGINE=InnoDB;
INSERT INTO t4_win VALUES
  (1,1,10),(2,1,20),(3,1,30),(4,2,40),(5,2,50);

-- 目标 SELECT：窗口帧回填 + 字段与表达式混合输出
SELECT
  id,
  grp,
  v,
  NTH_VALUE(v, 2) OVER (PARTITION BY grp ORDER BY id
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS nth2,
  LAG(v, 1) OVER (PARTITION BY grp ORDER BY id) AS lag1,
  v * 2 AS v2
FROM t4_win
ORDER BY grp, id;

-- 对照：等价窗口查询但输出列全为字段（无表达式列）
SELECT
  id,
  grp,
  v,
  NTH_VALUE(v, 2) OVER (PARTITION BY grp ORDER BY id
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS nth2,
  LAG(v, 1) OVER (PARTITION BY grp ORDER BY id) AS lag1
FROM t4_win
ORDER BY grp, id;

-- 清理
DROP TABLE IF EXISTS t4_win;
