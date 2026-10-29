-- Report #119945; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
DROP TABLE IF EXISTS t3;
SET SESSION sql_mode=@case_mode;
