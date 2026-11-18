-- T3 (C2): IS NULL over a non-nullable window-function child in a buffered window.
-- Sensitive: child is non-nullable (SUM OVER with frame over NOT NULL column) so parent skips propagation;
-- target propagates PROP_WINDOW_FUNCTION to the IS NULL wrapper. Oracle: window result over original rows, then IS NULL.
DROP TABLE IF EXISTS t3_w;
CREATE TABLE t3_w (id INT PRIMARY KEY, g INT NOT NULL, x INT NOT NULL);
INSERT INTO t3_w VALUES (1,1,10),(2,1,20),(3,2,30),(4,2,40),(5,1,50);
-- Target: IS NULL wrapper around a window function.
SELECT id, g, x,
       IS NULL(SUM(x) OVER (PARTITION BY g ORDER BY id ROWS BETWEEN 1 PRECEDING AND CURRENT ROW)) AS isn
  FROM t3_w ORDER BY id;
-- Contrast: bare window function (no IS NULL wrapper) — same window, no wrapper property question.
SELECT id, g, x,
       SUM(x) OVER (PARTITION BY g ORDER BY id ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS s
  FROM t3_w ORDER BY id;
DROP TABLE t3_w;

