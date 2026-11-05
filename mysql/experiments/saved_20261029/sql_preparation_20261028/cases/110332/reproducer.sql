-- MySQL report #110332; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET SESSION time_zone='+00:00';
SET timestamp=1678406400;
SELECT (CASE WHEN 1 THEN TIME '0:0:0' WHEN 2 THEN TIMESTAMP '1970-1-1 0:0:0' END) < 1024;
SELECT (CASE WHEN 1 THEN TIME '0:0:0' WHEN 2 THEN TIMESTAMP '1970-1-1 0:0:0' END);
SELECT (CASE WHEN 1 THEN TIME '0:0:0' WHEN 2 THEN TIMESTAMP '1970-1-1 0:0:0' END) into @var;
select @var;
select @var < 1024;
show warnings;
