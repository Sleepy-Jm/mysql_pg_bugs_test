-- Report #111955; source anchors: cmain, c534968, c535625
-- Static preparation only; not executed. See case.json before any future isolated run.
PREPARE p0 FROM 'WITH x(x) AS (WITH y(y) AS (SELECT ?) SELECT 1 FROM y WHERE y.y) SELECT 1 FROM x JOIN x y';
