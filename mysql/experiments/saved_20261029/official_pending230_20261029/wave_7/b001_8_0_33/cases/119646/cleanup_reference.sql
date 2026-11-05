-- Report #119646; source anchors: cmain, c555476, c555720
-- Static preparation only; not executed. See case.json before any future isolated run.
DROP VIEW IF EXISTS v_test;
DROP TABLE IF EXISTS t_main,t_ref;
SET SESSION optimizer_switch=@case_optimizer;
