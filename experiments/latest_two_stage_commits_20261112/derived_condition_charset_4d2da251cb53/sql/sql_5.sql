DROP TABLE IF EXISTS t5a, t5b;
CREATE TABLE t5a (c VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin);
CREATE TABLE t5b (c VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin);
INSERT INTO t5a VALUES ('abc'),('abd');
INSERT INTO t5b VALUES ('abc'),('abd');
SET optimizer_switch='derived_condition_pushdown=on';
SELECT dt.c FROM (SELECT c FROM t5a UNION ALL SELECT c FROM t5b) AS dt
 WHERE dt.c LIKE 'abc';
DROP TABLE t5a, t5b;

