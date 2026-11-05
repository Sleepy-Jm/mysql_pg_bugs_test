-- Report #111474; source anchors: cmain, c533720, c533721, c536550
-- Static preparation only; not executed. See case.json before any future isolated run.
DROP TABLE IF EXISTS t0;
SET SESSION optimizer_switch=@case_optimizer;
