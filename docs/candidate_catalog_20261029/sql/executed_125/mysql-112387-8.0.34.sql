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
