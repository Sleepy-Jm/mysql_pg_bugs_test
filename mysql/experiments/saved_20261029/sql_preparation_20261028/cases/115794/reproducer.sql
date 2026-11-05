-- MySQL report #115794; source: cmain, f33579, c546117
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
create table t1 (s1 int, id int);
create table t2 (id int, a int);
create table t0 (c0 int);

explain format=tree select /*+JOIN_ORDER(t2,t1)*/ t1.s1 from t1 INNER join t2 on (t2.id = t1.id) where t2.a=150007279  and t1.id in ( select c0 from  t0  GROUP BY c0 having count(1) > 0) ;
