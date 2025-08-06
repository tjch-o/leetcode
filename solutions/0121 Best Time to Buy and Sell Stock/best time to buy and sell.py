def max_profit(prices):
    profit = 0
    curr_lowest = float("inf")

    for price in prices:
        curr_lowest = min(curr_lowest, price)
        profit = max(profit, price - curr_lowest)
    return profit
