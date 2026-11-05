-- Source cmain + developer c541315. Separate source-documented RELEASE wrong-result variant.
-- Fresh table per optimizer arm; not the original debug-assertion reproduction.
CREATE TABLE t1 (c0 INT);
INSERT INTO t1(c0) VALUES (1),(2);
SET SESSION optimizer_switch='subquery_to_derived=off';
INSERT IGNORE INTO t1(c0) (SELECT (SELECT t1.c0 FROM t1) FROM t1);
SHOW WARNINGS;
SELECT c0 FROM t1 ORDER BY c0 IS NOT NULL,c0;
DROP TABLE t1;
CREATE TABLE t1 (c0 INT);
INSERT INTO t1(c0) VALUES (1),(2);
SET SESSION optimizer_switch='subquery_to_derived=on';
INSERT IGNORE INTO t1(c0) (SELECT (SELECT t1.c0 FROM t1) FROM t1);
SHOW WARNINGS;
SELECT c0 FROM t1 ORDER BY c0 IS NOT NULL,c0;
