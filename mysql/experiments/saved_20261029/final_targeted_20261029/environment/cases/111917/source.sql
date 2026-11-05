-- MySQL report #111917; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET SESSION optimizer_switch='derived_condition_pushdown=on';
SELECT 1 FROM (SELECT b'1') y(y) WHERE (NULL || y.y) NOT LIKE 'a';
 -- 1 row
SET SESSION optimizer_switch='derived_condition_pushdown=off';
SELECT 1 FROM (SELECT b'1') y(y) WHERE (NULL || y.y) NOT LIKE 'a';
 -- empty
