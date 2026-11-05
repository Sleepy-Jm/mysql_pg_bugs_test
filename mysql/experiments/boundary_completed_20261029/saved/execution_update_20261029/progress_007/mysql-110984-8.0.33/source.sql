-- MySQL report #110984; source anchors: cmain, c544757
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET NAMES utf8mb4 COLLATE utf8mb4_0900_ai_ci;
CREATE TABLE t1(flowid VARCHAR(32)) CHARSET=gbk COLLATE=gbk_bin;
INSERT INTO t1 VALUES('xxx');
SELECT CONCAT(abc,flowid) FROM (SELECT 'yyy-' AS abc,flowid FROM t1) AS alias;
SELECT CONCAT(abc,flowid) FROM (SELECT 'yyy-' AS abc,flowid FROM t1 LIMIT 1) AS alias;
