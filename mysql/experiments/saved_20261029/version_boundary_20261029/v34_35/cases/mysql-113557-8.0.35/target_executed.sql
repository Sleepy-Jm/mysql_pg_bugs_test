USE `replay_4eca1843d2d9bad70e9a11fc`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113557; source: cmain, c539454
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
create table t(a int, d json, index iad(a, (cast(d->'$.b' as signed array))));
insert into t value(1,'{"b":[]}'), (2,'{"b":[]}');
select * from t use index (iad) where a = 1;
select * from t ignore index (iad) where a = 1;

-- Read-only evidence after the unchanged source SQL, same session.
SELECT a,CAST(d AS CHAR) AS stored_json FROM t IGNORE INDEX(iad) ORDER BY a;
EXPLAIN SELECT * FROM t USE INDEX(iad) WHERE a=1;
