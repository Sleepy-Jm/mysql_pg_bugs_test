USE `replay_654b3a63d7270d90765251cc`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113358; source: cmain, c538763, c538769, c538772
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET @old_sql_mode=@@SESSION.sql_mode;
SET @old_optimizer_switch=@@SESSION.optimizer_switch;
SET SESSION sql_mode=CONCAT_WS(',',NULLIF(@@SESSION.sql_mode,''),'ONLY_FULL_GROUP_BY');
CREATE TABLE t1(a INT,b INT,c INT);
CREATE TABLE t2(a INT);
INSERT INTO t1 VALUES(1,1,1),(2,1,1);
INSERT INTO t2 VALUES(1),(2),(1);
SET SESSION optimizer_switch='subquery_to_derived=off';
SELECT b,(SELECT COUNT(t.a) FROM t2 AS t WHERE t.a=t1.a) AS c FROM t1;
SELECT b,(SELECT COUNT(t.a) FROM t2 AS t WHERE t.a=t1.a) AS c FROM t1 GROUP BY b;
SET SESSION optimizer_switch='subquery_to_derived=on';
SELECT b,(SELECT COUNT(t.a) FROM t2 AS t WHERE t.a=t1.a) AS c FROM t1 GROUP BY b;

-- Read-only postchecks for report 113358; run in the same disposable schema/session.
SELECT * FROM t1 ORDER BY a; SELECT * FROM t2 ORDER BY a; SELECT @@sql_mode,@@optimizer_switch;
