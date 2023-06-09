def isValidSudoku(board):
    n = 9

    def check_row(i, j):
        return board[i].count(board[i][j]) <= 1
    
    def check_col(i, j):
        column = list(map(lambda x: x[j], board))
        return column.count(board[i][j]) <= 1
    
    def check_grid(i, j):
        x = int(i / 3)
        y = int(j / 3) 
        start_x, end_x = 3 * x, 3 * x + 3 
        start_y, end_y = 3 * y, 3 * y + 3
        
        count = 0
        for a in range(start_x, end_x):
            for b in range(start_y, end_y):
                if (board[a][b] == board[i][j]):
                    count += 1
        return count <= 1
    
    for i in range(n):
        for j in range(n):
           if (board[i][j] != "."):
              bool_row = check_row(i, j)
              if bool_row == False: return False

              bool_col = check_col(i, j)
              if bool_col == False: return False

              bool_grid = check_grid(i, j)
              if bool_grid == False: return False
              
    return True