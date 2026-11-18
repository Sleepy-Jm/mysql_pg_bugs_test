-- T3: C1 exploratory. Nonzero frame sum with a NULL inside the frame to exercise
-- the m_frame_null_count subtraction in the divisor.
-- Current o=3, frame o=1..5: non-NULL x = 4,6,8,10 -> mean 7.
CREATE TEMPORARY TABLE t3 (p INT NOT NULL, o INT NOT NULL, x INT NULL);
INSERT INTO t3 VALUES
 (1,1,4),(1,2,NULL),(1,3,6),(1,4,8),(1,5,10),(1,6,12);
SELECT o, AVG(x) OVER (PARTITION BY p ORDER BY o ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING) AS a
FROM t3 ORDER BY o;
-- Contrast: same frame, no NULLs.
SELECT o, AVG(x) OVER (PARTITION BY p ORDER BY o ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING) AS a
FROM (SELECT p,o,COALESCE(x,0) AS x FROM t3) s ORDER BY o;
DROP TEMPORARY TABLE t3;

