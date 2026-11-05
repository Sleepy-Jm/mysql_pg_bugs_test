-- MySQL report #114378; source: cmain, c542585
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 FLOAT);
INSERT INTO t0(c0) VALUES(-1);

SELECT f1 FROM (SELECT ((t0.c0) ^ (CONVERT_TZ('2001-10-22 16:13:59.9', '-01:00','+00:00'))) AS f1 FROM t0) as t WHERE (f1) > (1);

SELECT f1 FROM (SELECT ((t0.c0) ^ (CONVERT_TZ('2001-10-22 16:13:59.9', '-01:00','+00:00'))) AS f1 FROM t0) as t;
