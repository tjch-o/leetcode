def max_profit_with_k_transactions(prices, k):
    n = len(prices)
    table = [[0 for _ in range(n)] for _ in range(k + 1)]

    for i in range(1, k + 1):
        max_diff = -prices[0]
        for j in range(1, n):
            table[i][j] = max(table[i][j - 1], prices[j] + max_diff)
            max_diff = max(max_diff, table[i - 1][j] - prices[j])
    return table[k][n - 1]


def max_profit(prices):
    return max_profit_with_k_transactions(prices, 2)
