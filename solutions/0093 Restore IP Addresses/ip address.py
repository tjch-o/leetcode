def backtrack(s, start, parts, res):
    if len(parts) == 4 and start == len(s):
        res.append(".".join(parts))
        return

    for i in range(1, 4):
        if start + i > len(s):
            continue

        segment = s[start : start + i]

        if len(segment) > 1 and segment[0] == "0":
            continue

        if int(segment) > 255:
            continue

        parts.append(segment)
        backtrack(s, start + i, parts, res)
        parts.pop()


def restore_ip_addresses(s):
    res = []
    backtrack(s, 0, [], res)
    return res
