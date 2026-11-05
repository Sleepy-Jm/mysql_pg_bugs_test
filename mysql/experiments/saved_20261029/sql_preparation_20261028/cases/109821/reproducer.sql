-- Report #109821; source anchors: cmain, c529336
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t0 (c0 INT);
CREATE TABLE t1 (c0 INT);
VALUES ROW(1),ROW((SELECT 1 FROM t1 NATURAL JOIN (SELECT 1 FROM t0) t0(c0)));
