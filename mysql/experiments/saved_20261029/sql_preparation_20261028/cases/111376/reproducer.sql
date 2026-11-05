-- MySQL report #111376; source anchors: cmain
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET SESSION sql_mode='NO_ENGINE_SUBSTITUTION';
create table v0(c1 INT);
CREATE TABLE v3 ( c4 NATIONAL CHAR ) PARTITION BY HASH ( c1 ) AS TABLE v0 ;
CREATE TABLE v5 ( INDEX ( ( c4 SOUNDS LIKE TRUE ) ) ) AS TABLE v3 ;

SELECT 1 AS server_alive;
