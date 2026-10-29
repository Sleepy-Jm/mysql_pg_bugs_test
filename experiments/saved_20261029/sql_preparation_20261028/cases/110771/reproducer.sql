-- MySQL report #110771; source anchors: cmain, c533650, c546398
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t1(a INT,b INT,KEY(b)) ENGINE=InnoDB ROW_FORMAT=REDUNDANT;
INSERT INTO t1 VALUES(0,0),(1,1),(2,2);
ALTER TABLE t1 ADD COLUMN c VARCHAR(25) DEFAULT NULL,ALGORITHM=INSTANT;
UPDATE t1 SET c='' WHERE a=0;
SELECT a,b,c,c IS NULL,LENGTH(c) FROM t1 ORDER BY a;
