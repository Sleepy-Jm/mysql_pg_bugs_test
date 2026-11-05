USE `replay_51f2adafc4f3aa0bba4a4a0c`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
CREATE TABLE t1(a INTEGER,b INTEGER,PRIMARY KEY(a));
CREATE TABLE t2(a INTEGER,b INTEGER,PRIMARY KEY(a,b));
INSERT INTO t1 VALUES(1,1),(2,2);
INSERT INTO t2 VALUES(2,1),(2,2),(2,3),(2,4);
ANALYZE TABLE t1,t2;
EXPLAIN FORMAT=TREE SELECT t1.b FROM t1 JOIN t2 WHERE t1.a=t2.a AND t2.a=2 AND t2.b>=t1.b AND t2.b<=t1.b+2;

-- No extra postcheck required by frozen oracle.
