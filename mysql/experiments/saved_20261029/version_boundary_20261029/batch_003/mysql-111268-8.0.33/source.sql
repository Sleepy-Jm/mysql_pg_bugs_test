-- MySQL report #111268; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t(id INT,c1 VARCHAR(10) COLLATE utf8mb4_bin) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
INSERT INTO t VALUES(1,'abc'),(2,'abc ');
SET character_set_connection=utf8mb3;
SELECT * FROM t WHERE c1='abc' AND c1='abc ';
SET character_set_connection=utf8mb4;
SELECT * FROM t WHERE c1='abc' AND c1='abc ';
