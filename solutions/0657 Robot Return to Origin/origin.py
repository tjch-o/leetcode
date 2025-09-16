def judge_circle(moves):
    move_map = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

    curr = [0, 0]

    for move in moves:
        x, y = move_map[move]
        curr[0] += x
        curr[1] += y
    return curr == [0, 0]
