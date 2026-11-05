USE `replay_16b9086527f29caa62a7427a`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
CREATE TABLE test (id int unsigned auto_increment key,name varchar(50)) ENGINE=INNODB;
INSERT INTO test(id,name) VALUES(1,'姜志福');
SELECT * FROM (SELECT * FROM test UNION ALL SELECT * FROM test) a WHERE id=1 AND name='姜志福';
SHOW WARNINGS;

SELECT id,name FROM test;