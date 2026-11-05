-- MySQL report #109824; source anchors: cmain
-- Static preparation only. NOT EXECUTED. See case.json for conditions and oracle.
CREATE VIEW t0(c2) AS (SELECT b'1');
SELECT 1 FROM t0 WHERE NOT t0.c2;
SELECT CAST(sum(c0) AS SIGNED) FROM (SELECT CAST(NOT t0.c2 AS SIGNED) FROM t0) t0(c0);
