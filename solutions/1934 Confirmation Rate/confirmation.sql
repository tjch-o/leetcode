SELECT
    s.user_id,
    round(
        CASE
            WHEN count(c.user_id) = 0 THEN 0
            ELSE sum(
                CASE
                    WHEN c.action = 'confirmed' THEN 1
                    ELSE 0
                END
            ) * 1.0 / count(c.user_id)
        END,
        2
    ) AS confirmation_rate
FROM
    Signups s
    LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY
    s.user_id;