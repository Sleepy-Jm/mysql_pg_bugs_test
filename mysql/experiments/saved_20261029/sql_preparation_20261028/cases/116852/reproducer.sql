-- Report #116852; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE mvi(id INT PRIMARY KEY,t INT,j JSON,INDEX index1(t,(CAST(j->'$' AS SIGNED ARRAY))),INDEX index2(t,(CAST(j->'$[*]' AS SIGNED ARRAY))));
INSERT INTO mvi VALUES(1,1,'[1,2,3]'),(2,1,'[]'),(3,1,NULL);
SELECT * FROM mvi FORCE INDEX(index1) WHERE t=1 ORDER BY id;
SELECT * FROM mvi FORCE INDEX(index2) WHERE t=1 ORDER BY id;
SELECT * FROM mvi IGNORE INDEX(index1,index2) WHERE t=1 ORDER BY id;
