-- MySQL report #111357; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t0 (c0 INT);
EXPLAIN FORMAT = JSON SELECT count(count(*)) OVER () FROM t0 ORDER BY (SELECT 1 WHERE NOT 1);
