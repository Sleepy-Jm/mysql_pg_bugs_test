-- MySQL report #111564; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
create table t1 (a int not null, b int not null);
create table t2 (a decimal(15,2) not null, b int not null);

explain format=tree
select * from t1, t2 where t2.a = (SELECT MIN(t2.a) FROM t2 WHERE t1.a = t2.a);

explain format=tree
select * from t1 left join t2 on t1.b = t2.b AND t2.a < (SELECT MIN(t2.a) FROM t2 WHERE t1.a = t2.a);
EXPLAIN FORMAT=JSON 
select * from t1, t2 where t2.a = (SELECT MIN(t2.a) FROM t2 WHERE t1.a = t2.a);
