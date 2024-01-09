def setZeroes(matrix):
    def setRowToZeroes(i, n):
        for y in range(n):
            matrix[i][y] = 0
    
    def setColumnToZeroes(j, m):
        for x in range(m):
            matrix[x][j] = 0
    
    ref_matrix = [row[:] for row in matrix]
    m = len(matrix)
    n = len(matrix[0])
    
    for i in range(m):
        for j in range(n):
            if ref_matrix[i][j] == 0:
                setRowToZeroes(i, n)
                setColumnToZeroes(j, m)
    return matrix