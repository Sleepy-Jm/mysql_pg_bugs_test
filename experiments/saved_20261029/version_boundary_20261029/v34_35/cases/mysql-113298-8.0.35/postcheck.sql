-- Read-only evidence after the unchanged source SQL, same session.
SELECT c1,1/1.5 AS computed_fraction,(1/1.5 IN(c1)) AS predicate_value FROM t0;
