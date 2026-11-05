-- MySQL report #109885; source anchors: cmain
-- Static preparation only. NOT EXECUTED. See case.json for conditions and oracle.
SET GLOBAL innodb_ft_aux_table = @saved_ft_aux;
SET SESSION innodb_ft_enable_stopword = @saved_ft_stop;
DROP TABLE IF EXISTS test;
