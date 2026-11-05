-- MySQL report #117852; source: cmain, c551648, c551747
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t1(c1 INT);
INSERT INTO t1 VALUES(1);
CREATE TABLE t2(c2 INT);
INSERT INTO t2 VALUES(2);
SELECT ref_2.c2 AS c_1,FIELD('I#',OCT(ref_2.c2))=0 AS w_1 FROM (t1 AS ref_1 LEFT OUTER JOIN t2 AS ref_2 ON (ref_1.c1=ref_2.c2));
SELECT ref_2.c2 AS c_1,FIELD('I#',OCT(ref_2.c2))=0 AS w_1 FROM (t1 AS ref_1 LEFT OUTER JOIN t2 AS ref_2 ON (ref_1.c1=ref_2.c2)) WHERE FIELD('I#',OCT(ref_2.c2))=0;
