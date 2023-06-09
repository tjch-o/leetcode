def isToeplitzMatrix(matrix):
    def checkDiagonal(i, j, m, n):
        while (i >=0 and j >= 0 and i < m - 1 and j < n - 1):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
            i += 1
            j += 1
        return True

    m = len(matrix)
    n = len(matrix[0])
    
    # we loop through the first row to check diagonals 
    for j in range(n):
        if checkDiagonal(0, j, m, n) == False:
            return False
        
    # we loop through the first column
    for i in range(m):
        if checkDiagonal(i, 0, m, n) == False:
            return False
            
    return True