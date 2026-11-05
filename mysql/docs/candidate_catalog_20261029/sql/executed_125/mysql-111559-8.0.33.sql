-- MySQL report #111559; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE VIEW v0 (c0) AS (WITH x(x) AS (SELECT 1), y(y) AS (SELECT 1) SELECT 1 FROM x);
SELECT 1 FROM v0;
SHOW CREATE VIEW v0;
