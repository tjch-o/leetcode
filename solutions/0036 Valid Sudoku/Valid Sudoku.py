def get_grid_number(i, j):
    x = i // 3
    y = j // 3
    return 3 * x + y


def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    squares = [set() for _ in range(9)]

    m, n = len(board), len(board[0])

    for i in range(m):
        for j in range(n):
            curr = board[i][j]
            grid_num = get_grid_number(i, j)

            if curr == ".":
                continue

            if curr in rows[i] or curr in columns[j] or curr in squares[grid_num]:
                return False

            rows[i].add(curr)
            columns[j].add(curr)
            squares[grid_num].add(curr)
    return True
