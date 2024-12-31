def length_of_last_word(s):
    ns = s.strip()
    n = len(ns)
    l = 0

    for i in range(n - 1, -1, -1):
        if ns[i] == " ":
            break

        l += 1
    return l
