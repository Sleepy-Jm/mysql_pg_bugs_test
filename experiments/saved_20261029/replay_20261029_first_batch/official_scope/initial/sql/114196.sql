-- MySQL report #114196; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE IF NOT EXISTS t0(c0 DECIMAL);
REPLACE INTO t0(c0) VALUES(0.1);

SELECT t0.c0 FROM t0 WHERE t0.c0 <= - 0.8;

SELECT (t0.c0 <= - 0.8) IS TRUE AS flag FROM t0;
SELECT * FROM t0;
