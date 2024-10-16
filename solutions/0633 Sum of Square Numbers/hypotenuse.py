from math import sqrt


def get_sum(a, b):
    return a**2 + b**2


def judge_square_sum(c):
    start = 0
    end = int(sqrt(c)) + 1

    while start <= end:
        curr_sum = get_sum(start, end)

        if curr_sum == c:
            return True
        elif curr_sum > c:
            end -= 1
        else:
            start += 1
    return False
