USE `replay_fd6971aaf60fb9c2576dd783`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #114714; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t1 (a INT, b INT);
INSERT INTO t1 VALUES (4, 40), (1, 10), (2, 20), (2, 20), (3, 30);

CREATE TABLE t2 SELECT DISTINCT a FROM t1;

ANALYZE TABLE t1, t2;


 EXPLAIN FORMAT=TREE SELECT (SELECT t2.a FROM t2 WHERE t2.a = t1.a) aa, b, COUNT(b) FROM t1 GROUP BY aa, b ORDER BY -aa, -b;

-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS t1_rows FROM t1;
SELECT COUNT(*) AS t2_rows FROM t2;
