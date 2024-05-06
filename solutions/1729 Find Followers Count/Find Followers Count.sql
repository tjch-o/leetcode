SELECT
    user_id,
    followers_count
FROM
    (
        SELECT
            user_id,
            count(*) AS followers_count
        FROM
            Followers
        GROUP BY
            user_id
        ORDER BY
            user_id ASC
    ) AS result;