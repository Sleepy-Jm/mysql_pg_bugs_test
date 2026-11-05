-- MySQL report #113302; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t0(c0 INT, c1 INT);
INSERT INTO t0(c1, c0) VALUES(0, 1);

SELECT * FROM t0 WHERE t0.c1 IN (GREATEST(0.1, 0.2)); -- empty result
CREATE INDEX i0 ON t0(c1);
SELECT * FROM t0 WHERE t0.c1 IN (GREATEST(0.1, 0.2)); -- {1|0}
