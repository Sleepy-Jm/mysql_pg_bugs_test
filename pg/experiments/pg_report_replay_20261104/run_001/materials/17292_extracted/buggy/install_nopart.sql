\echo create schema
create schema bmk;

\echo tbl_attribute_types.sql
\i tbl_attribute_types.sql
\echo tbl_attributes.sql
\i tbl_attributes.sql
\echo tbl_currencies.sql
\i tbl_currencies.sql
\echo tbl_dates.sql
\i tbl_dates.sql
\echo tbl_sources.sql
\i tbl_sources.sql
\echo nopart/tbl_index_curr_analytics.sql
\i nopart/tbl_index_curr_analytics.sql
\echo nopart/tbl_index_main.sql
\i nopart/tbl_index_main.sql
\echo vw_ftrucf_index.sql
\i vw_ftrucf_index.sql
