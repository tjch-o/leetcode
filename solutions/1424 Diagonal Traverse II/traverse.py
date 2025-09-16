from collections import defaultdict


def find_diagonal_order(nums):
    m = len(nums)
    res = []
    hashmap = defaultdict(list)

    for i in range(m):
        for j in range(len(nums[i])):
            hashmap[i + j].append((i, j))

    sorted_keys = sorted(hashmap.keys())
    for key in sorted_keys:
        indices = sorted(hashmap[key], reverse=True)
        values = [nums[i][j] for i, j in indices]
        res.extend(values)
    return res
