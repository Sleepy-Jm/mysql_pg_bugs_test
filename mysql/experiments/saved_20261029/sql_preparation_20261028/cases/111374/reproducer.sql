-- MySQL report #111374; source anchors: cmain
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET SESSION sql_mode='NO_ENGINE_SUBSTITUTION';
CREATE FUNCTION v0 ( ) RETURNS SERIAL READS SQL DATA DETERMINISTIC RETURN PARAM_MARKER ;

SELECT 1 AS server_alive;
