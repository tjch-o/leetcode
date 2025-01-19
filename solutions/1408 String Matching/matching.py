def string_matching(words):
    words.sort(key=len)
    res = set()

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] in words[j]:
                res.add(words[i])
    return list(res)
