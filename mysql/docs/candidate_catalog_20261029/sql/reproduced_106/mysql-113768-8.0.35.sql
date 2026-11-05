-- MySQL report #113768; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
create table tb(a bigint);
insert into tb values(9223372036854775807),(-9223372036854775808);
SELECT 1 FROM tb A WHERE (A.a, A.a) NOT IN  ((CAST(9223372036854775807 AS REAL),CAST(110 AS SIGNED INTEGER)),(CAST(92 AS REAL),CAST(NULL AS SIGNED INTEGER)));
SELECT CAST(9223372036854775807 AS REAL);
SHOW WARNINGS;
