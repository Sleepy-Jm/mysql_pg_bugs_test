-- MySQL report #112394; source: cmain, c536187
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
create table t0 (vkey int);
insert into t0 (vkey) values (5);
select 1 as c0
  from
    ((select
            case when true then 0 else 0 end as c_0
          from
            t0 as ref_5
          ) as subq_2
      right outer join t0 as ref_6
      on (subq_2.c_0 = ref_6.vkey ))
  where exists (
      select 
          1 
        from 
          t0 as ref_9
        where (subq_2.c_0 <> ref_9.vkey));
select 1 as c0
  from
    ((select
            0 as c_0
          from
            t0 as ref_5
          ) as subq_2
      right outer join t0 as ref_6
      on (subq_2.c_0 = ref_6.vkey ))
  where exists (
      select 
          1 
        from 
          t0 as ref_9
        where (subq_2.c_0 <> ref_9.vkey));
