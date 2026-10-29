USE `replay_101fc7960061f4e744bc2be3`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #114384; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE IF NOT EXISTS t1(c0 SMALLINT) ;
INSERT INTO t1(c0) VALUES(0.49);
CREATE INDEX i0 ON t1(c0);

SELECT t1.c0 FROM t1 WHERE t1.c0 IN (LOG(0.6261534882548163));

SELECT c0 FROM (SELECT t1.c0, (t1.c0 IN (LOG(0.6261534882548163))) IS TRUE AS flag FROM t1) as t WHERE flag=1;

-- Read-only postchecks for report 114384; run in the same disposable schema/session.
SELECT c0,LOG(0.6261534882548163) AS log_value FROM t1; EXPLAIN SELECT t1.c0 FROM t1 WHERE t1.c0 IN (LOG(0.6261534882548163)); SHOW WARNINGS;
