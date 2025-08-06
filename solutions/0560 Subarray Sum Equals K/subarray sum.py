from collections import defaultdict

def subarray_sum(nums, k):
    prefix_sum = 0
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1
    count = 0

    for num in nums:
        prefix_sum += num
        count += prefix_sums.get(prefix_sum - k, 0)
        prefix_sums[prefix_sum] += 1
    return count
