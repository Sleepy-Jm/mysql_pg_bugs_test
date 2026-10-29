-- MySQL report #112212; source: cmain, c535747
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET SESSION optimizer_switch=@old_optimizer_switch;
DROP TABLE IF EXISTS type1,type2;
