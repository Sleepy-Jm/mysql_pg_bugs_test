create table test(a float, b float);
insert into test select a, a % 10 from generate_series(1, 10000) a;


create function custom_max(float8, float8) returns float8 as
$$
  select case when $1 > $2 then $1 else $2 end
$$
language sql;


create aggregate custom_agg_max(float8)
(
    sfunc = custom_max,
    stype = float8,
    initcond = 0
);


set jit = on;
set jit_above_cost = 0;
set jit_dump_bitcode = on;
explain analyze select custom_agg_max(a)  from
test;
