USE `replay_c9f012b00d2e4b0409f3a08d`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
SELECT * FROM (SELECT "の" AS v) tbl WHERE tbl.v = "の";
SHOW WARNINGS;
CREATE TABLE tbl(id INT PRIMARY KEY,v VARCHAR(30)) DEFAULT CHARSET utf8mb4;
INSERT INTO tbl VALUES (1,'の');
SELECT * FROM (SELECT * FROM tbl UNION SELECT * FROM tbl) t WHERE t.v='の';
SHOW WARNINGS;

SELECT id,v FROM tbl;