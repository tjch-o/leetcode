def inplace_reverse(mat):
    m, n = len(mat), len(mat[0])

    for i in range(m):
        for j in range(n // 2):
            mat[i][j], mat[i][n - j - 1] = mat[i][n - j - 1], mat[i][j]


def inplace_transpose(mat):
    n = len(mat)

    for i in range(n):
        for j in range(n):
            if i < j:
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]


def rotate(matrix):
    inplace_transpose(matrix)
    inplace_reverse(matrix)
    return matrix
