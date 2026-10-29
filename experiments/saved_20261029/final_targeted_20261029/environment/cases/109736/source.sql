-- MySQL report #109736; source anchors: cmain
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SELECT 1 FROM DUAL WHERE 2 < ANY(VALUES ROW(CAST(X'7C' AS BINARY)),ROW(CAST(X'31' AS BINARY)));

SELECT CAST(sum(c0) AS SIGNED) FROM (SELECT CAST(2 < ANY(VALUES ROW(CAST(X'7C' AS BINARY)),ROW(CAST(X'31' AS BINARY))) AS SIGNED) FROM DUAL) t0(c0);
