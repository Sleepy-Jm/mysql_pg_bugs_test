-- MySQL report #18140; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
DELIMITER //
CREATE TABLE t9 (s1 int)//

CREATE FUNCTION `partition_exists`(p_p_name varchar(64))
RETURNS int(11)
return (select count(*) from information_schema.partitions
where partition_name = p_p_name) //

CREATE PROCEDURE p9 ()
begin
declare continue handler for sqlexception insert into t9 values
(partiton_exists('p2'));
insert into t9 values (partition_exists('p1'));
end//

call p9()//
DELIMITER ;
SHOW WARNINGS;
SELECT * FROM t9;
SELECT 1 AS connection_alive;
