-- Read-only evidence after the unchanged source SQL, same session.
SELECT k,HEX(k) AS hex_k FROM vals0;
SELECT k,HEX(k) AS hex_k FROM vals1;
