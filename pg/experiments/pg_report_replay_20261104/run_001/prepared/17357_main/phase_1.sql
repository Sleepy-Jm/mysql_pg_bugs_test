select
     *,
     row_number() over(
     partition by priority order by priority desc
) as n
from elements
;
