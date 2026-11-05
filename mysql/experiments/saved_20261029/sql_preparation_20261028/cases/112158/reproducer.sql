-- MySQL report #112158; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
show variables like "%char%";
show variables like "%collation%";
show variables like "lower_case_table_names";
create database db1;
use db1;
delimiter $$
create procedure p1()
begin
select "db1.p1";
end $$
delimiter ;
create database DB1;
use DB1;
delimiter $$
create procedure p1()
begin
select "DB1.p1";
end $$
delimiter ;
call db1.p1();
call DB1.p1();
