create table elements (
     id serial primary key,
     priority smallint default 0
);
insert into elements (priority) values
    (1), (2), (3), (0), (0),
    (3), (2), (1), (0), (0),
    (0), (0), (0), (0), (0),
    (1), (1), (2), (2), (3)
;
