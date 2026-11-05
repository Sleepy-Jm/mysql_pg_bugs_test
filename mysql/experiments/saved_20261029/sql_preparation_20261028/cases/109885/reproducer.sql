-- MySQL report #109885; source anchors: cmain
-- Static preparation only. NOT EXECUTED. See case.json for conditions and oracle.
SET @saved_ft_aux = @@GLOBAL.innodb_ft_aux_table;
SET @saved_ft_stop = @@SESSION.innodb_ft_enable_stopword;
CREATE TABLE test (id INT, name VARCHAR(255)) ENGINE=InnoDB;
SET innodb_ft_enable_stopword = 1;
ALTER TABLE test ADD FULLTEXT INDEX name_fti (name) WITH PARSER ngram;
SET GLOBAL innodb_ft_aux_table = CONCAT(DATABASE(), '/test');
SELECT value FROM information_schema.INNODB_FT_CONFIG WHERE `key`='use_stopword';
SET innodb_ft_enable_stopword = 0;
ALTER TABLE test DROP INDEX name_fti, ADD FULLTEXT INDEX name_fti(name) WITH PARSER ngram;
SELECT value FROM information_schema.INNODB_FT_CONFIG WHERE `key`='use_stopword';
ALTER TABLE test DROP INDEX name_fti;
ALTER TABLE test ADD FULLTEXT INDEX name_fti(name) WITH PARSER ngram;
SELECT value FROM information_schema.INNODB_FT_CONFIG WHERE `key`='use_stopword';
