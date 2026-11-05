-- Report #119679; source anchors: cmain, c555563
-- Static preparation only; not executed. See case.json before any future isolated run.
SELECT DISTINCT SUM(t3.c9) AS col_1_3, t3.c1 AS col_1_4, t2.c9 AS c9 FROM t2 AS t2 LEFT JOIN t3 AS t3 ON (t3.c3 = t2.c1) WHERE (NOT REGEXP_LIKE(t3.c14, '[a-z]+@[a-z]+\.[a-z]{2,3}')) GROUP BY ROUND(t2.c1), t2.c9, t3.c5, t3.c1 HAVING (COUNT(DISTINCT t2.c3) <= 4) ;
SELECT DISTINCT -SUM(-t3.c9) AS col_1_3, t3.c1 AS col_1_4, t2.c9 AS c9 FROM t2 AS t2 LEFT JOIN t3 AS t3 ON (t3.c3 = t2.c1) WHERE (NOT REGEXP_LIKE(t3.c14, '[a-z]+@[a-z]+\.[a-z]{2,3}')) GROUP BY ROUND(t2.c1), t2.c9, t3.c5, t3.c1 HAVING (COUNT(DISTINCT t2.c3) <= 4) ;
