def coin_change(coins, amount):
    if amount < 0:
        return -1

    table = [float("inf")] * (amount + 1)
    table[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                table[i] = min(table[i], table[i - coin] + 1)

    if table[amount] == float("inf"):
        return -1
    return table[amount]
