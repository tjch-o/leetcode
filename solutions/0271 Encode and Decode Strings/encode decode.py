def encode(strs):
    res = ""

    for s in strs:
        res += str(len(s)) + ";" + s
    return res


def decode(s):
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != ";":
            j += 1

        n = int(s[i:j])
        curr = s[j + 1 : j + 1 + n]
        res.append(curr)
        i = j + 1 + n
    return res
