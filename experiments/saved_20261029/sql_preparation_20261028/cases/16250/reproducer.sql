-- MySQL report #16250; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
create table t1 (b bit(1)); insert into t1 values (0),(1),(1);

select * from t1 where b='1';
#+---+
#| b |
#+---+
#|  |
#|  |
#+---+

alter table t1 add index (b);
select * from t1 where b='1';
#Empty set (0.00 sec)

drop table t1;

create table t1 (b bit(1) not null); insert into t1 values (0),(1),(1);

select * from t1 where b='1';
#+---+
#| b |
#+---+
#|  |
#|  |
#+---+

alter table t1 add index (b);
select * from t1 where b='1';
# Empty set, 1 warning (0.01 sec)
show warnings;
# Warning | 1264 | Out of range value adjusted for column 'b' at row 1 

drop table t1;
