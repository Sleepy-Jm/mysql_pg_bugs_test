USE `replay_dc0e32b639b210a8a92a47be`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #112387; source anchors: cmain, c536188
-- Static preparation only; not executed. See case.json before any future isolated run.
create table t0 (c4 double);
create table t1 (c8 varchar(200));
insert into t1 values (null);
insert into t0 values (-66.49);
insert into t0 values (null);

-- Test case 1

select * from t0
where
not (null in (
    select 1 from (select 1) as subq where false
    union all
    select
        ref_5.c8 as c_0
      from
        t1 as ref_5
      where t0.c4 >= t0.c4));


-- Test case 2
select * from t0
where
not (null in (
    select
        ref_5.c8 as c_0
      from
        t1 as ref_5
      where t0.c4 >= t0.c4));

-- Read-only postchecks for report 112387; run in the same disposable schema/session.
SELECT c4 FROM t0 ORDER BY c4; SELECT c8 FROM t1;
