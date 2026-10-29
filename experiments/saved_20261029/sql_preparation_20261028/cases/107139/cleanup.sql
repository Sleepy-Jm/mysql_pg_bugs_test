-- Report #107139; source anchors: cmain, c521910, c521911, c521912, c545749, c545995
-- Static preparation only; not executed. See case.json before any future isolated run.
DROP TRIGGER IF EXISTS ins_sum;
DROP TABLE IF EXISTS account;
DROP USER IF EXISTS "testinguser"@"localhost";
DROP USER IF EXISTS "superuser"@"localhost";
