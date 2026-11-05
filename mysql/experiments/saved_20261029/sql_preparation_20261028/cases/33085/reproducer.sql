-- MySQL report #33085; source anchors: cmain, c146848
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
drop function if exists f1;
delimiter //
create function f1 (i int)
returns int
not deterministic
no sql
begin
  return i;
end//
delimiter ;

drop table if exists t1;
create table t1 (i int);
insert into t1 values (1),(2);

select f1(1), count(*) 
from t1
group by f1(1);
SELECT f1(i), COUNT(*) FROM t1 GROUP BY f1(i);
