SELECT
    score,
    /* use dense_rank() instead of rank() so that there are no holes in rank */
    dense_rank() over (
        ORDER BY
            score DESC
    ) AS "rank"
FROM
    Scores;