def transpose(matrix):
    m, n = len(matrix), len(matrix[0])
    res = []

    for j in range(n):
        res.append([])
        for i in range(m):
            res[j].append(matrix[i][j])
    return res
