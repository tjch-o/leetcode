SELECT
    s1.name
FROM
    SalesPerson s1
WHERE
    s1.name NOT IN (
        SELECT
            s.name
        FROM
            SalesPerson s
            JOIN Orders o ON s.sales_id = o.sales_id
            JOIN Company c ON o.com_id = c.com_id
        WHERE
            c.name = 'RED'
    );