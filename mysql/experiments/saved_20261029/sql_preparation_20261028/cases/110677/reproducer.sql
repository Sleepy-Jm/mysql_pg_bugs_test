-- MySQL report #110677; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
PREPARE p0 FROM 'SELECT format_bytes(?)';
SET @a0 = NULL;
EXECUTE p0 USING @a0;
DEALLOCATE PREPARE p0;
