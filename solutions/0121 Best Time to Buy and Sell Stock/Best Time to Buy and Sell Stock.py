def maxProfit(prices):
    # you dont necessarily have to sell on the last day you just sell on the day you got the maximum profit
    if len(prices) == 1:
        return 0
   
    x = len(prices) # how many days
    table = [0 for i in range(x)]
    table[0] = 0 # you can only sell the stock a different day into the future
    table[1] = max(0, prices[1] - prices[0]) # in the situation where price dropped from day 1 to day 2

    for i in range(2, x): 
        # you dont necessarily have to sell on the day right after
        table[i] = max(table[i], table[i-1] + prices[i] - prices[i-1]) # see if each day has a profit increase or loss
    # tabulated the max profit for each day then i take the highest instead of usually me taking the last guy
    return max(table) 