USE `replay_acf42355f0f935241d6c911b`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #107337; source anchors: cmain, c522679, c554592
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t(a TIME);
INSERT INTO t VALUES('08:00:00');
SELECT * FROM t WHERE a IN ('08:00:00',NULL);
SELECT * FROM t WHERE a IN ('08:00:00','');
SELECT * FROM t WHERE a IN ('08:00:00','07:59:59');
SELECT * FROM t WHERE a IN (TIME'08:00:00',NULL);

-- Run after the unmodified source script, in the same owned schema; read-only evidence only.
SELECT COUNT(*) AS loaded_rows, MIN(a) AS min_a, MAX(a) AS max_a FROM t;
