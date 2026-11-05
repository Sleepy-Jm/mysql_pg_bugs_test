-- MySQL report #59154; source anchors: cmain, c356750
-- Static preparation only; NOT EXECUTED. Run only in a fresh isolated schema/instance.
SET @a:='aa',@a:=@a:=@a:=CEIL(@@GLOBAL.port);
SELECT @a;
