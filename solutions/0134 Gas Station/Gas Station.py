def canCompleteCircuit(gas, cost):
    total_gas = 0
    start = 0

    if sum(gas) < sum(cost):
        return -1

    for i in range(len(gas)):
        # gas reloaded at current station then used to travel to the next station
        total_gas += gas[i] - cost[i]

        if total_gas < 0:
            total_gas = 0
            # start at next station because any start point before i will not be able to complete circuit
            start = i + 1
    return start
