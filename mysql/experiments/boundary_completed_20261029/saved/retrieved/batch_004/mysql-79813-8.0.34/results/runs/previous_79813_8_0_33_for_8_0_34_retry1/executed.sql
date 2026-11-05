USE `replay_8d3cff0012ef2a01d6c46386`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
CREATE DATABASE temp;
USE temp;
CREATE TABLE temp.user (user_id INT(11) UNSIGNED NOT NULL,department_id INT(11) UNSIGNED NOT NULL,user_name VARCHAR(32) DEFAULT NULL,is_active BOOL NOT NULL DEFAULT 1);
INSERT INTO temp.user (user_id,department_id,user_name,is_active) VALUES (1,1,'test user 1',TRUE),(2,1,'test user 2',FALSE),(3,2,'test user 3',TRUE);
SELECT JSON_OBJECT('can_edit',IF(user.is_active = "1",TRUE,FALSE),'is_true',TRUE,'is_false',FALSE) AS exception_comments FROM temp.user;

-- No extra postcheck required by frozen oracle.
