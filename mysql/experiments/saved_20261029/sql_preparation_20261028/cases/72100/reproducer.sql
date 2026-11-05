-- MySQL report #72100; source anchors: cmain, c418803
-- Static preparation only; NOT EXECUTED. Run only in a fresh isolated schema/instance.
create table t (id serial, d decimal(65,30));
insert into t values (),(),(),(),(),(),(),(),();
insert into t values (),(),(),(),(),(),(),(),();
insert into t values (),(),(),(),(),(),(),(),();
update t set d = concat('1e-', id);
select d, d mod 1 from t;
SELECT COUNT(*) AS mismatches FROM t WHERE NOT (d <=> MOD(d,1));
