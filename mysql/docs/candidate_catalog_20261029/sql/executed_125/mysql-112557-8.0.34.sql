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
