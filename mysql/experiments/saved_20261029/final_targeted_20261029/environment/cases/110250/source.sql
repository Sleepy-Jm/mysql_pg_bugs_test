-- MySQL report #110250; source anchors: cmain
-- Static preparation only. NOT EXECUTED. See case.json for conditions and oracle.
CREATE TABLE t1(c0 BIGINT);
CREATE TABLE t0(c0 BOOLEAN);
INSERT INTO t0 VALUES (1),(NULL);
SELECT 1 FROM t1 RIGHT JOIN t0 USING(c0) WHERE -1 < CHAR(t1.c0);
SELECT CAST(sum(c0) AS SIGNED) FROM (SELECT CAST(-1 < CHAR(t1.c0) AS SIGNED) FROM t1 RIGHT JOIN t0 USING(c0)) t0(c0);
