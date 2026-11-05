-- MySQL report #25767; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
DROP TABLE IF EXISTS `t1`;

CREATE TABLE `t1` (
`id` INT NOT NULL auto_increment PRIMARY KEY,
`lasttouched` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
`update_seq` INT NOT NULL default '0',
UNIQUE KEY `update_seq` (`update_seq`)
) ENGINE=MyISAM;

DELIMITER |
CREATE TRIGGER tr1 BEFORE UPDATE ON t1
FOR EACH ROW
BEGIN
IF OLD.lasttouched=NEW.lasttouched THEN
SET NEW.update_seq = (SELECT IFNULL(MAX(update_seq),0)+1 FROM t1);
END IF;
END|
DELIMITER ;


REPAIR TABLE t1;
SHOW WARNINGS;
REPAIR TABLE t1;
SHOW WARNINGS;
SELECT COUNT(*) FROM t1;
