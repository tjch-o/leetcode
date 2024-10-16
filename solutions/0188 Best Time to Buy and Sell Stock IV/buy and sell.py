def max_profit(k, prices):
    n = len(prices)
    table = [[0 for _ in range(n)] for _ in range(k + 1)]

    for i in range(1, k + 1):
        profit = -prices[0]
        for j in range(1, n):
            table[i][j] = max(table[i][j - 1], profit + prices[j])
            profit = max(profit, table[i - 1][j] - prices[j])
    return table[k][n - 1]
