CREATE TABLE test (id int unsigned auto_increment key,name varchar(50)) ENGINE=INNODB;
INSERT INTO test(id,name) VALUES(1,'姜志福');
SELECT * FROM (SELECT * FROM test UNION ALL SELECT * FROM test) a WHERE id=1 AND name='姜志福';
SHOW WARNINGS;
