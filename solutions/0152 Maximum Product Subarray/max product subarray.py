def max_product(nums):
    if not nums:
        return 0

    local_max = nums[0]
    local_min = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        curr = nums[i]

        if curr < 0:
            # update both at the same time; cannot use local_min to update local_max first and vice versa when all values are negative
            local_max, local_min = local_min, local_max

        # add to subarray or start over with current element
        local_max = max(curr, local_max * curr)
        local_min = min(curr, local_min * curr)
        result = max(result, local_max)
    return result
