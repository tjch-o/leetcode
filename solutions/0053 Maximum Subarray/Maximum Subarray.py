def maxSubArray(nums):
    # implement Kadane's algorithm
    all_negative_flag = True
    current_subarray_sum = 0
    max_so_far = float("-inf")

    for num in nums:
        if num > 0:
            all_negative_flag = False

        current_subarray_sum += num
        if current_subarray_sum < 0:
            current_subarray_sum = 0

        max_so_far = max(max_so_far, current_subarray_sum)
    return max_so_far if not all_negative_flag else max(nums)
