-- Report #111418; source anchors: cmain, c533568, c533575, c533609, c533613, c533622
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t0 (c0 INTEGER);
INSERT INTO t0 VALUES (1);
SELECT (SELECT t0.c0 GROUP BY t0.c0 WITH ROLLUP) FROM t0;
