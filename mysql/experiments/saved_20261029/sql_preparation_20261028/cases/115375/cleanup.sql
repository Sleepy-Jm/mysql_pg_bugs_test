-- Report #115375; source anchors: cmain, c544463
-- Static preparation only; not executed. See case.json before any future isolated run.
SET GLOBAL innodb_ft_aux_table=@case_old_aux;
SET GLOBAL innodb_ft_enable_stopword=@case_old_stop;
DROP TABLE IF EXISTS test.testing;
