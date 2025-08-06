def jump(nums):
    n = len(nums)
    count = 0
    furthest = 0
    furthest_from_curr_jump = 0

    for i in range(n - 1):
        furthest = max(furthest, i + nums[i])

        if i == furthest_from_curr_jump:
            furthest_from_curr_jump = furthest
            count += 1

            if furthest_from_curr_jump >= n - 1:
                break
    return count
