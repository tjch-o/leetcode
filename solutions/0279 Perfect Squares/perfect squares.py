from math import floor, sqrt


def num_squares(n):
    table = [float("inf") for _ in range(n + 1)]
    table[0] = 0

    squares = [i**2 for i in range(1, n + 1)]

    for i in range(1, n + 1):
        for square in squares:
            if square > i:
                break

            table[i] = min(table[i], table[i - square] + 1)
    return table[n]
