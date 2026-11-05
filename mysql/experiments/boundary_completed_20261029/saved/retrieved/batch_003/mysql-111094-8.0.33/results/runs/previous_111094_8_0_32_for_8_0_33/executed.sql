USE `replay_6c07e3ff4de2ae6a4132bb25`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #111094; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE order_test (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	val varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
	PRIMARY KEY (id),
	KEY val(val)
);

INSERT INTO order_test (val) VALUES ('Wä'), ('E');

-- Incorrect order
SELECT *, val = 'wä', val = 'Wä', val = 'E'
FROM order_test
ORDER BY val = 'wä' DESC, val = 'Wä' DESC, val = 'E' DESC;

-- Expected order control
SELECT *, val = 'ka', val = 'Wä', val = 'E'
FROM order_test
ORDER BY val = 'ka' DESC, val = 'Wä' DESC, val = 'E' DESC;

-- Read-only postcheck appended after unchanged source SQL.
SELECT id,HEX(val) AS value_hex,COLLATION(val) AS coll FROM order_test ORDER BY id;
