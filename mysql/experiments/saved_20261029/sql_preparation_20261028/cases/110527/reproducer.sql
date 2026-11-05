-- MySQL report #110527; source anchors: cmain, c540950
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLEt0 (c0 TEXT);
INSERT INTO t0(c0) VALUES (1);
ANALYZE LOCAL TABLE t0 UPDATE HISTOGRAM ON c0 WITH 2 BUCKETS;
SELECT 1 FROM (SELECT 1) x(x) JOIN t0 ON reverse(1) = t0.c0;
SELECT 1 AS server_alive;
