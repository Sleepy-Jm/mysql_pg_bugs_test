-- MySQL report #113248; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t0 (c0 INT);
CREATE TABLE t1 (c0 INT, c1 INT);
CREATE VIEW v2 (c0) AS (SELECT 2 FROM t1 WHERE 1 IN (SELECT 1 FROM t0 GROUP BY t1.c0 HAVING t1.c1 IS NULL));
PREPARE p0 FROM 'ALTER TABLE t0 MAX_ROWS = 1';
EXECUTE p0;
EXECUTE p0;
DEALLOCATE PREPARE p0;
