-- MySQL report #117847; source: cmain, c551633
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t1(c1 DOUBLE);
INSERT INTO t1 VALUES(0);
SELECT NULLIF(-33.26,ref_1.c1) IS NULL AS w1 FROM t1 AS ref_1;
SELECT NULLIF(-33.26,ref_1.c1) IS NULL AS w1 FROM t1 AS ref_1 WHERE NULLIF(-33.26,ref_1.c1) IS NULL;
