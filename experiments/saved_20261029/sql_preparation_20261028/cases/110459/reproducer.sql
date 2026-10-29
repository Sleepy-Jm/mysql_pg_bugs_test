-- MySQL report #110459; source anchors: cmain
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET SESSION sql_mode='ONLY_FULL_GROUP_BY';
CREATE TABLE t2(c0 INT);
CREATE TABLE t4(c0 INT);
SET SESSION optimizer_switch='derived_merge=on';
SELECT ty.c0 FROM t2 ty JOIN LATERAL (SELECT ty.c0 FROM t4) x(x) ON TRUE GROUP BY x.x;
SET SESSION optimizer_switch='derived_merge=off';
SELECT ty.c0 FROM t2 ty JOIN LATERAL (SELECT ty.c0 FROM t4) x(x) ON TRUE GROUP BY x.x;
