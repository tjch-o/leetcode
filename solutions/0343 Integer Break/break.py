def integer_break(n):
    table = [0 for _ in range(n + 1)]
    table[1] = 1

    for i in range(2, n + 1):
        for j in range(1, i):
            table[i] = max(table[i], max(table[i - j], i - j) * j)
    return table[n]
