-- MySQL report #45257; source anchors: c231617, c233486
-- Static preparation only; NOT EXECUTED. Run only in a fresh isolated schema/instance.
drop table if exists t1;
create table t1(a varchar(128),b varchar(128),key(a),key(b))engine=innodb;
insert into t1 values (repeat('a',128),repeat('b',128));
insert into t1 select * from t1;
insert into t1 select * from t1;
insert into t1 select * from t1;
insert into t1 select * from t1;
insert into t1 select * from t1;
insert into t1 select * from t1;
set session sort_buffer_size=1;
select * from t1 force index(a,b) where a like 'a%' or b like 'b%' order by a,b;
SHOW WARNINGS;
SELECT @@SESSION.sort_buffer_size;
