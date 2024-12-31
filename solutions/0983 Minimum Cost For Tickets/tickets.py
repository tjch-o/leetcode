def min_cost_tickets(days, costs):
    travel_days = set(days)
    travel_costs = [float("inf") for _ in range(days[-1] + 1)]
    travel_costs[0] = 0

    for i in range(1, days[-1] + 1):
        if i not in travel_days:
            travel_costs[i] = travel_costs[i - 1]
        else:
            travel_costs[i] = min(
                travel_costs[i],
                travel_costs[max(0, i - 1)] + costs[0],
                travel_costs[max(0, i - 7)] + costs[1],
                travel_costs[max(0, i - 30)] + costs[2],
            )
    return travel_costs[days[-1]]
