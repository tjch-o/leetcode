def length_of_lis(nums):
    n = len(nums)
    table = [1 for _ in range(n)]

    for j in range(1, n):
        for i in range(j):
            if nums[j] > nums[i]:
                table[j] = max(table[j], table[i] + 1)
    return max(table)
