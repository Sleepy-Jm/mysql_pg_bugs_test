-- MySQL report #111693; source: cmain, c534274
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 INT);
INSERT INTO t0(c0) (VALUES ROW(1), ROW(2) ORDER BY 1) UNION (SELECT 3);
SELECT c0 FROM t0 ORDER BY c0;
