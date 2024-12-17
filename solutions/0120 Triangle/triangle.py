def minimum_total(triangle):
    n = len(triangle)
    table = []

    for i in range(n):
        table.append([])
        for j in range(len(triangle[i])):
            table[i].append(float("inf"))

    table[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j < len(triangle[i - 1]):
                table[i][j] = min(table[i][j], table[i - 1][j] + triangle[i][j])

            if j > 0:
                table[i][j] = min(table[i][j], table[i - 1][j - 1] + triangle[i][j])
    return min(table[-1])
