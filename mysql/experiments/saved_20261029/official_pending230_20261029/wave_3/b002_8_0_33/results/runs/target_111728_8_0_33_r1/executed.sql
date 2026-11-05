USE `replay_a7216595c3f6c351f983a95a`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #111728; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE ta(id BIGINT,PRIMARY KEY(id));
INSERT INTO ta(id) VALUES(1801425248110076165);
CREATE TABLE tb(value VARCHAR(50));
INSERT INTO tb(value) VALUES("1801425248110076222");
SELECT value FROM tb WHERE value IN(SELECT id FROM ta);
SELECT value FROM tb WHERE value IN(SELECT /*+no_index(ta)*/ id FROM ta);

-- Read-only evidence after the unchanged source SQL, same session.
SELECT id FROM ta;
SELECT value,HEX(value) AS stored_hex FROM tb;
SELECT @@session.sql_mode;
