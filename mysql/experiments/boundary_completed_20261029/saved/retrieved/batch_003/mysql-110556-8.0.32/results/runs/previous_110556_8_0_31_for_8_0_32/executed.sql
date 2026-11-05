USE `replay_0c1e096794b033b2365f1be1`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #110556; source anchors: cmain, c556442
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE test1(md_id INT NOT NULL AUTO_INCREMENT,member_id INT NOT NULL,mid INT NOT NULL,expand_info JSON NOT NULL,PRIMARY KEY(md_id) USING BTREE,UNIQUE INDEX member_id(mid ASC,member_id ASC) USING BTREE) ENGINE=InnoDB;
INSERT INTO test1 VALUES(1,1,1,'[1]'),(2,2,1,'[]');
ALTER TABLE test1 ADD INDEX test_index(mid,(CAST(expand_info AS CHAR(20) ARRAY)));
SELECT COUNT(*) FROM test1 FORCE INDEX(PRIMARY) WHERE mid=1;
SELECT COUNT(*) FROM test1 FORCE INDEX(test_index) WHERE mid=1;

-- Read-only evidence after the unchanged source SQL, same session.
SELECT md_id,mid,CAST(expand_info AS CHAR) AS json_value FROM test1 FORCE INDEX(PRIMARY) ORDER BY md_id;
