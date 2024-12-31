from collections import defaultdict


def find_max_length(nums):
    n = len(nums)

    for i in range(n):
        if nums[i] == 0:
            nums[i] = -1

    prefix_sums = {}
    curr = 0
    max_l = 0

    for i, num in enumerate(nums):
        curr += num

        if curr == 0:
            max_l = max(max_l, i + 1)

        if curr in prefix_sums:
            max_l = max(max_l, i - prefix_sums[curr])
        else:
            prefix_sums[curr] = i
    return max_l
