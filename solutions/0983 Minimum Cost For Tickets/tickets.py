def min_cost_tickets(days, costs):
    last_day = days[-1]
    days_set = set(days)
    table = [float("inf") for _ in range(last_day + 1)]
    table[0] = 0

    for i in range(1, last_day + 1):
        if i not in days_set:
            table[i] = table[i - 1]
        else:
            table[i] = min(
                table[max(0, i - 1)] + costs[0],
                table[max(0, i - 7)] + costs[1],
                table[max(0, i - 30)] + costs[2],
            )
    return table[last_day]
