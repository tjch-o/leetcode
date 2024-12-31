def max_coins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    table = [[0 for _ in range(n)] for _ in range(n)]

    for l in range(2, n):
        for i in range(0, n - l):
            j = i + l

            for k in range(i + 1, j):
                table[i][j] = max(
                    table[i][j], table[i][k] + nums[i] * nums[k] * nums[j] + table[k][j]
                )
    return table[0][n - 1]
