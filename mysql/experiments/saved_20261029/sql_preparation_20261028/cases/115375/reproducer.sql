-- Report #115375; source anchors: cmain, c544463
-- Static preparation only; not executed. See case.json before any future isolated run.
USE test;
SET @case_old_aux=@@global.innodb_ft_aux_table,@case_old_stop=@@global.innodb_ft_enable_stopword;
CREATE TABLE testing(id INT UNSIGNED NOT NULL,name VARCHAR(300) BINARY NOT NULL,PRIMARY KEY(id,name),FULLTEXT KEY(name) WITH PARSER ngram);
INSERT INTO testing(id,name) VALUES(1,'Movie9/PlayMovie/12345');
SET GLOBAL innodb_ft_aux_table='test/testing';
SET GLOBAL innodb_ft_enable_stopword=OFF;
SELECT COUNT(*) FROM testing WHERE MATCH(name) AGAINST('Mov' IN BOOLEAN MODE);
SELECT * FROM INFORMATION_SCHEMA.INNODB_FT_INDEX_CACHE;
