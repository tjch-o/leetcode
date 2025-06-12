def fib(n):
    if n == 0 or n == 1:
        return n

    table = [0 for _ in range(n + 1)]
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]
