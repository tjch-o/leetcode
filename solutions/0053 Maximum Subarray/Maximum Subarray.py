def max_subarray(nums):
    if not nums:
        return 0

    curr_max = nums[0]
    global_max = nums[0]

    for i in range(1, len(nums)):
        curr_max = max(curr_max + nums[i], nums[i])
        global_max = max(global_max, curr_max)
    return global_max
