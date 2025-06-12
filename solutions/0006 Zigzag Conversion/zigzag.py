def convert(s, num_rows):
    if len(s) <= 1 or num_rows == 1:
        return s

    levels = [[] for _ in range(num_rows)]
    curr = 0
    going_down = True

    for c in s:
        levels[curr].append(c)

        if curr == num_rows - 1:
            going_down = False
        elif curr == 0:
            going_down = True

        if going_down == True:
            curr += 1
        else:
            curr -= 1

    res = []
    for level in levels:
        res.append("".join(level))
    return "".join(res)
