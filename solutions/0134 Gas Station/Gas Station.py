def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    total = 0
    start = 0

    for i, g in enumerate(gas):
        net = g - cost[i]

        if total + net < 0:
            start = i + 1
            total = 0
        else:
            total += net
    return start
