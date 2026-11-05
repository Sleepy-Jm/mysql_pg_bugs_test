USE `replay_9c70d15c3f8a431f80030026`;
SET time_zone="+00:00";


create table t2 (vkey int, pkey int, c19 int, c20 double, c22 int);
insert into t2 values (135, 145000, -13, 17.61, 0);


select  
  case when true then null else (DENSE_RANK() over (partition by ref_0.pkey order by ref_0.vkey desc, ref_0.pkey asc)) end as c_0, 
  case when ((LAST_VALUE(ref_0.pkey) over (partition by ref_0.c19 order by ref_0.vkey desc, ref_0.pkey desc)) in (select  
          ref_0.c22 as c_0
        from 
          t2 as ref_8
        )) then ref_0.c20 else ref_0.c20 end
       as c_1 
from 
  t2 as ref_0
order by c_1 desc;
select
  case when true then null else (DENSE_RANK() over (partition by ref_0.pkey order by ref_0.vkey desc, ref_0.pkey asc)) end as c_0,
  ref_0.c20 as c_1
from
  t2 as ref_0
order by c_1 desc;