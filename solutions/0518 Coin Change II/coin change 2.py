def change(amount, coins):
    n = len(coins)
    coins.sort()

    table = [0 for _ in range(amount + 1)]
    table[0] = 1

    for j in range(n):
        for i in range(1, amount + 1):
            if i - coins[j] >= 0:
                table[i] += table[i - coins[j]]
    return table[amount]
