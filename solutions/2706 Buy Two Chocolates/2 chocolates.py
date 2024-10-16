import heapq

def buy_choco(prices, money):
    leftover = money
    k = 2
    heapq.heapify(prices)

    for _ in range(k):
        leftover -= heapq.heappop(prices)
    
    if leftover < 0:
        return money
    return leftover