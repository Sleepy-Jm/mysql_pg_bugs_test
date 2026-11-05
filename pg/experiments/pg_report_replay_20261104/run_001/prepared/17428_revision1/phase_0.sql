create table mytable (
    id serial,
    other int
);
select (select count(*) from mytable), last_value from mytable_id_seq; -- 0 (displayed expected output removed)
insert into mytable (other) values (0);
select (select count(*) from mytable), last_value from mytable_id_seq; -- 1 (displayed expected output removed)
insert into mytable (other) values (0);
select (select count(*) from mytable), last_value from mytable_id_seq; -- 2 (displayed expected output removed)
insert into mytable (other) values (0);
select (select count(*) from mytable), last_value from mytable_id_seq; -- 3 (displayed expected output removed)
