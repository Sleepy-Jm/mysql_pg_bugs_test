USE `replay_194cf2c09901a05d242306a1`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #112527; source anchors: cmain, c536451
-- Static preparation only; not executed. See case.json before any future isolated run.
create table t1 (vkey int, pkey int);
insert into t1 values (3, 13000);
insert into t1 values (5, 15000);
insert into t1 values (28, 38000);

-- Query1

select  
  count(*) as c_1
from 
  t1 as ref_0
where (REPEAT(REPEAT(case when (null <= ref_0.vkey) then (null) else (case when false then ('o#W4O') else ('o#W4O') end) end, ref_0.vkey), ref_0.pkey)) >= 'i';


SHOW WARNINGS;


select  
  count(*) as c_1
from 
  t1 as ref_0
where (REPEAT(REPEAT(case when (null <= ref_0.vkey) then (null) else ('o#W4O') end, ref_0.vkey), ref_0.pkey)) >= 'i';


SHOW WARNINGS;

-- Read-only evidence after the unchanged source SQL, same session.
SELECT @@max_allowed_packet AS packet_limit;
SELECT COUNT(*) AS loaded_rows,MAX(5*vkey*pkey) AS maximum_generated_bytes FROM t1;
