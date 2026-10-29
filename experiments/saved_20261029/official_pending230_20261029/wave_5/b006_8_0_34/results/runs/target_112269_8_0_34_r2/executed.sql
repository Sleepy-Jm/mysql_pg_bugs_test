USE `replay_7dcaec2aea02f36a424f7ad8`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #112269; source: cmain, c535878
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 DECIMAL UNIQUE);
CREATE TABLE t2(c0 FLOAT, c1 TEXT);
CREATE INDEX i0 ON t2(c1(1));

INSERT INTO t0 VALUES(1);
INSERT INTO t2 VALUES(NULL, '1j');

SELECT * FROM t0, t2 WHERE t2.c1 = t0.c0;  -- {1|NULL|1j}
SELECT /*+ JOIN_ORDER(t2, t0)*/ * FROM t0, t2 WHERE t2.c1 = t0.c0;

-- Read-only postchecks for report 112269; run in the same disposable schema/session.
SELECT * FROM t0; SELECT * FROM t2;
