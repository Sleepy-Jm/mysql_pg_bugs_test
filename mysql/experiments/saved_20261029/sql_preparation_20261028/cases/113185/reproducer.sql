-- MySQL report #113185; source: cmain, c538280, c538291
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t1(c0 INT);
INSERT INTO t1 VALUES(1);
SELECT NULLIF(-1,c0*(1/true)),NULLIF(-1,c0*(1/true)) IS NULL FROM t1;
SELECT * FROM t1 WHERE NULLIF(-1,c0*(1/true));
SELECT * FROM t1 WHERE NULLIF(-1,c0*(1/true)) IS NULL;
