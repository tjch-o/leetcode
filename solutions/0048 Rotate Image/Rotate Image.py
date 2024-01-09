def rotate(matrix):
    n = len(matrix)

    # in place transpose
    for i in range(n):
        for j in range(n):
            if i < j:
                # only works for a n x n matrix
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # matrix = matrix[::-1] is not an inplace reverse
    for i in range(n):
        matrix[i].reverse()
    return matrix
