-- MySQL report #111261; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET global innodb_purge_stop_now=ON;

CREATE TABLE t1 (id BIGINT AUTO_INCREMENT PRIMARY KEY, s_id BIGINT, t_id VARCHAR(100), pad VARCHAR(512), INDEX sid_name(s_id, t_id));

DELIMITER //

CREATE PROCEDURE insert_numbers()
BEGIN
  DECLARE i INT DEFAULT 1;
  WHILE i <= 1000 DO
    INSERT INTO t1 (s_id, t_id, pad) VALUES (i/200, i, repeat('a', 512));
    SET i = i + 1;
  END WHILE;
END //
DELIMITER ;

CALL insert_numbers();
INSERT INTO t1 (s_id,t_id, pad) SELECT s_id,t_id, pad from t1;

DELETE from t1 where s_id=3;

select id from t1 where t_id='800';

select id from t1 force index(primary) where t_id='800';

SET global innodb_purge_stop_now=OFF;
