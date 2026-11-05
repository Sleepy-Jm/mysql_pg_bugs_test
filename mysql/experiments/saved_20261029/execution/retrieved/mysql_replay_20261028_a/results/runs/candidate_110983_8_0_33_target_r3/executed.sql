USE `replay_bfb5ef0bf0607e945f8fd1f1`;
SET time_zone="+00:00";
CREATE TABLE table1(id INT);
INSERT INTO table1 VALUES(1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12);
DELIMITER $$
CREATE PROCEDURE test2()
BEGIN
SELECT count(*) over(rows between 5 preceding and 5 following) AS A,
count(*) over(rows between 5 preceding and 5 following)+1 AS Aplus,
count(*) over() AS B, count(*) over()+1 AS Bplus FROM table1;
END$$
DELIMITER ;
CALL test2();
CALL test2();
