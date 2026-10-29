CREATE TABLE t1(a int,b int,c varchar(100));
CREATE TABLE t2(a int,b int,c varchar(100));
EXPLAIN FORMAT=TREE SELECT * FROM t1 LEFT JOIN t2 ON t1.a=t2.a AND t2.a>0;
