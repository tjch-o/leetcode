def get_money_amount(n):
    table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            min_cost = float("inf")

            for guess in range(i, j):
                c = guess + max(table[i][guess - 1], table[guess + 1][j])
                min_cost = min(min_cost, c)

            table[i][j] = min_cost
    return table[1][n]
