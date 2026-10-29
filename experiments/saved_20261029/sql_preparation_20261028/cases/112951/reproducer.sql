-- Report #112951; source anchors: cmain, c537633
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t0 ( c0 INT ZEROFILL CHECK ( t0.ca3 < ( ( SELECT 1 ca0 FROM DUAL GROUP BY 1 HAVING 1 ORDER BY COUNT( 1 ) ) > RAND( ) / 100 ) ) ) SELECT true AS ca3;
