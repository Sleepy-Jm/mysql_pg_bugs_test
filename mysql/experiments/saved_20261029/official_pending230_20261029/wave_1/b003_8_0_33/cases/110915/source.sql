-- MySQL report #110915; source anchors: cmain, c532281
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t0(c0 INT,c1 INT,c2 INT);
CREATE TABLE t7(c0 INT,c1 INT,c2 INT);
SELECT 1 FROM t0 JOIN t7 ON TRUE GROUP BY t7.c0,t0.c0 HAVING t7.c0=1;
