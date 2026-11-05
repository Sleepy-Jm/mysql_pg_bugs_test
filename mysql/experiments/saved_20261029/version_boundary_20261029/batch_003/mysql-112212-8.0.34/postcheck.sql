-- Read-only postchecks for report 112212; run in the same disposable schema/session.
SELECT COUNT(*) AS type1_rows FROM type1; SELECT COUNT(*) AS type2_rows FROM type2; SELECT @@optimizer_switch;
