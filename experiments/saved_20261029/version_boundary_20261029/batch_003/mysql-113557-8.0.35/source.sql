-- MySQL report #113557; source: cmain, c539454
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
create table t(a int, d json, index iad(a, (cast(d->'$.b' as signed array))));
insert into t value(1,'{"b":[]}'), (2,'{"b":[]}');
select * from t use index (iad) where a = 1;
select * from t ignore index (iad) where a = 1;
