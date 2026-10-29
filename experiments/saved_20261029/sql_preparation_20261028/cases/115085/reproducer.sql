-- Report #115085; source anchors: cmain, c543556, c543569, c544660, c544661
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t1(
  id INT UNSIGNED NOT NULL,
  fk_id INT UNSIGNED NOT NULL,
  data JSON DEFAULT NULL,
  name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id),
  KEY fk_id (fk_id),
  KEY functional_index (fk_id, (CAST(data AS CHAR(15) ARRAY)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


INSERT INTO t1 VALUES(123456,23,'["x","y","z"]','row with array value');
INSERT INTO t1 VALUES(99999,23,'[]','row with empty array');
EXPLAIN SELECT * FROM t1 USE INDEX(functional_index) WHERE fk_id=23 ORDER BY id DESC LIMIT 10;
SELECT * FROM t1 USE INDEX(functional_index) WHERE fk_id=23 ORDER BY id DESC LIMIT 10;
SELECT * FROM t1 USE INDEX(fk_id) WHERE fk_id=23 ORDER BY id DESC LIMIT 10;
