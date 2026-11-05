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
