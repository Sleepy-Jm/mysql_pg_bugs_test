CREATE TABLE point_tbl(f1 point);
CREATE INDEX gpointind ON point_tbl USING gist(f1);
INSERT INTO point_tbl SELECT ('0,0') FROM generate_series(1, 185);
INSERT INTO point_tbl VALUES ('0,NaN');
