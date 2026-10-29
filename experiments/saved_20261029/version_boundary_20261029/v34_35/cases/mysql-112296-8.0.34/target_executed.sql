USE `replay_ea3ca9ab3b017cba40d536b5`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #112296; source: cmain, c535940, c539425
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 INT);
CREATE TABLE t1(c0 INT);
CREATE TABLE t2(c0 INT);
REPLACE INTO t0(c0) VALUES(1), (2);
INSERT INTO t2(c0) VALUES(3);

SELECT t0.c0 FROM t0 LEFT JOIN t1 ON FALSE RIGHT JOIN t2 ON (t1.c0 IS NOT NULL) IN (t2.c0 = 1000); -- {NULL}
SELECT /*+ NO_BNL(t0)*/ t0.c0 FROM t0 LEFT JOIN t1 ON FALSE RIGHT JOIN t2 ON (t1.c0 IS NOT NULL) IN (t2.c0 = 1000);

-- Read-only postchecks for report 112296; run in the same disposable schema/session.
SELECT * FROM t0; SELECT COUNT(*) AS t1_rows FROM t1; SELECT * FROM t2;
