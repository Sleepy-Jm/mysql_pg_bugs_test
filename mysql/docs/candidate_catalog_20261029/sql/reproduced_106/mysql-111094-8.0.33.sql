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
