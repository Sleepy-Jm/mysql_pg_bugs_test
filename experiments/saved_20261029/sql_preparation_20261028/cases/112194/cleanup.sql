-- Report #112194; source anchors: cmain, c535766, c535821, c535822, c535885
-- Static preparation only; not executed. See case.json before any future isolated run.
DROP VIEW IF EXISTS vw_emp;
DROP TABLE IF EXISTS emp,dept;
SET SESSION optimizer_switch=@case_optimizer;
