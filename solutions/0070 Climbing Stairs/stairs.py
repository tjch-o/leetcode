def climbStairs(n):
    if n <= 2:
        return n

    table = [0 for _ in range(n + 1)]
    table[1] = 1
    table[2] = 2

    for i in range(3, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]
