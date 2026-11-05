USE `replay_915999642d117d8282a59300`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #112389; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
create table t0 (c0 int);
create table t4 (c17 int);
insert into t0  values (16);


select
  1 as c_0
from
  ((select
          case when true then ref_0.c17 else ref_0.c17 end as c_1
        from
          t4 as ref_0
        ) as subq_0
    right outer join t0 as ref_1
    on (subq_0.c_1 = ref_1.c0))
where FIELD(subq_0.c_1, null) <= (ref_1.c0);



select
  1 as c_0
from
  ((select
          ref_0.c17 as c_1
        from
          t4 as ref_0
        ) as subq_0
    right outer join t0 as ref_1
    on (subq_0.c_1 = ref_1.c0))
where FIELD(subq_0.c_1, null) <= (ref_1.c0);

-- Read-only postcheck appended after unchanged source SQL.
SELECT c0 FROM t0; SELECT COUNT(*) AS n FROM t4; SELECT FIELD(NULL,NULL) AS field_null_null;
