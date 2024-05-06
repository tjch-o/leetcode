def find_cheapest_price(n, flights, src, dst, k):
    costs = [float("inf") for _ in range(n)]
    costs[src] = 0
    
    # implement Bellman Ford
    for _ in range(k + 1):
        temp = costs.copy()
        
        for source, dest, price in flights:
            if costs[source] == float("inf"):
                continue
        
            temp[dest] = min(temp[dest], costs[source] + price)
        
        costs = temp
    
    if costs[dst] == float("inf"):
        return -1
    return costs[dst]
