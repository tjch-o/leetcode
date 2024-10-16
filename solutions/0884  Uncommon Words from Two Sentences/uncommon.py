from collections import Counter


def uncommon_from_sentences(s1, s2):
    counts_1 = Counter(s1.split(" "))
    counts_2 = Counter(s2.split(" "))
    res = []

    for word in counts_1:
        if word not in counts_2 and counts_1[word] == 1:
            res.append(word)

    for word in counts_2:
        if word not in counts_1 and counts_2[word] == 1:
            res.append(word)
    return res
