def array_pair_sum(nums):
    nums.sort()
    n = len(nums)
    max_sum = 0

    for i in range(n // 2):
        max_sum += nums[2 * i]
    return max_sum
