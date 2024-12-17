def is_toeplitz_matrix(matrix):
    def check_diagonal(i, j, m, n):
        while i >= 0 and j >= 0 and i < m - 1 and j < n - 1:
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
            i += 1
            j += 1
        return True

    m, n = len(matrix), len(matrix[0])

    for j in range(n):
        if check_diagonal(0, j, m, n) == False:
            return False

    for i in range(m):
        if check_diagonal(i, 0, m, n) == False:
            return False
    return True
