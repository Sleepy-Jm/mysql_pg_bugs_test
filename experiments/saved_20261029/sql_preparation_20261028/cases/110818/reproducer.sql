-- MySQL report #110818; source: cmain, c532047
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 INT);
INSERT INTO t0(c0) VALUES(NULL);
SELECT CAST(t0.c0 > ANY(SELECT 1 FROM t0) AS SIGNED) FROM t0;
