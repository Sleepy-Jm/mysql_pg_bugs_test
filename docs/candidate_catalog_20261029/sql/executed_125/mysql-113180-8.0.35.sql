-- MySQL report #113180; source: cmain, c538271, c538297
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 INT, c1 INT, PRIMARY KEY(c0));
INSERT INTO t0(c0, c1) VALUES (1, 0);
CREATE UNIQUE INDEX i1 ON t0(c1 , c0 );

SELECT * FROM t0 WHERE SIN(1150199883)=c1; -- 1 0
SELECT * FROM t0 WHERE NOT SIN(1150199883)=c1; -- 1 0
