-- MySQL report #114060; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET time_zone='+00:00';
SET timestamp=1706745600;
SELECT *
FROM (
	SELECT DATE(`dt2`) AS `dt3` 
	FROM (
		SELECT * FROM (
			SELECT 1 AS `c1`, 1 AS `c2` 
		) t1
		LEFT JOIN (
			SELECT `f1`, `f2`, MAX(`dt`) AS `dt2` 
			FROM (
				SELECT 1 AS `f1`, 1 AS `f2`, NOW() AS `dt`
			) tmp_23 
			GROUP BY `f1`, `f2`
		) tmp_24 
		ON ((`c1` <=> `f1`) AND (`c2` <=> `f2`))
	) tmp_25
) tmp_26
WHERE `dt3` < '2024-02-05';
