USE `replay_d9d56fd1097dbc48a2c6a0ef`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
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

-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS loaded_rows FROM t1;
