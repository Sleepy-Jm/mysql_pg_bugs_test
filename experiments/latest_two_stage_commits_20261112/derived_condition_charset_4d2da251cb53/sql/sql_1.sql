DROP TABLE IF EXISTS t1a, t1b;
CREATE TABLE t1a (c VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin);
CREATE TABLE t1b (c VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin);
INSERT INTO t1a VALUES ('Ä'),('A'),('ä');
INSERT INTO t1b VALUES ('Ä'),('A'),('ä');
SET optimizer_switch='derived_condition_pushdown=on';
SELECT dt.c FROM (SELECT c FROM t1a UNION ALL SELECT c FROM t1b) AS dt
 WHERE dt.c LIKE _utf8mb4'Ä';
SELECT dt.c FROM (SELECT c FROM t1a UNION ALL SELECT c FROM t1b) AS dt
 WHERE dt.c LIKE 'Ä';
DROP TABLE t1a, t1b;

