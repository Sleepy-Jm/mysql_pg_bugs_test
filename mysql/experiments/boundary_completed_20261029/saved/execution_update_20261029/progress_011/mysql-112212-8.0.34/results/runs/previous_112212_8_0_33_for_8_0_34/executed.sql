USE `replay_abeec9d9f184ae77aaf1cc44`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #112212; source: cmain, c535747
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET @old_optimizer_switch=@@SESSION.optimizer_switch;
SET SESSION optimizer_switch='subquery_to_derived=off';
CREATE TABLE type1(c1 bit(8), c2 json, c3 int, c4 json);
INSERT INTO type1 VALUES(b'1010', '{"key1": "value1", "key2": "value2"}', 1, '["key1"]');
INSERT INTO type1 VALUES(b'1011', '{"key1": "value1", "key2": "value2"}', 2, '["key2", "key22"]');
INSERT INTO type1 VALUES(b'1111', '{"key3": "value3", "key3": "value3"}', 3, '{"key3": 3}');
INSERT INTO type1 VALUES(null, null, null, '["key4"]');
CREATE TABLE type2(c1 bit(8), c2 json, c3 int, c4 varchar(20));
INSERT INTO type2 VALUES(b'1010', '{"key1": "value1", "key2": "value2"}', 1, "key1");
INSERT INTO type2 VALUES(b'1100', '{"key2": "value2", "key2": "value2"}', 2, "key2");
INSERT INTO type2 VALUES(b'1100', '{"key2": "value2", "key2": "value2"}', 2, "key22");
INSERT INTO type2 VALUES(b'1111', '{"key3": "value3", "key3": "value3"}', 3, "key3");
INSERT INTO type2 VALUES(null, null, null, "key4");

SELECT BIN(c1), c3 FROM type1 where c2 = (select var_pop(c2) from type2 where type2.c1 = type1.c1);

set @@optimizer_switch='subquery_to_derived=on';

SELECT BIN(c1), c3 FROM type1 where c2 = (select var_pop(c2) from type2 where type2.c1 = type1.c1);

-- Read-only postchecks for report 112212; run in the same disposable schema/session.
SELECT COUNT(*) AS type1_rows FROM type1; SELECT COUNT(*) AS type2_rows FROM type2; SELECT @@optimizer_switch;
