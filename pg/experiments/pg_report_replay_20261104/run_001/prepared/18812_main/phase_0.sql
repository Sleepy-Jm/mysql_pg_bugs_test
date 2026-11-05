CREATE TABLE t
(
    c varchar(10) NOT NULL
);


CREATE VIEW v AS
SELECT NULL::text AS c
FROM t;


CREATE RULE "insert" AS ON INSERT TO v
    WHERE FALSE
    DO INSTEAD
    INSERT INTO t (c)
    VALUES (new.c);


CREATE RULE "skip" AS ON INSERT TO v DO INSTEAD NOTHING;
