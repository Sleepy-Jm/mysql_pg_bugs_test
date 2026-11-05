INSERT INTO async_pt SELECT i FROM generate_series(3000, 3100) i;
DELETE FROM async_pt;
UPDATE async_pt SET a = a;
