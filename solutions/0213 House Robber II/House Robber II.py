def rob(nums):
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])

    def rob_helper(nums, start, end):
        table = [0 for _ in range(end - start + 1)]
        table[0] = nums[start]
        table[1] = max(nums[start], nums[start + 1])

        for i in range(2, end - start + 1):
            table[i] = max(table[i - 1], table[i - 2] + nums[start + i])
        return table[-1]

    # take the first house but not the last house
    case_1 = rob_helper(nums, 0, len(nums) - 2)
    # take the last house but not the first house
    case_2 = rob_helper(nums, 1, len(nums) - 1)
    return max(case_1, case_2)
