def check_row(board, i, j):
    return board[i].count(board[i][j]) <= 1


def check_col(board, i, j):
    column = list(map(lambda x: x[j], board))
    return column.count(board[i][j]) <= 1


def check_grid(board, i, j):
    x = int(i / 3)
    y = int(j / 3)
    start_x, end_x = 3 * x, 3 * x + 3
    start_y, end_y = 3 * y, 3 * y + 3

    count = 0
    for a in range(start_x, end_x):
        for b in range(start_y, end_y):
            if board[a][b] == board[i][j]:
                count += 1
    return count <= 1


def is_valid_sudoku(board):
    n = 9

    for i in range(n):
        for j in range(n):
            if board[i][j] != ".":
                row_flag = check_row(board, i, j)
                if not row_flag:
                    return False

                col_flag = check_col(board, i, j)
                if not col_flag:
                    return False

                grid_flag = check_grid(board, i, j)
                if not grid_flag:
                    return False

    return True
