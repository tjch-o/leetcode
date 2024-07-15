def can_partition(nums):
    total = sum(nums)

    if total % 2 != 0:
        return False
    
    target = total // 2
    table = [False for _ in range(target + 1)]
    table[0] = True

    for num in nums:
        # iterate downwards to avoid using the same number multiple times
        for i in range(target, num - 1, -1):
            table[i] = table[i] or table[i - num]
    return table[target]
