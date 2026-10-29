-- MySQL report #108155; source anchors: cmain, c524987, c541387
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET SESSION sql_mode='';
CREATE TABLE error_1048_test(c1 CHAR(1) NOT NULL,c2 CHAR(1) NOT NULL) ENGINE=InnoDB;
DELIMITER //
CREATE TRIGGER error_1048_test_BEFORE_INSERT BEFORE INSERT ON error_1048_test FOR EACH ROW BEGIN END//
DELIMITER ;
INSERT INTO error_1048_test(c1) VALUES('a');
SHOW WARNINGS;
SELECT * FROM error_1048_test;
UPDATE error_1048_test SET c2='b';
SHOW WARNINGS;
SELECT * FROM error_1048_test;
