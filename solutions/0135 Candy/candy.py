def candy(ratings):
    n = len(ratings)
    table = [1 for _ in range(n)]

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            table[i] = max(table[i], table[i - 1] + 1)

    for j in range(n - 2, -1, -1):
        if ratings[j] > ratings[j + 1]:
            table[j] = max(table[j], table[j + 1] + 1)
    return sum(table)
