-- T2: C1 exploratory. Asymmetric frame [i-1, i+3]; current row has three rows after it.
-- True mean over o=2..6 for current o=3 is (20+30+40+50+60)/5 = 40.
CREATE TEMPORARY TABLE t2 (p INT NOT NULL, o INT NOT NULL, x INT NOT NULL);
INSERT INTO t2 VALUES
 (1,1,7),(1,2,11),(1,3,13),(1,4,17),(1,5,19),(1,6,23);
SELECT o, AVG(x) OVER (PARTITION BY p ORDER BY o ROWS BETWEEN 1 PRECEDING AND 3 FOLLOWING) AS a
FROM t2 ORDER BY o;
-- Contrast: same data, frame ending at current row so upper == current_row.
SELECT o, AVG(x) OVER (PARTITION BY p ORDER BY o ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS a
FROM t2 ORDER BY o;
DROP TEMPORARY TABLE t2;

