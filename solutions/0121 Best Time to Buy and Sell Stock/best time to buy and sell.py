def max_profit(prices):
    if not prices:
        return 0

    min_price_so_far = prices[0]
    highest_profit = 0

    for i in range(len(prices)):
        min_price_so_far = min(min_price_so_far, prices[i])
        highest_profit = max(highest_profit, prices[i] - min_price_so_far)
    return highest_profit
