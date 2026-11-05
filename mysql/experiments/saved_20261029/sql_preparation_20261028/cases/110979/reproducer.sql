-- MySQL report #110979; source anchors: cmain, c532415
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLEt0 (c0 YEAR, c1 INT AS (1) VIRTUAL);
INSERT IGNORE INTO t0 (c0) (SELECT 2100);
SET SESSION BINLOG_ROW_IMAGE = 'MINIMAL';
UPDATE t0 SET c0 = 2000 WHERE utc_date() <> c0;
SELECT * FROM t0;
SELECT 1 AS server_alive;
