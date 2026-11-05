USE `replay_2645a5f5e31311501bab8d71`;
SET time_zone="+00:00";
-- Source: bugs.mysql.com/bug.php?id=118625#cmain
-- Source SQL draft. Not executed or confirmed on target versions.
-- Run only in a newly created isolated test schema; no runner is invoked here.
CREATE TABLE t0(c0 BIGINT(33)  ) ;
CREATE INDEX i0 ON t0(c0);
INSERT INTO t0(c0) VALUES(0);
SELECT 1 AS ref0 FROM t0 WHERE NOT ((t0.c0) != (CAST(0.4 AS DOUBLE)));
