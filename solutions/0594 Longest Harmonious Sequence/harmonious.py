from collections import Counter


def find_lhs(nums):
    counts = Counter(nums)
    max_l = 0

    for num in counts:
        if num + 1 in counts:
            max_l = max(max_l, counts[num] + counts[num + 1])
    return max_l
