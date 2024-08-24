def can_jump(nums):
    if len(nums) <= 1:
        return True

    n = len(nums)
    goal = n - 1
    furthest = 0

    for i, curr in enumerate(nums):
        if i > furthest:
            return False
        
        # make furthest jump as possible
        furthest = max(furthest, i + curr)

        if furthest >= goal:
            return True
    return False
