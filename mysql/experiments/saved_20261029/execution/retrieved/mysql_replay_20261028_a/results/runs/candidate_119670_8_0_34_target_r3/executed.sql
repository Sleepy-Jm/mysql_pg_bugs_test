USE `replay_afd6156a787f995f12ebab8f`;
SET time_zone="+00:00";
-- Source: bugs.mysql.com/bug.php?id=119670#cmain
-- Source SQL draft. Not executed or confirmed on target versions.
-- Run only in a newly created isolated test schema; no runner is invoked here.
CREATE TABLE t2(c0 TINYINT(168));
CREATE INDEX i0 ON t2(c0 DESC);
REPLACE INTO t2(c0) VALUES(0);
SELECT c0 FROM t2 WHERE (NOT (((t2.c0) NOT IN (CAST(0.2914388740243027 AS DOUBLE))) || (t2.c0))); -- 0
SET @a = 0.2914388740243027;
PREPARE prepare_query FROM 'SELECT c0 FROM t2 WHERE (NOT (((t2.c0) NOT IN (CAST(? AS DOUBLE))) || (t2.c0)))';
EXECUTE prepare_query USING @a; -- empty result
DEALLOCATE PREPARE prepare_query;
