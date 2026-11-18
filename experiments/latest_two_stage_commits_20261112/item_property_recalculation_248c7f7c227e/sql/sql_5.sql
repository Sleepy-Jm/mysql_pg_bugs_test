-- T5 (C2): IS NULL over a non-nullable window child using a different window function (COUNT OVER)
-- to vary the child item type while keeping the non-nullable property. Same sensitive property.
DROP TABLE IF EXISTS t5_w;
CREATE TABLE t5_w (id INT PRIMARY KEY, g INT NOT NULL, x INT NOT NULL);
INSERT INTO t5_w VALUES (1,1,10),(2,1,20),(3,2,30),(4,2,40),(5,1,50);
-- Target: IS NULL over COUNT window (COUNT is non-nullable).
SELECT id, g, x,
       IS NULL(COUNT(x) OVER (PARTITION BY g ORDER BY id ROWS BETWEEN 1 PRECEDING AND CURRENT ROW)) AS isn
  FROM t5_w ORDER BY id;
-- Contrast: same window without IS NULL wrapper.
SELECT id, g, x,
       COUNT(x) OVER (PARTITION BY g ORDER BY id ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS c
  FROM t5_w ORDER BY id;
DROP TABLE t5_w;

