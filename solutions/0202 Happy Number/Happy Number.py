def sum_square_of_digits(number):
    str_num = str(number)
    sum = 0
    for digit in str_num:
        sum += int(digit) ** 2
    return sum


def is_happy(n):
    x = n
    seen = set()
    while sum_square_of_digits(x) != 1:
        if x not in seen:
            seen.add(x)
            x = sum_square_of_digits(x)
        else:
            # there will be a cycle where the sequence of numbers repeat without reaching 1
            return False
    return True
