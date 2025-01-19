def prefix_count(words, pref):
    count = 0
    l = len(pref)

    for word in words:
        if word[:l] == pref:
            count += 1
    return count
