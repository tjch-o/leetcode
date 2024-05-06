def coin_change(coins, amount):
    table = [0 for _ in range(amount + 1)]

    for i in range(1, amount + 1):
        table[i] = float("Inf")
        for coin in coins:
            if i - coin >= 0:
                # minus the largest coin then +1 to the number of coins used
                table[i] = min(table[i], 1 + table[i - coin])
    return table[amount] if table[amount] != float("Inf") else -1
