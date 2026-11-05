-- Report #111157; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
USE test_database;

CREATE TABLE test_table_new LIKE test_table;
DROP TABLE test_table;
RENAME TABLE test_table_new TO test_table;

-- Error. Even though 'definer'@'localhost' has permission to execute test_function, 'applier'@'%' does not, and this seems to affect data dictionary generation.
SHOW FIELDS FROM test_view;
