-- MySQL report #110003; source anchors: cmain, c529853, c529854
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t1(id INT NOT NULL AUTO_INCREMENT,val BIT(1) NOT NULL DEFAULT b'0',PRIMARY KEY(id,val)) ENGINE=InnoDB AUTO_INCREMENT=122 DEFAULT CHARSET=utf8mb4;
INSERT INTO t1(val) VALUES(0),(1);
INSERT INTO t1(val) SELECT val FROM t1;
INSERT INTO t1(val) SELECT val FROM t1;
SELECT id,HEX(val) FROM t1 WHERE id='123' AND val='1';
SELECT COUNT(*) AS before_count FROM t1;
DELETE FROM t1 WHERE id='123' AND val='1';
SELECT ROW_COUNT() AS deleted_count;
SELECT COUNT(*) AS after_count FROM t1;
