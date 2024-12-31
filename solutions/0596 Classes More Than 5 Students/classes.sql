SELECT
    class
FROM
    (
        SELECT
            class,
            count(class) AS num
        FROM
            Courses
        GROUP BY
            class
    ) AS result
WHERE
    num >= 5;