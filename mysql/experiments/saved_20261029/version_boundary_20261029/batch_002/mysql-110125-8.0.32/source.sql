-- MySQL report #110125; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE IF NOT EXISTS t0(c0 DOUBLE ZEROFILL) ;
CREATE INDEX i0 ON t0(c0 DESC);
INSERT DELAYED IGNORE INTO t0(c0) VALUES(0);

SELECT c0 FROM t0 WHERE (IFNULL(-1123870957, '')) IN (t0.c0); -- 0
