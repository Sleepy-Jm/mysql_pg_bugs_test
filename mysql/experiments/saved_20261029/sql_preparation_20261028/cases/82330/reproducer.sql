-- MySQL report #82330; source anchors: cmain, c542132
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET NAMES utf8mb4;
CREATE TABLE t1 (num SERIAL, val VARCHAR(32), FULLTEXT KEY fts_with_ngram(val) WITH PARSER ngram) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
INSERT INTO t1 VALUES(1,'泣かないでbaby');
SELECT @@ngram_token_size,@@innodb_ft_enable_stopword;
SELECT * FROM t1 WHERE MATCH(val) AGAINST('baby' IN BOOLEAN MODE);
SELECT * FROM information_schema.INNODB_FT_DEFAULT_STOPWORD;
