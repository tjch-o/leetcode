def compare_two_words(w1, w2, order):
    shorter_w_len = len(w1) if len(w1) <= len(w2) else len(w2)

    for i in range(shorter_w_len):
        w1_c = w1[i]
        w1_c_index = order.index(w1_c)

        w2_c = w2[i]
        w2_c_index = order.index(w2_c)

        if w1_c_index > w2_c_index:
            return False
        elif w1_c_index < w2_c_index:
            return True

    if len(w1) > len(w2):
        return False
    return True


def is_alien_sorted(words, order):
    n = len(words)

    for i in range(n - 1):
        curr = words[i]
        next = words[i + 1]

        if not compare_two_words(curr, next, order):
            return False
    return True
