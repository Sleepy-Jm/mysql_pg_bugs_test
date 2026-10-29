-- MySQL report #110550; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
VALUES ROW(1,1,1), ROW(5,5,5), ROW(4,4,4) ORDER BY column_1;
VALUES ROW(1,1,1), ROW(5,5,5), ROW(4,4,4) UNION VALUES ROW(0,0,0) ORDER BY column_1;
