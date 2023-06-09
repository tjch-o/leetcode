def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    table = [[0 for _ in range(n)] for _ in range(m)]
    
    if obstacleGrid[0][0] == 1:
        return 0
    table[0][0] = 1
    
    for i in range(1, m):
        if obstacleGrid[i][0] == 1:
            table[i][0] = 0
            break
        else:
            table[i][0] = 1
            
    for j in range(1, n):
        if obstacleGrid[0][j] == 1:
            table[0][j] = 0
            break
        else:
            table[0][j] = 1
                
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                table[i][j] = 0
            else:
                table[i][j] = table[i][j - 1] + table[i - 1][j]
    
    return table[m - 1][n - 1]