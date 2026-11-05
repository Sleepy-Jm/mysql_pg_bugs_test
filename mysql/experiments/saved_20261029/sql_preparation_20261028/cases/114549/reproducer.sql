-- Report #114549; source anchors: cmain, c542097, c544270
-- Static preparation only; not executed. See case.json before any future isolated run.
# Casting the DOUBLE 1.9 to signed INTEGER
select cast(cast(1.9 as double) as signed) ;

# Should return the same, using a DOUBLE column
create table k(a double);
insert into k values (1.9);
select * from  k;
show create table  k;
select cast(a as signed) from k;

# Should return the same, using a DOUBLE literal
select cast(1.9e0 as signed) from k;
# And here a DOUBLE column of a derived table
select cast(y as signed) from (select cast(1.9 as double)) as der(y);

# For reference, when using a DECIMAL input
select cast(1.9 as signed) from k;
