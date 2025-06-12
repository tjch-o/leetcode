def largest_divisible_subset(nums):
    if not nums:
        return []

    nums.sort()

    n = len(nums)
    table = [1 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    max_size = 0
    max_i = 0

    for j in range(n):
        for i in range(j):
            if nums[j] % nums[i] == 0 and table[i] + 1 > table[j]:
                table[j] = table[i] + 1
                parent[j] = i

            if table[j] > max_size:
                max_size = table[j]
                max_i = j

    res = []
    while max_i != -1:
        res.append(nums[max_i])
        max_i = parent[max_i]
    return res[::-1]
