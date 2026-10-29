-- MySQL report #116398; source anchors: cmain, c548049, c548050
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
create table `tbl` (
  `id` int unsigned not null auto_increment,
  `user_id` int default null,
  primary key (`id`)
) engine=innodb default charset=utf8mb4 collate=utf8mb4_0900_ai_ci;
replace into tbl(user_id) values(1),(2),(3),(4),(5),(6),(7),(8),(9),(0);
replace into tbl(user_id) select a.user_id from tbl a,tbl b,tbl c,tbl d;

create table `fp_tbl` (
  `id` int unsigned not null auto_increment,
  `user_id` int default null,
  primary key (`id`)
) engine=innodb default charset=utf8mb4 collate=utf8mb4_0900_ai_ci;
replace into fp_tbl(user_id) values(1),(2),(3),(4),(5),(6),(7),(8),(9),(0);
replace into fp_tbl(user_id) select a.user_id from fp_tbl a,fp_tbl b,fp_tbl c,fp_tbl d;

create table `fp_pol` (
  `id` int unsigned not null auto_increment,
  `lead_id` int unsigned default null,
  primary key (`id`)
) engine=innodb default charset=utf8mb4 collate=utf8mb4_0900_ai_ci;
set @a:=0;
replace into fp_pol(lead_id) values(1),(2),(3),(4),(5),(6),(7),(8),(9),(0);
replace into fp_pol(lead_id) select @a:=@a+1 from fp_pol a,fp_pol b,fp_pol c,fp_pol d;
replace into fp_pol(lead_id) select @a:=@a+1 from fp_pol a,fp_pol b limit 9989990;
replace into fp_pol(lead_id) select @a:=@a+1 from fp_pol a;

delete from fp_tbl where id in (1,2);
delete from fp_pol where id in (1,2);

analyze table fp_pol,fp_tbl,tbl;

select * from tbl where id in (1,2);
select * from fp_tbl where id in (1,2);
select * from fp_pol where id in (1,2);

explain select a.id, count(*) as n from tbl as a left join fp_tbl as f on f.id = a.id left join fp_pol as p on p.lead_id = f.id where a. id in (1,2) and p.id is null group by a.id;

set session join_buffer_size=256*1024;

select a.id, count(*) as n
from tbl as a
left join fp_tbl as f on f.id = a.id
left join fp_pol as p on p.lead_id   = f.id
where a.id in (1,2) and p.id is null
group by a.id;

set session join_buffer_size=1024*1024*1024;

select a.id, count(*) as n
from tbl as a
left join fp_tbl as f on f.id = a.id
left join fp_pol as p on p.lead_id   = f.id
where a.id in (1,2) and p.id is null
group by a.id;

select version();
