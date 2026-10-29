-- MySQL report #114524; source: cmain, c541999, c547320, c548407, c551563, c553072
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
set names utf8mb4;
create table t1 (id int auto_increment primary key, c1 varchar(255), c2 json null);
prepare it from 'insert into t1(c2, c1) values(?, ?)';
set @a=0;
set @b=2;
execute it using @b, @a;
set @b='{}';

# Unexpectedly fails with ERROR 3144
execute it using @b, @a;
