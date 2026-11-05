select * from
(values('null'::jsonb),('[]'::jsonb),('[null]'::jsonb),('[[]]'::jsonb)) as
t(j) order by j;
