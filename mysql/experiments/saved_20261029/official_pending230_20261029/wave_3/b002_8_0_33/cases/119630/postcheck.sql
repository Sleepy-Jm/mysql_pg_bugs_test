-- Read-only postchecks for report 119630; run in the same disposable schema/session.
SELECT * FROM t_bug_mat1 ORDER BY id; SELECT * FROM t_bug_mat2 ORDER BY id; SELECT @@optimizer_switch;
