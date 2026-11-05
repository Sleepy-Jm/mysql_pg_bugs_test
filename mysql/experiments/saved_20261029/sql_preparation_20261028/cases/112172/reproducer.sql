-- MySQL report #112172; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t0 (c0 INT PRIMARY KEY);
CREATE TABLE t1 (c0 INT PRIMARY KEY);
SELECT 1 FROM (SELECT CAST(t0.c0 AS UNSIGNED) FROM t0 WHERE (SELECT 1 FROM t1) = t0.c0) x(x) LEFT JOIN t1 ON t1.c0 = x.x WHERE 1 = x.x;
