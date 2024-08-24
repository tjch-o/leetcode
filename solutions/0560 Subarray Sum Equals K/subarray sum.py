def subarray_sum(nums, k):
    count = 0
    curr_sum = 0
    n = len(nums)
    prefix_sum_counts = {0: 1}

    for i in range(n):
        curr = nums[i]
        curr_sum += curr
        complement = curr_sum - k

        if complement in prefix_sum_counts:
            count += prefix_sum_counts[complement]

        prefix_sum_counts[curr_sum] = prefix_sum_counts.get(curr_sum, 0) + 1
    return count
