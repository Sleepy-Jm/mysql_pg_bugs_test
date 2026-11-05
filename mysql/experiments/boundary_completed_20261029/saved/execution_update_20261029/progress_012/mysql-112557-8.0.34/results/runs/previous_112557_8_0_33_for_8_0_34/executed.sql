USE `replay_6e8aadb9a178a330a9825dd8`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #112557; source: cmain, c536507, c537445, c537488, c537535, c538930, c546013
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
create table t1 (vkey int, pkey int, c5 int, c7 varchar(200));
insert into t1 values (20, 30000, 59, null);
insert into t1 values (59, 69000, null, null);
select  
  ref_0.c5 >= (case when (true and exists (
        select  
              ref_2.pkey as c_3
            from 
              t1 as ref_2
            where ref_2.vkey between ref_0.c5 and ref_0.c5
        )) then null else (case when (FIRST_VALUE('') over (partition by ref_0.c7 order by ref_0.vkey asc, ref_0.pkey desc) >= null) then null else ref_0.pkey end
        ) end
      ) as c_6
from 
  t1 as ref_0;
select  
  ref_0.c5 >= (case when (exists (
        select  
              ref_2.pkey as c_3
            from 
              t1 as ref_2
            where ref_2.vkey between ref_0.c5 and ref_0.c5
        )) then null else (case when (FIRST_VALUE('') over (partition by ref_0.c7 order by ref_0.vkey asc, ref_0.pkey desc) >= null) then null else ref_0.pkey end
        ) end
      ) as c_6
from 
  t1 as ref_0;

-- Read-only postchecks for report 112557; run in the same disposable schema/session.
SELECT vkey,pkey,c5,c7 FROM t1 ORDER BY vkey;
