def max_subarray_sum_circular(nums):
    total = sum(nums)
    curr_max, curr_min = 0, 0
    max_sum, min_sum = float("-inf"), float("inf")

    for num in nums:
        curr_max = max(num, curr_max + num)
        max_sum = max(max_sum, curr_max)
        curr_min = min(num, curr_min + num)
        min_sum = min(min_sum, curr_min)

    if max_sum > 0:
        return max(max_sum, total - min_sum)
    return max_sum
