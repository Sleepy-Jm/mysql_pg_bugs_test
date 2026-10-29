-- MySQL report #110045; source: cmain, c554980
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SELECT STATEMENT_DIGEST_TEXT('SELECT -1 WHERE 1 = 1');
SELECT STATEMENT_DIGEST_TEXT('SELECT -1 WHERE 1 = -1');
