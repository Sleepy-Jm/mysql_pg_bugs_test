-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS doc_rows FROM t_doc;
SELECT COUNT(*) AS search_rows,COUNT(DISTINCT id) AS unique_ids FROM t_search_string;
