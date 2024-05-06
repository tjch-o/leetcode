SELECT
    v.customer_id,
    count(v.visit_id) AS count_no_trans
FROM
    visits v
WHERE
    v.visit_id NOT IN (
        SELECT
            t.visit_id
        FROM
            transactions t
    )
GROUP BY
    v.customer_id;