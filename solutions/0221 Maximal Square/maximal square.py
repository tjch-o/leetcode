def maximal_square(matrix):
    m, n = len(matrix), len(matrix[0])
    table = [[0 for _ in range(n)] for _ in range(m)]
    max_side = 0

    for i in range(m):
        if matrix[i][0] == "1":
            table[i][0] = 1
            max_side = max(max_side, table[i][0])

    for j in range(n):
        if matrix[0][j] == "1":
            table[0][j] = 1
            max_side = max(max_side, table[0][j])

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == "1":
                # bounded by the left, up, and diagonal; cannot make square bigger than the smallest of them
                table[i][j] = (
                    min(table[i - 1][j - 1], table[i][j - 1], table[i - 1][j]) + 1
                )
                max_side = max(max_side, table[i][j])
    return max_side**2
