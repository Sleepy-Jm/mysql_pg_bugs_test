-- MySQL report #109820; source anchors: cmain, c529314
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t1(id INT);
INSERT INTO t1 VALUES(1),(2);
EXPLAIN SELECT /*+ NO_MERGE() */ * FROM (SELECT * FROM t1) dt;
SHOW WARNINGS;
CREATE VIEW v_1 AS SELECT /*+ NO_MERGE() */ * FROM (SELECT * FROM t1) dt;
SHOW CREATE VIEW v_1;
EXPLAIN SELECT * FROM v_1;
SHOW WARNINGS;
