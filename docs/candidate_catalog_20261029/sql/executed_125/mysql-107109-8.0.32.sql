-- MySQL report #107109; source anchors: cmain
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET SESSION optimizer_switch='semijoin=on';
SET NAMES utf8mb4;
SELECT /*+ SET_VAR(optimizer_switch='semijoin=off') */ @@optimizer_switch;
SHOW WARNINGS;
SET NAMES utf8mb3;
SELECT /*+ SET_VAR(optimizer_switch='semijoin=off') */ @@optimizer_switch;
SHOW WARNINGS;
