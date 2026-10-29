USE `replay_e7e2508d28fc744e8540fdf2`;
SET time_zone="+00:00";
select UNIX_TIMESTAMP(case when true then (nullif(coalesce(nullif(TIMESTAMP('2090-9-4', '7:6:19'), null), null), null)) else (nullif(coalesce(nullif(TIMESTAMP('2090-9-4', '7:6:19'), null), null), null)) end) as c_6;
select UNIX_TIMESTAMP(nullif(coalesce(nullif(TIMESTAMP('2090-9-4', '7:6:19'), null), null), null)) as c_6;