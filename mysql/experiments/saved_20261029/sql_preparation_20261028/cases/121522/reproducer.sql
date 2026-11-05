-- MySQL report #121522; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET NAMES utf8mb4;
SELECT REGEXP_INSTR('abcabcabc','a+',1,4), REGEXP_INSTR('abcabcabc','a+',1,4294967298);
SELECT REGEXP_INSTR('abcabcabc','b+',4294967297);
SELECT REGEXP_REPLACE('aaabbccbbddaa','b+','x',1,4294967297);

-- expected: 0, 0 / ERROR 3686 / 'aaabbccbbddaa'
-- actual:   0, 4 / 2          / 'aaaxccbbddaa'
