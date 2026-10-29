-- MySQL report #46189; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SELECT @@lower_case_table_names, @@collation_connection;
CREATE TABLE CLSync (id INT);
CREATE TABLE CLConf (id INT);
CREATE TABLE CLMT14 (id INT);
CREATE TABLE CLMstr (id INT);
SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema=DATABASE() AND table_name='CLSync';
DROP TABLE CLMT14; DROP TABLE CLSync; DROP TABLE CLMstr; DROP TABLE CLConf;
SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema=DATABASE() AND table_name='CLSync';
SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema=DATABASE() AND table_name='clsync';
