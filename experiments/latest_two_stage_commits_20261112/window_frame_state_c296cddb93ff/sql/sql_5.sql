-- T5: H2 exploratory only. MIN/MAX over an optimized ROWS frame where the first row
-- is brought back into the frame; checks whether first_rowno_in_rows_frame and
-- rowno_being_visited stay consistent. Does not confirm H2 without the missing guard.
CREATE TEMPORARY TABLE t5 (p INT NOT NULL, o INT NOT NULL, x INT NOT NULL);
INSERT INTO t5 VALUES
 (1,1,9),(1,2,3),(1,3,7),(1,4,1),(1,5,8),(1,6,2);
SELECT o,
       MIN(x) OVER (PARTITION BY p ORDER BY o ROWS BETWEEN 2 PRECEDING AND 1 FOLLOWING) AS mn,
       MAX(x) OVER (PARTITION BY p ORDER BY o ROWS BETWEEN 2 PRECEDING AND 1 FOLLOWING) AS mx
FROM t5 ORDER BY o;
-- Contrast: same frame, but with a strictly increasing sequence so a stale cache
-- would be visible as a wrong extremum.
SELECT o,
       MIN(x) OVER (PARTITION BY p ORDER BY o ROWS BETWEEN 2 PRECEDING AND 1 FOLLOWING) AS mn,
       MAX(x) OVER (PARTITION BY p ORDER BY o ROWS BETWEEN 2 PRECEDING AND 1 FOLLOWING) AS mx
FROM (SELECT p,o,o*10 AS x FROM t5) s ORDER BY o;
DROP TEMPORARY TABLE t5;

