-- Read-only evidence after the unchanged source SQL, same session.
SELECT md_id,mid,CAST(expand_info AS CHAR) AS json_value FROM test1 FORCE INDEX(PRIMARY) ORDER BY md_id;
