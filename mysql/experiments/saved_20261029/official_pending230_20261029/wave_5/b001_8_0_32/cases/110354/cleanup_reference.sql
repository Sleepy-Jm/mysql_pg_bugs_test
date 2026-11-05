-- Report #110354; source anchors: cmain, f32102
-- Static preparation only; not executed. See case.json before any future isolated run.
DROP TABLE IF EXISTS tt;
SET SESSION sql_mode=@case_old_mode;
SET SESSION time_zone=@case_old_tz;
