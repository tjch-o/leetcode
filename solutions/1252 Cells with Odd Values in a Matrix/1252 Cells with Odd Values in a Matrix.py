def col_increment(matrix, m, n, i, j):
    for col in range(n):
        matrix[i][col] += 1
    return matrix


def row_increment(matrix, m, n, i, j):
    for row in range(m):
        matrix[row][j] += 1
    return matrix


def odd_cells(m, n, indices):
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    for indice in indices:
        i, j = indice[0], indice[1]
        # order here does not matter
        matrix = col_increment(matrix, m, n, i, j)
        matrix = row_increment(matrix, m, n, i, j)

    count = 0
    for x in range(m):
        for y in range(n):
            if matrix[x][y] % 2 != 0:
                count += 1
    return count
