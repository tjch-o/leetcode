SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM
    employee e
    JOIN department d ON e.departmentId = d.id
WHERE
    e.salary IN (
        SELECT
            max(e1.salary)
        FROM
            employee e1
            /* where clause is needed in the case where salary matches the highest salary in another 
             department but not highest in own department */
        WHERE
            e.departmentId = e1.departmentId
        GROUP BY
            e1.departmentId
    );