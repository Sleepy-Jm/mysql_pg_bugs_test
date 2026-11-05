-- MySQL report #110562; source anchors: cmain, c531648
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
VALUES ROW(1,4),ROW(2,1),ROW(3,3) ORDER BY column_1;
SELECT * FROM (VALUES ROW(1,4),ROW(2,1),ROW(3,3)) AS t ORDER BY column_1;
