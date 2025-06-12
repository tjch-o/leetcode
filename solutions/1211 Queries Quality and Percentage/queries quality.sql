SELECT
    q.query_name,
    round(avg(q.rating * 1.0 / q.position), 2) AS quality,
    round(
        sum(
            CASE
                WHEN q.rating < 3 THEN 1
                ELSE 0
            END
        ) * 100.0 / count(*),
        2
    ) AS poor_query_percentage
FROM
    Queries q
GROUP BY
    q.query_name;