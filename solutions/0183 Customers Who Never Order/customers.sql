SELECT
    name AS Customers
FROM
    Customers
    LEFT JOIN Orders ON Customers.id = Orders.customerid
WHERE
    Orders.customerid IS NULL;