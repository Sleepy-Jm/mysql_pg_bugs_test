-- Read-only postchecks for report 114775; run in the same disposable schema/session.
SELECT * FROM main ORDER BY id; SELECT * FROM dummy ORDER BY id; SELECT * FROM seq ORDER BY id;
