-- MySQL report #112037; source: cmain, c535234
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET SESSION optimizer_switch=@old_optimizer_switch;
DROP TABLE IF EXISTS t1;
