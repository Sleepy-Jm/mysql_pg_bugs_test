-- MySQL report #110341; source anchors: cmain, c530604, c530617
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SELECT VERSION(); 

SET @p1 = '2023-02-03', @p2='2023-02-25';

CREATE TABLE t1 (
    created_at DATE
) ;

INSERT INTO t1 VALUES (@p1), (@p2);

SET @s = "select * from t1 where created_at in (?, ?)";

PREPARE stmt FROM @s;

EXECUTE stmt USING @p1, @p2; -- returns 2 rows as expected

SELECT FOUND_ROWS(); -- returns count of 2 as expected

DEALLOCATE PREPARE stmt;

CREATE TABLE t2 (
    created_at DATE
) 
PARTITION BY RANGE (DAYOFMONTH(created_at)) (
    PARTITION p1 VALUES LESS THAN (16), 
    PARTITION p2 VALUES LESS THAN MAXVALUE
);

INSERT INTO t2 VALUES (@p1), (@p2);

SET @s = "select * from t2 where created_at in (?, ?)";

PREPARE stmt FROM @s;

EXECUTE stmt USING @p1, @p2; -- returns 2 rows as expected

SELECT FOUND_ROWS(); -- returns count of 0, this is incorrect

DEALLOCATE PREPARE stmt;
