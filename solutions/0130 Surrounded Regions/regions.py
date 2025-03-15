def within_board(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])


def dfs(board, i, j):
    if not within_board(board, i, j) or board[i][j] != "O":
        return

    board[i][j] = "S"
    dfs(board, i - 1, j)
    dfs(board, i + 1, j)
    dfs(board, i, j - 1)
    dfs(board, i, j + 1)


def solve(board):
    m, n = len(board), len(board[0])

    for i in range(m):
        if board[i][0] == "O":
            dfs(board, i, 0)
        if board[i][n - 1] == "O":
            dfs(board, i, n - 1)

    for j in range(n):
        if board[0][j] == "O":
            dfs(board, 0, j)
        if board[m - 1][j] == "O":
            dfs(board, m - 1, j)

    for i in range(m):
        for j in range(n):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "S":
                board[i][j] = "O"
    return board
