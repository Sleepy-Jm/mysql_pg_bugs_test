USE `replay_4ef1afcbd53346e1b3da7afc`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
CREATE TABLE t1(a int,b int,c varchar(100));
CREATE TABLE t2(a int,b int,c varchar(100));
EXPLAIN FORMAT=TREE SELECT * FROM t1 LEFT JOIN t2 ON t1.a=t2.a AND t2.a>0;

-- No extra postcheck required by frozen oracle.
