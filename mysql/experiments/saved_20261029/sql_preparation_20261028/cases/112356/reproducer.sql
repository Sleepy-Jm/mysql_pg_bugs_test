-- Report #112356; source anchors: cmain, c536117, c537121
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE `test1` (   `a` int(11) NOT NULL,   `b` int(11) DEFAULT NULL,   PRIMARY KEY (`a`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

insert into test1 values (1,1),(2,2),(3,3);

select b
from (
select case when 1=1 then b else 1 end as b
from (
select b from test1 group by b) t1
) t2
where t2.b is not null;
