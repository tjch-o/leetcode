def maxProfit(prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        # cannot just find the min of the prices because the min could be after the max
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
