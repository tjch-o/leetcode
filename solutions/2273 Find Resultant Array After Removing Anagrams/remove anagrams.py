def remove_anagrams(words):
    n = len(words)
    res = [words[0]]

    for i in range(1, n):
        if "".join(sorted(list(words[i]))) != "".join(sorted(list(res[-1]))):
            res.append(words[i])
    return res
