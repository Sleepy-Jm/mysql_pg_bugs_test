-- MySQL report #110961; source anchors: cmain, c541304, c541315, c542409
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLEt1 (c0 INT);
INSERT INTO t1(c0) VALUES (1), (2);
SET @@SESSION.OPTIMIZER_SWITCH = 'subquery_to_derived=on';
INSERT IGNORE INTO t1 (c0) (SELECT (SELECT t1.c0 FROM t1) FROM t1);
SHOW WARNINGS;
SELECT * FROM t1;
SELECT 1 AS server_alive;
