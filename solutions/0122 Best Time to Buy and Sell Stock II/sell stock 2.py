def max_profit(prices):
    profit = 0
    n = len(prices)

    for i in range(1, n):
        past, future = prices[i - 1], prices[i]
        if future > past:
            profit += (future - past)
    return profit
