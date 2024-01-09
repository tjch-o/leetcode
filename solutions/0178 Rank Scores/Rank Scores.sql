select score,
    /* use dense_rank() instead of rank() so that there are no holes in rank */
    dense_rank() over (
        order by score desc
    ) as "rank"
from Scores;