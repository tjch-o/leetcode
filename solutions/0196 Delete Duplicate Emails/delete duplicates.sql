DELETE FROM
    Person
WHERE
    id NOT IN (
        SELECT
            min(id)
        FROM
            Person
        GROUP BY
            email
    );