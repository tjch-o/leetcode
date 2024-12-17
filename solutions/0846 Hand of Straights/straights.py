from collections import Counter


def is_n_straight_hand(hand, group_size):
    n = len(hand)

    if n % group_size != 0:
        return False

    counts = Counter(hand)

    for i in sorted(counts):
        num_grps = counts[i]

        if num_grps > 0:
            for j in range(i, i + group_size):
                if num_grps > counts[j]:
                    return False

                counts[j] -= num_grps
    return True
