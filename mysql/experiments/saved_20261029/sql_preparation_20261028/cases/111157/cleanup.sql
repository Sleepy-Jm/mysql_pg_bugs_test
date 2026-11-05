-- Report #111157; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
USE test_database;
DROP VIEW IF EXISTS test_view;
DROP FUNCTION IF EXISTS test_function;
DROP TABLE IF EXISTS test_table,test_table_new;
DROP DATABASE test_database;
DROP USER IF EXISTS 'applier'@'%';
DROP USER IF EXISTS 'definer'@'localhost';
