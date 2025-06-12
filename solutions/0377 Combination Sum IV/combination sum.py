def combination_sum(nums, target):
    table = [0 for _ in range(target + 1)]
    table[0] = 1

    for num in range(target + 1):
        for i in range(len(nums)):
            if num - nums[i] >= 0:
                table[num] += table[num - nums[i]]
    return table[target]
