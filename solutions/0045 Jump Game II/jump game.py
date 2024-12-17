def jump(nums):
    n = len(nums)
    count = 0
    furthest = 0
    ptr = 0

    for i in range(len(nums)):
        if i >= n - 1:
            break

        furthest = max(furthest, i + nums[i])

        if i == ptr:
            ptr = furthest
            count += 1
    return count
