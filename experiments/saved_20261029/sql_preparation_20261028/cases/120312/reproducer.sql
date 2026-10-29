-- MySQL report #120312; source: cmain, c556733
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SELECT CURDATE(),@@SESSION.time_zone,@@SESSION.sql_mode;
CREATE TABLE t3 (
  pk SMALLINT NOT NULL,
  c5 TIME,
  category CHAR(2) NOT NULL,
  PRIMARY KEY (pk)
);

INSERT INTO t3 VALUES (1, '12:34:56', 'ok');

SELECT MIN(cuc28.c5) AS col_1
FROM t3 AS cuc28
WHERE category = 'ok'
UNION ALL
SELECT DATE_ADD(DATE('2025-03-14'), INTERVAL 0 SECOND) AS col_1;

CREATE VIEW V_cuc28_alt AS
SELECT MIN(cuc28.c5) AS col_1
FROM t3 AS cuc28
WHERE category = 'ok';

SELECT V_cuc28_alt.col_1 AS col_1
FROM V_cuc28_alt
UNION ALL
SELECT DATE_ADD(DATE('2025-03-14'), INTERVAL 0 SECOND) AS col_1;
