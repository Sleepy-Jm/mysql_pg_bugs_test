USE `replay_f673975e36ced1b128d8e174`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
CREATE TABLE test1 (id decimal(12,2));
INSERT INTO test1 VALUES (0.00),(NULL);
CREATE TABLE test2 (id decimal(12,2));
INSERT INTO test2 VALUES (0.00),(NULL);
SELECT * FROM test1;
SELECT * FROM test2;
SELECT * FROM test1 c LEFT JOIN test2 d ON c.id=d.id;
SELECT * FROM test1 c RIGHT JOIN test2 d ON c.id=d.id;

-- No extra postcheck required by frozen oracle.
