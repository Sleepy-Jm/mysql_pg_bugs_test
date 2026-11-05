-- Report #113097; source anchors: cmain, c538086, c553120, c553157
-- Static preparation only; not executed. See case.json before any future isolated run.
DROP TABLE IF EXISTS temp;
SET SESSION optimizer_switch=@case_optimizer;
