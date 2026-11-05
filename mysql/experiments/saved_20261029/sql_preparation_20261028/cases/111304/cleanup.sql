-- Report #111304; source anchors: cmain, c533246
-- Static preparation only; not executed. See case.json before any future isolated run.
DELETE FROM query_rewrite.rewrite_rules WHERE id=@case_rule1;
CALL query_rewrite.flush_rewrite_rules();
DROP TABLE IF EXISTS test_jfg.t;
DROP DATABASE test_jfg;
