SELECT * FROM XMLTABLE (ROW () passing null COLUMNS v1 TIMESTAMP, v2 int) AS f (v1, v2, v3);
