-- Report #110256; source anchors: cmain, c530389
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t0(c0 DECIMAL) ;
INSERT DELAYED IGNORE INTO t0(c0) VALUES('');
CREATE INDEX i0 ON t0(c0 DESC);
SELECT ALL t0.c0 FROM t0 WHERE (t0.c0) = (LEAST('1507214118', "0W*-+	U0")); 
DROP INDEX i0 ON t0;
SELECT ALL t0.c0 FROM t0 WHERE (t0.c0) = (LEAST('1507214118', "0W*-+	U0"));
