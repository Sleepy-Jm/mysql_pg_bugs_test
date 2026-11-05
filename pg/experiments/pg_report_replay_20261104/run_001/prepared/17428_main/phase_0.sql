create table mytable (
    id serial,
    other int
);
select (select count(*) from mytable), last_value from mytable_id_seq; -- 0,
1
insert into mytable (other) values (0);
select (select count(*) from mytable), last_value from mytable_id_seq; -- 1,
1
insert into mytable (other) values (0);
select (select count(*) from mytable), last_value from mytable_id_seq; -- 2,
2
insert into mytable (other) values (0);
select (select count(*) from mytable), last_value from mytable_id_seq; -- 3,
3;
