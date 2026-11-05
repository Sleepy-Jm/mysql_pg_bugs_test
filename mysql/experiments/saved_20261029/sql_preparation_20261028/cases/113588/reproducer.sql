-- MySQL report #113588; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
-- prepare a table
CREATE TABLE `t` (
  `id` int,
  `k_id` int,
  `name` varchar(255)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;

-- insert some data
insert into t values(1, 2,repeat('a',100));
insert into t values(1, 2,repeat('a',100));
insert into t values(1, 3,repeat('a',100));


-- set group_concat_max_len = 1073741824 (1GB) to do a select
set group_concat_max_len = 1073741824;
SELECT LENGTH(GROUP_CONCAT( `name` ORDER BY `k_id` )) AS names FROM t GROUP BY id ORDER BY LENGTH(GROUP_CONCAT( `name` ORDER BY `k_id`));
-- set group_concat_max_len = 1073741824 * 2 (2GB) to do the same select
set group_concat_max_len = 1073741824 * 2;
SELECT LENGTH(GROUP_CONCAT( `name` ORDER BY `k_id` )) AS names FROM t GROUP BY id ORDER BY LENGTH(GROUP_CONCAT( `name` ORDER BY `k_id`));
-- set group_concat_max_len = 1610612832 (1.5GB) to do the same select
set group_concat_max_len = 1610612832 ;
SELECT LENGTH(GROUP_CONCAT( `name` ORDER BY `k_id` )) AS names FROM t GROUP BY id ORDER BY LENGTH(GROUP_CONCAT( `name` ORDER BY `k_id`));
