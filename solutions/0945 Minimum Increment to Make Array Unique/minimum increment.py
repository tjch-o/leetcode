def min_increment_for_unique(nums):
    nums.sort()
    count = 0

    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            increment = nums[i - 1] - nums[i] + 1
            nums[i] += increment
            count += increment
    return count
