def can_jump(nums):
    n = len(nums)
    furthest = 0

    for i in range(n):
        if i > furthest:
            return False

        furthest = max(furthest, i + nums[i])
    return True
