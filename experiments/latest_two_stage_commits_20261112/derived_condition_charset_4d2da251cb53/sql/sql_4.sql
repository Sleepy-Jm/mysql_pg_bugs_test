DROP TABLE IF EXISTS t4a, t4b;
CREATE TABLE t4a (c VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin);
CREATE TABLE t4b (c VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin);
INSERT INTO t4a VALUES ('Ä'),('A');
INSERT INTO t4b VALUES ('Ä'),('A');
SET optimizer_switch='derived_condition_pushdown=on';
SELECT dt.m FROM (
  SELECT (c LIKE _utf8mb4'Ä') AS m FROM t4a
  UNION ALL
  SELECT (c LIKE _utf8mb4'Ä') AS m FROM t4b
) AS dt WHERE dt.m = 1;
SELECT dt.m FROM (
  SELECT (c LIKE 'Ä') AS m FROM t4a
  UNION ALL
  SELECT (c LIKE 'Ä') AS m FROM t4b
) AS dt WHERE dt.m = 1;
DROP TABLE t4a, t4b;

