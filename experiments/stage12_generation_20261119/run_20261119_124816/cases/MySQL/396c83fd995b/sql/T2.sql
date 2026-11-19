-- 准备
DROP TABLE IF EXISTS t2;
CREATE TABLE t2 (id INT PRIMARY KEY, a INT NOT NULL);
INSERT INTO t2 VALUES (1,1),(2,2),(3,3),(4,4);

SET @cnt := 0;

-- 目标 SELECT：别名 x 被 GROUP BY 引用，x 内含副作用
SELECT (@cnt := @cnt + 1) + a AS x, COUNT(*) AS c
FROM t2
GROUP BY x + 1
ORDER BY x;

-- 观测副作用次数
SELECT @cnt AS eval_count;

-- 对照：不使用别名
SET @cnt2 := 0;
SELECT (@cnt2 := @cnt2 + 1) + a AS x, COUNT(*) AS c
FROM t2
GROUP BY ((@cnt2 := @cnt2 + 1) + a) + 1
ORDER BY x;
SELECT @cnt2 AS eval_count2;

-- 清理
DROP TABLE IF EXISTS t2;
