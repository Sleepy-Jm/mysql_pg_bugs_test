-- Report #111157; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE USER 'definer'@'localhost' IDENTIFIED WITH mysql_no_login;
GRANT SELECT, EXECUTE ON *.* TO 'definer'@'localhost';

CREATE USER 'applier'@'%';
GRANT SELECT, INSERT, CREATE, CREATE VIEW, ALTER, DROP ON *.* TO 'applier'@'%';

CREATE DATABASE test_database;
USE test_database;

CREATE TABLE test_table (
  id INT NOT NULL PRIMARY KEY
);

CREATE DEFINER='definer'@'localhost' FUNCTION test_function ()
RETURNS INT DETERMINISTIC
RETURN 1;

-- 'definer'@'localhost' has permission to execute test_function
CREATE DEFINER='definer'@'localhost' VIEW test_view AS
SELECT test_function() FROM test_table
;

-- Success
SHOW FIELDS FROM test_view;
