-- Report #112516; source anchors: cmain, c536410
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TEMPORARY TABLE t0 ( c50 TEXT , INDEX i0 ( ( IF ( 110 , -27 , 39 ) IS NOT UNKNOWN ) DESC , ( t0 . c41 = OCT ( t0 . c50 ) LIKE IF ( t0 . c41 , t0 . c50 , CONVERT ( c41 , NCHAR ) ) ) ASC ) , c41 DOUBLE DEFAULT ( 25 ) , INDEX i1 ( ( c41 + 3 ) ) ) REPLACE AS SELECT 116 AS c16 GROUP BY 1 ;
