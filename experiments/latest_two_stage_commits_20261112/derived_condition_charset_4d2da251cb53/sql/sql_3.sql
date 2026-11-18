DROP TABLE IF EXISTS t3a, t3b;
CREATE TABLE t3a (c VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin);
CREATE TABLE t3b (c VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin);
INSERT INTO t3a VALUES ('Ä'),('A');
INSERT INTO t3b VALUES ('Ä'),('A');
SET NAMES latin1;
SET optimizer_switch='derived_condition_pushdown=on';
SELECT dt.c FROM (SELECT c FROM t3a UNION ALL SELECT c FROM t3b) AS dt
 WHERE dt.c LIKE 'Ä';
SET NAMES utf8mb4;
DROP TABLE t3a, t3b;

