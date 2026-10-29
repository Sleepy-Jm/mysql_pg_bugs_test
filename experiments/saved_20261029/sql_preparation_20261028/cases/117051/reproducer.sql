-- Report #117051; source anchors: cmain, c549847
-- Static preparation only; not executed. See case.json before any future isolated run.
USE x;
SELECT CURRENT_USER(),USER();
SHOW GRANTS;
DELETE FROM t WHERE a=1;
SELECT * FROM t WHERE a=1;
