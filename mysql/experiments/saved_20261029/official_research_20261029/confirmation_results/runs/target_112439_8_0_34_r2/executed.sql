USE `replay_add07ac56d35abcfd6c51b6e`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #112439; source: cmain, c536279
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t(i INT PRIMARY KEY);
INSERT INTO t VALUES(1),(2),(3);
SELECT * FROM t WHERE i IN(VALUES ROW(1),ROW(2));
SELECT * FROM t WHERE i IN(SELECT 1 UNION SELECT 2);

-- Run after the unmodified source script, in the same owned schema; read-only evidence only.
SELECT i FROM t ORDER BY i;
