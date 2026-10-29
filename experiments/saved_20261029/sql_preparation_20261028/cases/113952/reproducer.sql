-- MySQL report #113952; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE `test` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mt1` mediumtext,
  `mt2` mediumtext,
  PRIMARY KEY (`id`),
  KEY `idx_mt1` (`mt1`(191)),
  KEY `idx_mt2` (`mt2`(191))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

INSERT INTO
  `test` (
    `mt1`,
    `mt2`
  )
VALUES
  (
    repeat('a', 7500),
    repeat('b', 7500)
  );

UPDATE
  `test`
SET
  `mt1` = 'test',
  `mt2` = 'test'
WHERE
  `id` = 1;
TRUNCATE TABLE test;
INSERT INTO test(mt1,mt2) VALUES(REPEAT('a',7500),REPEAT('b',7500));
UPDATE test SET mt1='test' WHERE id=1;
UPDATE test SET mt2='test' WHERE id=1;
SELECT id,LENGTH(mt1),LENGTH(mt2) FROM test;
