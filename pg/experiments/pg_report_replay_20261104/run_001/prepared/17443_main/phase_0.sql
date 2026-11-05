create temp table teste as
  select s::int as id1, s::int as id2, quote_ident('Nome ' || to_char(s,
'FM00000000'))::varchar(15) as nome
    from generate_series(1,10000000) x(s);


create index teste1 on teste (id1);
create index teste2 on teste using brin (id2);
