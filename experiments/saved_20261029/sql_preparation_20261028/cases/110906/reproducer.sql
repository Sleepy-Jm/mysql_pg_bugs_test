-- MySQL report #110906; source anchors: cmain, c532215
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t0(c0 INT,INDEX i1(((SELECT DISTINCT 1 FROM (SELECT 1) x(x) ORDER BY x.x)))) AS (SELECT 1 c0);
SELECT 1 AS server_alive;
