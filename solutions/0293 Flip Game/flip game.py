def generate_possible_next_moves(s):
    n = len(s)
    res = []

    for i in range(n - 1):
        window = s[i : i + 2]

        if window == "++":
            move = s[:i] + "--" + s[i + 2 :]
            res.append(move)
    return res
