-- MySQL report #104534; source anchors: cmain, c536875
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET NAMES utf8mb4;
create table UTF8MB4_test( text_col1 varchar(255), text_col2 varchar(255)) 
    default CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
create index text_col2_index on UTF8MB4_test(text_col2);

insert into UTF8MB4_test values('Some text','Some text');
insert into UTF8MB4_test values('Some other text','Some other text');
insert into UTF8MB4_test values('この𠝹𠱓𠱸この𠲖𠳏𠳕𠴕𠵼𠵿𠸎𠸏𠹷', 'この𠝹𠱓𠱸この𠲖𠳏𠳕𠴕𠵼𠵿𠸎𠸏𠹷');
insert into UTF8MB4_test values('この𠝹𠱓𠱸この𠲖', 'この𠝹𠱓𠱸この𠲖');

SELECT * FROM UTF8MB4_test WHERE text_col1 LIKE 'この𠝹%';
SELECT * FROM UTF8MB4_test WHERE text_col2 LIKE 'この𠝹%';
DROP INDEX text_col2_index ON UTF8MB4_test;
SELECT * FROM UTF8MB4_test WHERE text_col2 LIKE 'この𠝹%';
