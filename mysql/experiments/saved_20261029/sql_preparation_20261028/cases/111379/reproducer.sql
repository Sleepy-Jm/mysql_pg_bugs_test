-- MySQL report #111379; source anchors: cmain
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET SESSION sql_mode='NO_ENGINE_SUBSTITUTION';
create table v0(c1 INT);
SELECT * FROM v0 GROUP BY c1 HAVING c1 MEMBER OF ( EXISTS ( ( TABLE v0 LOCK IN SHARE MODE ) ORDER BY c1) ) ;

SELECT 1 AS server_alive;
