-- MySQL report #119572; source: cmain, c555362, c555363, c557880
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET SESSION optimizer_trace=@old_optimizer_trace;
DROP TABLE IF EXISTS t1;
