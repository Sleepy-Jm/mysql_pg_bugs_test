-- T1: C1 exploratory. Frame [i-2, i+2] with partition end reached so upper > current_row.
-- Sensitive operand is x in AVG(x); rows after current row are in the frame.
CREATE TEMPORARY TABLE t1 (p INT NOT NULL, o INT NOT NULL, x INT NOT NULL);
INSERT INTO t1 VALUES
 (1,1,10),(1,2,20),(1,3,30),(1,4,40),(1,5,50),(1,6,60);
-- Target query: current row o=3, frame rows o=1..5, true mean = 30.
SELECT o, AVG(x) OVER (PARTITION BY p ORDER BY o ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING) AS a
FROM t1 ORDER BY o;
-- Contrast: same frame but current row is the last row (upper == current_row), no trailing rows.
SELECT o, AVG(x) OVER (PARTITION BY p ORDER BY o ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) AS a
FROM t1 ORDER BY o;
DROP TEMPORARY TABLE t1;

