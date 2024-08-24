SELECT
    Department,
    Employee,
    Salary
FROM
    (
        SELECT
            d.name AS Department,
            e.name AS Employee,
            e.salary AS Salary,
            dense_rank() over (
                PARTITION by e.departmentId
                ORDER BY
                    e.salary DESC
            ) AS rank
        FROM
            Employee e
            JOIN Department d ON e.departmentId = d.id
    )
WHERE
    rank <= 3;