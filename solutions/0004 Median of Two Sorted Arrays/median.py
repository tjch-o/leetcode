import math


def find_median_sorted_arrays(n1, n2):
    m, n = len(n1), len(n2)
    total = m + n
    is_odd = False

    if total % 2 != 0:
        median = math.floor(total / 2)
        is_odd = True
    else:
        median = math.floor((total - 1) / 2)
        is_odd = False

    res = []
    while n1 and n2:
        head1 = n1[0]
        head2 = n2[0]
        if head1 <= head2:
            res.append(head1)
            n1.pop(0)
        else:
            res.append(head2)
            n2.pop(0)

    res.extend(n1)
    res.extend(n2)

    if is_odd:
        return res[median]
    else:
        return (res[median] + res[median + 1]) / 2
