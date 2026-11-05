USE `replay_343bdd78cc77b3d78942412d`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113649; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
DELIMITER //
CREATE PROCEDURE demo(out a varchar(1024))
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE cur1 CURSOR FOR SELECT format(-1.7976931348623157E+307,256);
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  OPEN cur1;
  read_loop: LOOP
    FETCH cur1 INTO a;
    IF done THEN
      LEAVE read_loop;
    END IF;
  END LOOP;
  CLOSE cur1;
END//
DELIMITER ;
CALL demo(@hello);
SHOW WARNINGS;
SELECT @hello,LENGTH(@hello),FORMAT(-1.7976931348623157E+307,256),LENGTH(FORMAT(-1.7976931348623157E+307,256)),CAST(@hello AS BINARY)=CAST(FORMAT(-1.7976931348623157E+307,256) AS BINARY) AS same_bytes;

-- No additional postcheck required by the reviewed oracle.
