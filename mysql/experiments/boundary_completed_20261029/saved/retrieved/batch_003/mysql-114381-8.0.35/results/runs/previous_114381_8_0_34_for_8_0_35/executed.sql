USE `replay_2b7bae427df8bf244f9f17e0`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #114381; source: cmain, c541692
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 DOUBLE) ;
CREATE TABLE t1 LIKE t0;
INSERT IGNORE INTO t1(c0) VALUES(1);
INSERT INTO t0(c0) VALUES(0.1);

SELECT t1.c0 AS _c0 FROM t1, t0 WHERE (( EXISTS (SELECT 1 )) < ((NOT t0.c0))) IN (((t1.c0) XOR ("")) / (TIMEDIFF('3939-09-13 16:49:10.309835', '4722-09-08 23:55:52.675528')));
SELECT _c0 FROM (SELECT t1.c0 AS _c0, ((( EXISTS (SELECT 1 )) < ((NOT t0.c0))) IN (((t1.c0) XOR ("")) / (TIMEDIFF('3939-09-13 16:49:10.309835', '4722-09-08 23:55:52.675528')))) IS TRUE AS flag FROM t1, t0) as t WHERE flag=1;

-- Read-only postchecks for report 114381; run in the same disposable schema/session.
SELECT * FROM t0; SELECT * FROM t1; SELECT TIMEDIFF('3939-09-13 16:49:10.309835','4722-09-08 23:55:52.675528'); SHOW WARNINGS;
