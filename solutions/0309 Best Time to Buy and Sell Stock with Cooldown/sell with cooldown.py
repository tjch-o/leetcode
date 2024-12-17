def max_profit(prices):
    n = len(prices)
    table = [[0 for _ in range(2)] for _ in range(n)]

    table[0][0] = 0
    table[0][1] = -prices[0]

    for i in range(1, n):
        table[i][0] = max(table[i - 1][0], table[i - 1][1] + prices[i])

        if i > 1:
            table[i][1] = max(table[i - 1][1], table[i - 2][0] - prices[i])
        else:
            table[i][1] = max(table[i - 1][1], -prices[i])
    return table[n - 1][0]
