-- Read-only postchecks for report 111737; run in the same disposable schema/session.
SELECT @@sql_mode; SELECT COUNT(*) AS tab_exists FROM information_schema.tables WHERE table_schema=DATABASE() AND table_name='tab';
