from math import floor, sqrt


def is_square(x):
    square_root = sqrt(x)
    return square_root == floor(square_root)


def num_squares(n):
    table = [float("inf") for _ in range(n + 1)]
    perfect_squares = []

    for i in range(1, n + 1):
        if is_square(i):
            perfect_squares.append(i)

    for i in perfect_squares:
        table[i] = 1

    for i in range(1, n + 1):
        for j in perfect_squares:
            if i - j >= 0:
                table[i] = min(table[i], table[i - j] + 1)
    return table[n]
