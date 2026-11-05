-- MySQL report #111293; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t0 (c0 INT) PARTITION BY HASH((SELECT DISTINCT 1 x ORDER BY x)) AS (SELECT 1 c0);
