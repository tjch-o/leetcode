SELECT
    email
FROM
    (
        SELECT
            email,
            count(*) AS count
        FROM
            Person
        GROUP BY
            email
    ) AS result
WHERE
    count > 1;