def can_jump(nums):
    furthest = 0

    for i, num in enumerate(nums):
        if i > furthest:
            return False

        furthest = max(furthest, i + num)
    return True
