def max_subarray(nums):
    # implement Kadane's algorithm
    all_negative = True
    current_subarr_sum = 0
    max_so_far = float("-inf")

    for num in nums:
        if num > 0:
            all_negative = False

        current_subarr_sum += num
        if current_subarr_sum < 0:
            current_subarr_sum = 0

        max_so_far = max(max_so_far, current_subarr_sum)
    return max_so_far if not all_negative else max(nums)
