USE `replay_5ff3677579ddc5e8eb7939e4`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
CREATE DATABASE bug_db;
CREATE TABLE bug_db.bug_t(id INT NOT NULL AUTO_INCREMENT, col_str VARCHAR(255), col_int INT, PRIMARY KEY (id), INDEX col_str (col_str), INDEX col_int_ind (col_int));
INSERT INTO bug_db.bug_t(id,col_str,col_int) VALUES (1,"a",1),(2,"a",1),(3,"a",1);
SELECT @@SESSION.optimizer_switch;
SELECT id FROM bug_db.bug_t t1 WHERE EXISTS (SELECT 1 FROM bug_db.bug_t t2 WHERE t1.id > t2.id AND t1.col_str=t2.col_str AND t1.col_int=t2.col_int);
SET optimizer_switch='semijoin=off';
SELECT id FROM bug_db.bug_t t1 WHERE EXISTS (SELECT 1 FROM bug_db.bug_t t2 WHERE t1.id > t2.id AND t1.col_str=t2.col_str AND t1.col_int=t2.col_int);

-- No extra postcheck required by frozen oracle.
