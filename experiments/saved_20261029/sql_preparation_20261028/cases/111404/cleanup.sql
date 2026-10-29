-- Report #111404; source anchors: cmain, c533545, c533546
-- Static preparation only; not executed. See case.json before any future isolated run.
DROP PROCEDURE IF EXISTS p3;
DROP TABLE IF EXISTS v0,v2;
SET SESSION sql_mode=@case_sql_mode;
