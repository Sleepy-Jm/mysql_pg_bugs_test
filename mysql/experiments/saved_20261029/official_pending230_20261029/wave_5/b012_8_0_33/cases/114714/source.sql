-- MySQL report #114714; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t1 (a INT, b INT);
INSERT INTO t1 VALUES (4, 40), (1, 10), (2, 20), (2, 20), (3, 30);

CREATE TABLE t2 SELECT DISTINCT a FROM t1;

ANALYZE TABLE t1, t2;


 EXPLAIN FORMAT=TREE SELECT (SELECT t2.a FROM t2 WHERE t2.a = t1.a) aa, b, COUNT(b) FROM t1 GROUP BY aa, b ORDER BY -aa, -b;
