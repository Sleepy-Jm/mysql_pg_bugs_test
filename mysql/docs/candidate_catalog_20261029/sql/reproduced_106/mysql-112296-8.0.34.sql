-- MySQL report #112296; source: cmain, c535940, c539425
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 INT);
CREATE TABLE t1(c0 INT);
CREATE TABLE t2(c0 INT);
REPLACE INTO t0(c0) VALUES(1), (2);
INSERT INTO t2(c0) VALUES(3);

SELECT t0.c0 FROM t0 LEFT JOIN t1 ON FALSE RIGHT JOIN t2 ON (t1.c0 IS NOT NULL) IN (t2.c0 = 1000); -- {NULL}
SELECT /*+ NO_BNL(t0)*/ t0.c0 FROM t0 LEFT JOIN t1 ON FALSE RIGHT JOIN t2 ON (t1.c0 IS NOT NULL) IN (t2.c0 = 1000);
