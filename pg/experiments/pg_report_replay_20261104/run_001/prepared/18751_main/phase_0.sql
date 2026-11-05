create table t1(t timestamptz primary key, v text);
create table t2(t timestamptz primary key, v text);


insert into t1(t, v)
select to_timestamp(i * 3600), i::text
from generate_series(0, 24 * 7 - 1) as t(i);


insert into t2(t, v)
select to_timestamp(i * 3600), i::text
from generate_series(24 * 7, 100000) as t(i);
