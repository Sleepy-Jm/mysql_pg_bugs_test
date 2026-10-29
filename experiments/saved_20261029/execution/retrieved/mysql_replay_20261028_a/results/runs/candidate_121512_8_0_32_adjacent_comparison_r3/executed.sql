USE `replay_1e33d65b0450f66e342653e6`;
SET time_zone="+00:00";
-- Source: bugs.mysql.com/bug.php?id=121512#cmain
-- Source SQL draft. Not executed or confirmed on target versions.
-- Run only in a newly created isolated test schema; no runner is invoked here.
SELECT ELT(4294967297,1,2,3) IS NULL, ELT(4294967297,1,2,3)+0,
       ELT(4294967297,1,2,3)|0, ELT(4294967297,1.1,1.2,1.3)+0, ELT(4,1,2,3)+0;


CREATE TABLE t17 (id INT PRIMARY KEY, n BIGINT, a INT, b INT, c INT);
INSERT INTO t17 VALUES (1, 4294967297, 10, 20, 30);
SELECT ELT(n,a,b,c) IS NULL, ELT(n,a,b,c)+0 FROM t17;
SELECT SUM(ELT(n,a,b,c)) FROM t17;

