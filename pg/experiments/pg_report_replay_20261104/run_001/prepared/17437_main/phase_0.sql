explain analyze select aid from generate_series('2022-02-25
14:00:00'::timestamp, '2022-02-25 15:00:00'::timestamp, interval '5min')
f(t) join pgbench_accounts on extract(epoch from (now()-t))*1000 < aid;