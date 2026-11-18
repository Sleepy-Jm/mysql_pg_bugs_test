-- T4: C1 exploratory. Two partitions; only the first partition reaches the cache end
-- with trailing frame rows, the second does not. Isolates the "upper > current_row"
-- condition from partition-boundary effects.
CREATE TEMPORARY TABLE t4 (p INT NOT NULL, o INT NOT NULL, x INT NOT NULL);
INSERT INTO t4 VALUES
 (1,1,100),(1,2,200),(1,3,300),(1,4,400),(1,5,500),
 (2,1,1),(2,2,2),(2,3,3);
SELECT p, o, AVG(x) OVER (PARTITION BY p ORDER BY o ROWS BETWEEN 1 PRECEDING AND 2 FOLLOWING) AS a
FROM t4 ORDER BY p, o;
-- Contrast: frame ending at current row in both partitions.
SELECT p, o, AVG(x) OVER (PARTITION BY p ORDER BY o ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS a
FROM t4 ORDER BY p, o;
DROP TEMPORARY TABLE t4;

