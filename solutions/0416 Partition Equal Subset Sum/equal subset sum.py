def can_partition(nums):
    s = sum(nums)

    if s % 2 != 0:
        return False

    target = s // 2
    table = [False for _ in range(target + 1)]
    table[0] = True

    for num in nums:
        for x in range(target, num - 1, -1):
            table[x] = table[x] or table[x - num]
    return table[target]
