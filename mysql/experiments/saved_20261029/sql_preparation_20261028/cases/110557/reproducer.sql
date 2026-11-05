-- MySQL report #110557; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
show variables like 'innodb_disable_sort_file_cache';
CREATE TABLE test (
`id` int(0) NOT NULL AUTO_INCREMENT,
`name` varchar(255),
`img` varchar(255),
PRIMARY KEY (`id`) USING BTREE,
FULLTEXT INDEX `testfulltext`(`img`) WITH PARSER `ngram`
) ENGINE = InnoDB;
INSERT INTO test (name) VALUE ("hey");
ALTER TABLE test ADD FULLTEXT INDEX IDX_NAME(name) WITH PARSER ngram;
