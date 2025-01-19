def tribonacci(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    
    table = [0, 1, 1]
    
    for i in range(3, n + 1):
        table.append(table[i - 3] + table[i - 2] + table[i - 1])
    return table[n]