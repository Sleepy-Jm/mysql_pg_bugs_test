-- Read-only postchecks for report 112661; run in the same disposable schema/session.
SHOW CREATE TABLE table1; SHOW INDEX FROM table1; SHOW ENGINES; SELECT @@sql_mode;
