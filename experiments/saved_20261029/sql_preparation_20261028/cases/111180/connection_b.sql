-- MySQL report #111180; source: cmain, c532956, c532962, c532963
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SHOW VARIABLES LIKE 'long_query_time';
DELIMITER $$
CREATE PROCEDURE insert_test(IN max_num INT)
BEGIN
DECLARE i INT DEFAULT 0;
SET autocommit=0;
REPEAT
SET i=i+1;
INSERT INTO t1(id) VALUES(i);
UNTIL i=max_num END REPEAT;
COMMIT;
END$$
DELIMITER ;
CALL insert_test(100000);
SET autocommit=1;
UPDATE t1 SET name='test202305290';
SELECT * FROM mysql.slow_log;
SET GLOBAL max_binlog_size=1073741824;
UPDATE t1 SET name='test202305291';
SELECT * FROM mysql.slow_log;
