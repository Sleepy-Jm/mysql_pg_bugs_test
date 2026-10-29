USE `replay_5b90663f4a0d2cea38cb7983`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #72100; source anchors: cmain, c418803
-- Static preparation only; NOT EXECUTED. Run only in a fresh isolated schema/instance.
create table t (id serial, d decimal(65,30));
insert into t values (),(),(),(),(),(),(),(),();
insert into t values (),(),(),(),(),(),(),(),();
insert into t values (),(),(),(),(),(),(),(),();
update t set d = concat('1e-', id);
select d, d mod 1 from t;
SELECT COUNT(*) AS mismatches FROM t WHERE NOT (d <=> MOD(d,1));
