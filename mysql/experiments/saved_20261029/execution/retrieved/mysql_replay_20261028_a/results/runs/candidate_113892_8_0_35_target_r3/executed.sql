USE `replay_7f1a90db0d50e37ad3b341d0`;
SET time_zone="+00:00";
CREATE TABLE dupe_key(a INT,b INT,c INT,KEY a(a),KEY a_2(a,b)) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO dupe_key VALUES(1,2,3),(4,5,6),(7,8,9),(0,0,0);
ANALYZE TABLE dupe_key;
SELECT a FROM dupe_key FORCE INDEX(a) WHERE a=1 OR a<>1;
EXPLAIN SELECT a FROM dupe_key FORCE INDEX(a) WHERE a=1 OR a<>1;
EXPLAIN SELECT a FROM dupe_key USE INDEX(a) WHERE a=1 OR a<>1;
