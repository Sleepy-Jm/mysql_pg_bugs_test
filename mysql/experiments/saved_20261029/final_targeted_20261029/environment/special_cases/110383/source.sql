-- MySQL report #110383; source anchors: cmain, c554013
-- Static preparation only. NOT EXECUTED. See case.json for conditions and oracle.
SET @saved_file_per_table=@@GLOBAL.innodb_file_per_table;
SET GLOBAL innodb_file_per_table=0;
CREATE TABLE t(i INT NOT NULL,PRIMARY KEY(i)) ENGINE=InnoDB;
SHOW CREATE TABLE t;
ALTER TABLE t ADD j INT NOT NULL;
SHOW CREATE TABLE t;
