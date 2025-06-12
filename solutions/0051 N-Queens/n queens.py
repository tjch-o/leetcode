def is_safe(board, row, col):
    m, n = len(board), len(board[0])

    for i in range(row):
        if board[i][col] == "Q":
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False

        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False

        i -= 1
        j += 1
    return True


def backtrack(n, board, row, res):
    if row == n:
        res.append(["".join(row[:]) for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = "Q"
            backtrack(n, board, row + 1, res)
            board[row][col] = "."


def solve_n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    res = []
    backtrack(n, board, 0, res)
    return res
