-- Read-only postchecks for report 115380; run in the same disposable schema/session.
SELECT id,cc,m,t FROM t15 ORDER BY id; SELECT * FROM t2 ORDER BY id;
