from collections import Counter


def is_n_straight_hand(hands, group_size):
    n = len(hands)

    if n % group_size != 0:
        return False

    counts = Counter(hands)

    for card in sorted(counts.keys()):
        while counts[card] > 0:
            for i in range(card, card + group_size):
                if i not in counts:
                    return False

                counts[i] -= 1

                if counts[i] == 0:
                    del counts[i]
    return True
