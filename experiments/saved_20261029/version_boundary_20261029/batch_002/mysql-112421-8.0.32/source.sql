CREATE TABLE test1 (id decimal(12,2));
INSERT INTO test1 VALUES (0.00),(NULL);
CREATE TABLE test2 (id decimal(12,2));
INSERT INTO test2 VALUES (0.00),(NULL);
SELECT * FROM test1;
SELECT * FROM test2;
SELECT * FROM test1 c LEFT JOIN test2 d ON c.id=d.id;
SELECT * FROM test1 c RIGHT JOIN test2 d ON c.id=d.id;
