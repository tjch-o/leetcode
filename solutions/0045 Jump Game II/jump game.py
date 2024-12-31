def jump(nums):
    n = len(nums)
    curr_max = 0
    next_max = 0
    count = 0

    for i in range(n - 1):
        next_max = max(next_max, i + nums[i])

        if i == curr_max:
            curr_max = next_max
            count += 1

        if i == n - 1:
            break
    return count
