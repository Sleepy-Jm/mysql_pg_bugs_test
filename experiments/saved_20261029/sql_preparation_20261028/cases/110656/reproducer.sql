-- MySQL report #110656; source anchors: cmain, c531717, c540098
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLEt0 (c0 INT, c2 INT, PRIMARY KEY (c0));
CREATE TABLE t1 (c0 DATETIME, PRIMARY KEY (c0));
INSERT IGNORE INTO t0(c2) VALUES (1);
INSERT INTO t0(c0,c2) VALUES (1,2),(3,4);
INSERT IGNORE INTO t1(c0) VALUES (NULL);



SELECT t1.c0 FROM t0 JOIN t1 USING (c0) WHERE t1.c0 IS NULL;
