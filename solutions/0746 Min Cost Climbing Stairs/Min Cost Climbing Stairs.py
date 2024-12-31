def min_cost_climbing_stairs(cost):
    n = len(cost)
    table = [float("inf") for _ in range(n)]
    
    # can either start from step with index 0 or index 1
    table[0] = cost[0]
    table[1] = cost[1]
    
    for i in range(2, n):
        table[i] = min(table[i - 2] + cost[i], table[i - 1] + cost[i]) 
        
    # top of the floor is not cost table[n - 1] because we pay the cost then choose how many steps to jump
    # after paying cost of table[n - 1] can choose to jump 2 steps or pay table[n - 1] and jump 1 step
    return min(table[n - 1], table[n - 2])