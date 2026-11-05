-- MySQL report #111659; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
DROP TABLE IF EXISTS tbl_test_bug;
CREATE TABLE tbl_test_bug (
  id int UNSIGNED NOT NULL AUTO_INCREMENT,
  col_1 TINYINT UNSIGNED NOT NULL,
  col_2 TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY (id DESC),
  KEY col_1_idx (col_1),
  KEY col_2_idx (col_2)
) ENGINE=InnoDB;

-- Filling the table with random data (800 rows)
DELIMITER ;;
CREATE PROCEDURE gen_rows_test()
BEGIN
  DECLARE idx INT DEFAULT 800;
  WHILE idx > 0 DO
    INSERT INTO tbl_test_bug (col_1, col_2) VALUES (FLOOR(1 + (RAND() * 2)), FLOOR(1 + (RAND() * 10)));
    SET idx = idx - 1;
  END WHILE;
END;;
CALL gen_rows_test();;
DROP PROCEDURE IF EXISTS gen_rows_test;;
DELIMITER ;
SELECT * FROM tbl_test_bug ORDER BY id;
SELECT id FROM tbl_test_bug WHERE col_1=1 AND col_2=1;
SELECT id FROM tbl_test_bug WHERE col_1=1 AND col_2=1 LIMIT 1;
SELECT id FROM tbl_test_bug WHERE col_1=1 AND col_2=1 LIMIT 100;
ALTER TABLE tbl_test_bug DROP INDEX col_1_idx;
SELECT id FROM tbl_test_bug WHERE col_1=1 AND col_2=1;
