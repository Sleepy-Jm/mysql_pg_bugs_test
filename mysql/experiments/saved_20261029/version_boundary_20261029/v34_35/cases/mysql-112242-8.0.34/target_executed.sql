USE `replay_a2a085193056a8a9a1a6cb74`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #112242; source: cmain, c535808
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET @old_optimizer_switch=@@SESSION.optimizer_switch;
CREATE TABLE t0(c0 INT);
INSERT INTO t0(c0) VALUES(1);
CREATE INDEX i0 USING HASH ON t0(c0) INVISIBLE;

SET SESSION optimizer_switch = 'use_invisible_indexes=off';
SELECT t0.c0 FROM t0 WHERE COALESCE(0.6) IN (t0.c0); -- {}
SET SESSION optimizer_switch = 'use_invisible_indexes=on';
SELECT t0.c0 FROM t0 WHERE COALESCE(0.6) IN (t0.c0);

-- Read-only postcheck appended after unchanged source SQL.
SELECT c0 FROM t0; SELECT INDEX_NAME,INDEX_TYPE,IS_VISIBLE FROM information_schema.statistics WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='t0'; SELECT @@optimizer_switch;
