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
