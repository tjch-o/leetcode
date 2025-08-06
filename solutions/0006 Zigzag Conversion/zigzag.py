def convert(s, num_rows):
    if num_rows == 1:
        return s

    rows = [[] for _ in range(num_rows)]
    ptr = 0
    i = 0

    while i < len(s):
        if ptr == 0:
            while i < len(s) and ptr < num_rows - 1:
                rows[ptr].append(s[i])
                ptr += 1
                i += 1

        if ptr == num_rows - 1:
            while i < len(s) and ptr > 0:
                rows[ptr].append(s[i])
                ptr -= 1
                i += 1

    res = []
    for row in rows:
        res.append("".join(row))
    return "".join(res)
