USE `replay_7888578ed69eb0bf41dd0caf`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113319; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t1(a INT); CREATE TABLE t2(a INT);
INSERT INTO t1 VALUES(1),(2),(3),(4); INSERT INTO t2 VALUES(1),(2);
SET optimizer_switch='subquery_to_derived=off';
SELECT (SELECT COUNT(1) AS cnt FROM t2 WHERE t2.a=t1.a HAVING cnt>0) FROM t1;
SET optimizer_switch='subquery_to_derived=on';
SELECT (SELECT COUNT(1) AS cnt FROM t2 WHERE t2.a=t1.a HAVING cnt>0) FROM t1;

-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS t1_rows FROM t1;
SELECT COUNT(*) AS t2_rows FROM t2;
