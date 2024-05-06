SELECT
    e.employee_id
FROM
    Employees e
    LEFT JOIN Employees m ON e.manager_id = m.employee_id
WHERE
    e.salary < 30000
    AND m.employee_id IS NULL
    AND e.manager_id IS NOT NULL
ORDER BY
    employee_id;