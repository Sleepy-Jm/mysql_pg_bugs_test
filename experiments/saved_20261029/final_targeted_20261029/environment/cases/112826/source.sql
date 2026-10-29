-- MySQL report #112826; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t0(c0 INT,INDEX i0(c0)) AS SELECT 1 c0;
SELECT 1 FROM t0 WHERE t0.c0=-(-.5);
SELECT t0.c0=-(-.5) FROM t0;
SELECT 1 FROM t0 IGNORE INDEX(i0) WHERE t0.c0=-(-.5);
