from collections import Counter


def flatten(board):
    m = len(board)
    result = []

    for i in range(m):
        for j in board[i]:
            result.append(j)
    return result


def check_wins(flattened_board, m=3):
    win_states = [m * ["X"], m * ["O"]]
    first_win = False
    second_win = False

    for i in range(0, len(flattened_board), m):
        row = flattened_board[i : i + m]

        if row == win_states[0]:
            first_win = True
        if row == win_states[1]:
            second_win = True

    for j in range(m):
        col = [flattened_board[i + j] for i in range(0, len(flattened_board), m)]

        if col == win_states[0]:
            first_win = True
        if col == win_states[1]:
            second_win = True

    left_diagonal = [flattened_board[i * (m + 1)] for i in range(m)]
    right_diagonal = [flattened_board[(i + 1) * (m - 1)] for i in range(m)]

    if left_diagonal == win_states[0] or right_diagonal == win_states[0]:
        first_win = True
    if left_diagonal == win_states[1] or right_diagonal == win_states[1]:
        second_win = True
    return (first_win, second_win)


def valid_tic_tac_toe(board):
    flattened_board = flatten(board)
    counts = Counter(flattened_board)

    if counts["X"] < counts["O"] or counts["X"] - counts["O"] > 1:
        return False

    first_win, second_win = check_wins(flattened_board)

    if first_win and second_win:
        return False
    elif first_win and counts["X"] - counts["O"] != 1:
        return False
    elif second_win and counts["X"] != counts["O"]:
        return False
    return True
