USE `replay_e7e0bb0e5a1c5dffdde6f529`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #116852; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE mvi(id INT PRIMARY KEY,t INT,j JSON,INDEX index1(t,(CAST(j->'$' AS SIGNED ARRAY))),INDEX index2(t,(CAST(j->'$[*]' AS SIGNED ARRAY))));
INSERT INTO mvi VALUES(1,1,'[1,2,3]'),(2,1,'[]'),(3,1,NULL);
SELECT * FROM mvi FORCE INDEX(index1) WHERE t=1 ORDER BY id;
SELECT * FROM mvi FORCE INDEX(index2) WHERE t=1 ORDER BY id;
SELECT * FROM mvi IGNORE INDEX(index1,index2) WHERE t=1 ORDER BY id;

-- Read-only postcheck appended after unchanged source SQL.
SELECT id,t,CAST(j AS CHAR) FROM mvi IGNORE INDEX(index1,index2) ORDER BY id; SHOW CREATE TABLE mvi; EXPLAIN SELECT * FROM mvi FORCE INDEX(index1) WHERE t=1 ORDER BY id; EXPLAIN SELECT * FROM mvi FORCE INDEX(index2) WHERE t=1 ORDER BY id;
