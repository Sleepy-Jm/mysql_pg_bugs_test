-- MySQL report #24657; source anchors: cmain, c94687
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
drop table if exists t1;

create table t1 (a varchar(19));

insert into t1 select rand();
insert into t1 select rand() from t1;
insert into t1 select rand() from t1;
insert into t1 select rand() from t1;
insert into t1 select rand() from t1;
SELECT COUNT(*) AS row_count FROM t1;
SELECT 1 AS server_alive;
