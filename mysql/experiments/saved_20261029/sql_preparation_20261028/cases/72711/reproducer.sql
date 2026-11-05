-- MySQL report #72711; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
set sql_mode='ansi';
create table t (dt datetime);
insert into t values ('0000-00-00 12:34:56');
select dt, hour(dt) from t;
select dt, hour(dt) from (select cast('0000-00-00 12:34:56' as datetime) dt) sub;
select cast('0000-00-00 12:34:56' as datetime) `dt`, hour(cast('0000-00-00 12:34:56' as datetime)) `hour(dt)` from dual;
