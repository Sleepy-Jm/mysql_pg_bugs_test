-- Run after the unmodified source script, in the same owned schema; read-only evidence only.
SELECT USER1_ID,USER2_ID FROM FRIENDSHIP;
SELECT USER_ID,PAGE_ID FROM LIKES;
SELECT PAGE_ID FROM LIKES WHERE USER_ID=1;
