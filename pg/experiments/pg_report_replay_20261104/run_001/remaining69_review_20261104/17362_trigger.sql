set enable_seqscan=off;
\set VERBOSITY verbose
select id from bad_strings order by lower(value collate
"fi-FI-x-icu") asc, id;
