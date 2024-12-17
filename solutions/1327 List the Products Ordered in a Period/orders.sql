SELECT
    product_name,
    unit
FROM
    (
        SELECT
            p.product_name AS product_name,
            sum(o.unit) AS unit
        FROM
            Products p
            JOIN Orders o ON p.product_id = o.product_id
        WHERE
            o.order_date > '2020-01-31'
            AND o.order_date < '2020-03-01'
        GROUP BY
            p.product_name
    )
WHERE
    unit >= 100;