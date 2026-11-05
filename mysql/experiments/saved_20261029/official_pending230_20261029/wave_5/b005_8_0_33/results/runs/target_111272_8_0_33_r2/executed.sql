USE `replay_4a89fd81582677f810659b2d`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #111272; source anchors: cmain, c533174
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET NAMES utf8mb4;
-- case 1
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (c1 TINYTEXT, KEY i0 (c1(1)));
INSERT INTO t1 VALUES ("͕fB-'"),("^1o");
SELECT c1 FROM t1 WHERE c1 > ("?ykFo|1"); -- 1

-- case 2
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (c1 TINYTEXT);
INSERT INTO t1 VALUES ("͕fB-'"),("^1o");
SELECT c1 FROM t1 WHERE c1 > ("?ykFo|1"); -- 2

-- Read-only postchecks for report 111272; run in the same disposable schema/session.
SELECT HEX(c1) FROM t1 ORDER BY HEX(c1); SELECT @@collation_connection,@@collation_database,@@sql_mode;
