-- Report #112910; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
SELECT * FROM ( VALUES ROW ( 'a', 0 ) ) t0 WHERE t0.column_1 = ( CAST( 1/16 AS DOUBLE PRECISION ) ) ; -- expected: empty, actually: empty

SELECT * FROM ( VALUES ROW ( 'a', 0 ), ROW ( 'b', 1 ) ) t0 WHERE t0.column_1 = ( CAST( 1/16 AS DOUBLE PRECISION ) ) ; -- expected: empty, actually: 1 row
