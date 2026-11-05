-- Read-only postchecks for report 111918; run in the same disposable schema/session.
SELECT c0 FROM t1 ORDER BY c0; SELECT HEX(CAST(X'0B36' AS CHAR));
