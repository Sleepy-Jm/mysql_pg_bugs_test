-- MySQL report #120297; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
-- 1. create table
  
  
  DROP TABLE IF EXISTS t3;
  CREATE TABLE t3 (a INT);
  INSERT INTO t3 VALUES (1),(2),(3),(1),(2);

  -- 2. core
  SET SESSION debug='+d,ast';
  SELECT COUNT(*) FROM t3 UNION SELECT COUNT(*) FROM t3;
