create table pt (a int, b int) partition by list (b);
create table t(a pt, check (a = '(1, 2)'::pt));
alter table pt alter column a type char(4);
