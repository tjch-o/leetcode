def max_subarray(nums):
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]

    max_ending_at_pos = nums[0]
    curr_max = nums[0]

    for i in range(1, len(nums)):
        # start from current position or add to previous subarray; not adding might miss out on a potential higher sum
        max_ending_at_pos = max(nums[i], max_ending_at_pos + nums[i])
        curr_max = max(curr_max, max_ending_at_pos)
    return curr_max
