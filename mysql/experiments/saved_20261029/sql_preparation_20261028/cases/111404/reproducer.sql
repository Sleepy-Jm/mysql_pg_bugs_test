-- Report #111404; source anchors: cmain, c533545, c533546
-- Static preparation only; not executed. See case.json before any future isolated run.
SET @case_sql_mode=@@session.sql_mode;
SET SESSION sql_mode='NO_ENGINE_SUBSTITUTION';
CREATE TABLE v0(c1 INT);
CREATE PROCEDURE p3() CREATE TABLE v2(CHECK((SELECT 'abc'))) AS TABLE v0;
CALL p3;
SELECT 1 AS server_alive;
