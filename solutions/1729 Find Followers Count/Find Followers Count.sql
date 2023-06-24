select user_id,
    followers_count
from (
        select user_id,
            count(*) as followers_count
        from Followers
        group by user_id
        order by user_id asc
    ) as result;