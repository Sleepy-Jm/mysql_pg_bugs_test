-- T4 (C2): IS NULL over a non-nullable window child with a different frame (UNBOUNDED PRECEDING),
-- exercising a different buffering boundary than T3. Same sensitive property, different frame condition.
DROP TABLE IF EXISTS t4_w;
CREATE TABLE t4_w (id INT PRIMARY KEY, g INT NOT NULL, x INT NOT NULL);
INSERT INTO t4_w VALUES (1,1,10),(2,1,20),(3,2,30),(4,2,40),(5,1,50);
-- Target: IS NULL over running SUM with UNBOUNDED PRECEDING frame.
SELECT id, g, x,
       IS NULL(SUM(x) OVER (PARTITION BY g ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)) AS isn
  FROM t4_w ORDER BY id;
-- Contrast: same window without IS NULL wrapper.
SELECT id, g, x,
       SUM(x) OVER (PARTITION BY g ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS s
  FROM t4_w ORDER BY id;
DROP TABLE t4_w;

