explain analyze select * from (
(select * from t1)
union all
(select * from t2 where true) -- Not just `true`, any condition here
)
order by t
limit 10;
