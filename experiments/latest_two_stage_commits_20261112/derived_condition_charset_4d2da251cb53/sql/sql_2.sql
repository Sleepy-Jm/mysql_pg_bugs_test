DROP TABLE IF EXISTS t2a, t2b;
CREATE TABLE t2a (c VARCHAR(32) CHARACTER SET latin1 COLLATE latin1_bin);
CREATE TABLE t2b (c VARCHAR(32) CHARACTER SET latin1 COLLATE latin1_bin);
INSERT INTO t2a VALUES ('A'),('B');
INSERT INTO t2b VALUES ('A'),('B');
SET optimizer_switch='derived_condition_pushdown=on';
SELECT dt.c FROM (SELECT c FROM t2a UNION ALL SELECT c FROM t2b) AS dt
 WHERE dt.c LIKE 'A';
SELECT dt.c FROM (SELECT c FROM t2a UNION ALL SELECT c FROM t2b) AS dt
 WHERE dt.c LIKE _latin1'A';
DROP TABLE t2a, t2b;

