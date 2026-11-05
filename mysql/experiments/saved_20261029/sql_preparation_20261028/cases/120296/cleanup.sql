-- Report #120296; source anchors: cmain, c556697
-- Static preparation only; not executed. See case.json before any future isolated run.
DROP TABLE IF EXISTS t_main,t_ref;
SET SESSION sql_mode=@case_mode;
SET SESSION optimizer_switch=@case_optimizer;
