def combination_sum(nums, target):
    table = [0 for _ in range(target + 1)]
    table[0] = 1

    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0:
                table[i] += table[i - num]
    return table[target]
