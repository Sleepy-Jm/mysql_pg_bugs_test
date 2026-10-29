-- MySQL report #112615; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SELECT 1 FROM (SELECT 1) y(y) JOIN (SELECT 1) z(z) ON (SELECT 1 FROM (SELECT 1) x(x) HAVING 1 IN (SELECT min(x.x) FROM (SELECT 1) w(w))) WHERE 1 = 2;
