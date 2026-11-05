-- Report #112465; source anchors: cmain, c536324
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t0 ( c32 INT , c45 INT ) ;
INSERT INTO t0 VALUES ( -58 , -39 ) , ( 87 , -95 ) ;
ALTER TABLE t0 ADD COLUMN ( CONSTRAINT cc0 UNIQUE i0 ( c45 ) ) ;
