USE `replay_1ea77b90eedc69079445e939`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113506; source: cmain, c539290, c539293, c539294, c539322, c544157
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET NAMES utf8mb4;
CREATE TABLE t1(a CHAR(10) CHARACTER SET utf8mb4);
INSERT INTO t1 VALUES('你好'),('中午好');
SELECT a,CONVERT(a USING latin1) FROM t1 ORDER BY CONVERT(a USING utf8mb4);
SELECT a FROM t1 ORDER BY CONVERT(a USING utf8mb4);

-- Read-only postchecks for report 113506; run in the same disposable schema/session.
SELECT a,HEX(a),CHARSET(a),COLLATION(a) FROM t1 ORDER BY a; SELECT @@character_set_connection,@@collation_connection;
