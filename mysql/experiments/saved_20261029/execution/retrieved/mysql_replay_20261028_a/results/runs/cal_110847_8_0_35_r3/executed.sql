USE `replay_c14b84505432747e90cd555a`;
SET time_zone="+00:00";
CREATE DATABASE IF NOT EXISTS window_lag_bug;
USE window_lag_bug; 
DROP TABLE IF EXISTS `data_table`;
CREATE TABLE IF NOT EXISTS `data_table` (`uid` INT) ENGINE=InnoDB;
INSERT INTO `data_table` (`uid`) VALUES (100), (101);

PREPARE stmt1 FROM "SELECT (LAST_VALUE(a.`uid`) OVER `outer_window`) = a.`uid` as `result`
FROM 
	(	
		SELECT 
		LAG(`uid`) OVER `inner_window` AS `uid_lag`,
		`uid` AS `uid`
		FROM data_table
		WINDOW `inner_window` AS (ORDER BY `uid`)
	) AS a 
	WINDOW `outer_window` AS (ORDER BY a.`uid`)
";
EXECUTE stmt1;
EXECUTE stmt1;
SELECT VERSION();
DROP DATABASE window_lag_bug;