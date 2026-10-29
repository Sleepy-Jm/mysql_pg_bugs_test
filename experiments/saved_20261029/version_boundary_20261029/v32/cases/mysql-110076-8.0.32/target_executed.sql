USE `replay_bdb0dd5726391611a79527db`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
CREATE TABLE mytable(ID INTEGER NOT NULL,a VARCHAR(4) NOT NULL,b VARCHAR(4) NOT NULL,c VARCHAR(3) NOT NULL);
INSERT INTO mytable(ID,a,b,c) VALUES (1,'a1','b1','c1');
INSERT INTO mytable(ID,a,b,c) VALUES (2,'a2','b2','c2');
SELECT ID,(SELECT MAX(col1) FROM (VALUES ROW(a),ROW(b),ROW(c)) AS x(col1)) AS max FROM mytable;

-- No extra postcheck required by frozen oracle.
