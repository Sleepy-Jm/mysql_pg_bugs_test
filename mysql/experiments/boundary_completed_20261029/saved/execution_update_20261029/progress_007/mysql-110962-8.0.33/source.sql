-- MySQL report #110962; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
set sql_mode = "";




CREATE TABLE `s1` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `s_id` int(11) NOT NULL,
  `p_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1;

CREATE TABLE `t1` (
  `i` int(11) DEFAULT NULL
) ENGINE=InnoDB;

INSERT INTO s1 (p_id, s_id) VALUES (1, 1);
INSERT INTO s1 (p_id, s_id) VALUES (1, 1);
SELECT * FROM s1;

INSERT INTO t1 VALUES (1);
DELIMITER ;;
CREATE TRIGGER trg_s1 before INSERT ON `s1` FOR EACH ROW
IF 1 THEN
SET @sum = @sum + 1;
END IF ;;
DELIMITER ;
UPDATE t1 t JOIN s1 s ON s.s_id =t.i SET p_id = IF(1=0, null, p_id) WHERE t.i=1;
SHOW WARNINGS;
UPDATE t1 t JOIN s1 s ON s.s_id =t.i SET p_id = IF(1=1, null, p_id) WHERE t.i=1;
SHOW WARNINGS;
UPDATE t1 t JOIN s1 s ON s.s_id =t.i SET p_id = IF(1=1, 3, p_id) WHERE t.i=1;
SHOW WARNINGS;
select * from  t1 t JOIN s1 s ON s.s_id =t.i WHERE t.i=1;
SHOW WARNINGS;
UPDATE t1 t JOIN s1 s ON s.s_id =t.i SET p_id = IF(1=1, 3, p_id) WHERE t.i=1;
show warnings;
