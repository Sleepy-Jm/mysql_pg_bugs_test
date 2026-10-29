-- Report #117051; source anchors: cmain, c549847
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE DATABASE x;
CREATE TABLE x.t(a INT);
INSERT INTO x.t VALUES(1),(2);
CREATE USER u2@'%' IDENTIFIED BY '123ABCabc';
GRANT INSERT,DELETE,UPDATE ON x.* TO u2@'%';
GRANT SELECT ON x.t TO u2@'%';
