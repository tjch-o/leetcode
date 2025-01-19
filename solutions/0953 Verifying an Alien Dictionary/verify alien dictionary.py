def is_alien_sorted(words, order):
    mapping = {}

    for i, letter in enumerate(order):
        mapping[letter] = i

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_l = min(len(w1), len(w2))

        for j in range(min_l):
            if mapping[w1[j]] < mapping[w2[j]]:
                break
            elif mapping[w1[j]] > mapping[w2[j]]:
                return False

            if j == min_l - 1:
                if w1[min_l:] and not w2[min_l:]:
                    return False
    return True
