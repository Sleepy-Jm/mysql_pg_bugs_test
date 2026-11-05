-- Report #111383; source anchors: cmain, c533477
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t0 (c0 YEAR);
SELECT avg(nullif(t0.c0, t0.c0)) FROM t0;
