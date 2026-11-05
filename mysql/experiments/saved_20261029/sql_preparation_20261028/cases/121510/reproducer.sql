-- MySQL report #121510; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SELECT CONV('11', 2, 10) AS b2, CONV('11', 4294967298, 10) AS b2p32_2,
       CONV('11', -4294967294, 10) AS bm2p32_2, CONV('11', 37, 10) AS b37;

SELECT CONV('3', 10, 2) AS t2, CONV('3', 10, 4294967298) AS t2p32_2,
       CONV('3', 10, 37) AS t37;

SELECT CONV('-1', 10, 10) AS unsigned_out, CONV('-1', 10, -10) AS signed_out,
       CONV('-1', 10, 4294967286) AS t2p32_m10;

CREATE TABLE t015 (b BIGINT);
INSERT INTO t015 VALUES (16), (4294967312);
SELECT b, CONV('ff', b, 10) AS v FROM t015 ORDER BY b;
