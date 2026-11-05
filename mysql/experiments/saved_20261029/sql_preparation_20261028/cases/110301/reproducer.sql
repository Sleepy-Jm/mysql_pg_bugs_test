-- MySQL report #110301; source anchors: cmain, c530541
-- Static preparation only. NOT EXECUTED. See case.json for conditions and oracle.
SELECT @@SESSION.sql_mode;
CREATE TABLE t1(c0 INT);
ALTER TABLE t1 CHANGE COLUMN c0 c0 DATE NOT NULL;
INSERT INTO t1(c0) VALUES ROW(t1.c0);
SHOW WARNINGS;
SELECT t1.c0 FROM t1;
SELECT 1 FROM t1 WHERE t1.c0 IS NULL;
SELECT CAST(sum(c0) AS SIGNED) FROM (SELECT CAST(t1.c0 IS NULL AS SIGNED) FROM t1) t0(c0);
