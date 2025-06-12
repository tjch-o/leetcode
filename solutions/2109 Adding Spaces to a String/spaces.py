def addSpaces(s, spaces):
    res = ""
    ptr = 0

    for i in spaces:
        while ptr < i:
            res += s[ptr]
            ptr += 1
        res += " "

    if ptr < len(s):
        res += s[ptr:]
    return res
