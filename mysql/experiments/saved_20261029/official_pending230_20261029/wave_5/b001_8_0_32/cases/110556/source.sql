-- MySQL report #110556; source anchors: cmain, c556442
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE test1(md_id INT NOT NULL AUTO_INCREMENT,member_id INT NOT NULL,mid INT NOT NULL,expand_info JSON NOT NULL,PRIMARY KEY(md_id) USING BTREE,UNIQUE INDEX member_id(mid ASC,member_id ASC) USING BTREE) ENGINE=InnoDB;
INSERT INTO test1 VALUES(1,1,1,'[1]'),(2,2,1,'[]');
ALTER TABLE test1 ADD INDEX test_index(mid,(CAST(expand_info AS CHAR(20) ARRAY)));
SELECT COUNT(*) FROM test1 FORCE INDEX(PRIMARY) WHERE mid=1;
SELECT COUNT(*) FROM test1 FORCE INDEX(test_index) WHERE mid=1;
