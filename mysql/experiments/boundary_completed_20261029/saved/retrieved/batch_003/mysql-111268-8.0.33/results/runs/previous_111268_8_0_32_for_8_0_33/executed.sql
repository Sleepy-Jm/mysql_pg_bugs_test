USE `replay_1e3318b1f1e0bc2b3f9af6cd`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #111268; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t(id INT,c1 VARCHAR(10) COLLATE utf8mb4_bin) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
INSERT INTO t VALUES(1,'abc'),(2,'abc ');
SET character_set_connection=utf8mb3;
SELECT * FROM t WHERE c1='abc' AND c1='abc ';
SET character_set_connection=utf8mb4;
SELECT * FROM t WHERE c1='abc' AND c1='abc ';

-- Read-only evidence after the unchanged source SQL, same session.
SELECT id,HEX(c1) AS stored_hex FROM t ORDER BY id;
SELECT COLLATION_NAME,PAD_ATTRIBUTE FROM information_schema.COLLATIONS WHERE COLLATION_NAME='utf8mb4_bin';
SELECT @@character_set_connection,@@collation_connection;
