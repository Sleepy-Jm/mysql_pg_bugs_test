CREATE TABLE point_tbl (f1 point);
CREATE INDEX gpointind ON point_tbl USING gist (f1);
INSERT INTO point_tbl SELECT '(0,0)'::point FROM generate_series(1, 1000)
g;
