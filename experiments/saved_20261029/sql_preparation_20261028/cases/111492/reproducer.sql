-- MySQL report #111492; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SELECT 1 FROM (SELECT 1) y(y) WHERE 0 AND (SELECT 1 FROM (SELECT 1) x(x) GROUP BY y.y HAVING 1 = ALL(SELECT min(x.x)));
