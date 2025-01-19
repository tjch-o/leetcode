def max_amount(coins):
    m, n = len(coins), len(coins[0])
    table = [[[float("-inf") for _ in range(3)] for _ in range(n)] for _ in range(m)]

    for k in range(3):
        if coins[0][0] >= 0:
            table[0][0][k] = coins[0][0]
        elif k > 0:
            table[0][0][k] = 0
        else:
            table[0][0][k] = coins[0][0]

    for i in range(m):
        for j in range(n):
            for k in range(3):
                if i > 0:
                    table[i][j][k] = max(
                        table[i][j][k], table[i - 1][j][k] + coins[i][j]
                    )
                    if coins[i][j] < 0 and k > 0:
                        table[i][j][k] = max(table[i][j][k], table[i - 1][j][k - 1])

                if j > 0:
                    table[i][j][k] = max(
                        table[i][j][k], table[i][j - 1][k] + coins[i][j]
                    )
                    if coins[i][j] < 0 and k > 0:
                        table[i][j][k] = max(table[i][j][k], table[i][j - 1][k - 1])
    return max(table[m - 1][n - 1])
