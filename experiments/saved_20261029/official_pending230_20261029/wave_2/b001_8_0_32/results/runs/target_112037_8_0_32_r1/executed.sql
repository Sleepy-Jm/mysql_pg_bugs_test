USE `replay_45b73d02780f730a50bb9b02`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #112037; source: cmain, c535234
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET @old_optimizer_switch=@@SESSION.optimizer_switch;
CREATE TABLE t1(a INT);
INSERT INTO t1 VALUES (1),(2),(3),(4);
ANALYZE TABLE t1;
SET optimizer_switch='subquery_to_derived=on';
EXPLAIN analyze SELECT a + (SELECT SUM(a) FROM (SELECT a FROM t1 GROUP BY a) t2 ) FROM t1;

-- Read-only postchecks for report 112037; run in the same disposable schema/session.
SELECT a+(SELECT SUM(a) FROM (SELECT a FROM t1 GROUP BY a) t2) AS result_value FROM t1 ORDER BY a; SELECT a FROM t1 ORDER BY a;
