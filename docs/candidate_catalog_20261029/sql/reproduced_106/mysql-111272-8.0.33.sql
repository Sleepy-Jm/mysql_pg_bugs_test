-- MySQL report #111272; source anchors: cmain, c533174
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET NAMES utf8mb4;
-- case 1
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (c1 TINYTEXT, KEY i0 (c1(1)));
INSERT INTO t1 VALUES ("͕fB-'"),("^1o");
SELECT c1 FROM t1 WHERE c1 > ("?ykFo|1"); -- 1

-- case 2
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (c1 TINYTEXT);
INSERT INTO t1 VALUES ("͕fB-'"),("^1o");
SELECT c1 FROM t1 WHERE c1 > ("?ykFo|1"); -- 2
