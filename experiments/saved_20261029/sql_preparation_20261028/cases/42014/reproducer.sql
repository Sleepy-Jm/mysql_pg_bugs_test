-- MySQL report #42014; source anchors: cmain, c212179
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE foo(a DATE);
SELECT * FROM foo WHERE a=NAME_CONST('reportDate',_binary'2009-01-09' COLLATE 'binary');
SELECT 1 AS server_alive;
