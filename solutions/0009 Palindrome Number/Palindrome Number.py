def is_palindrome(x):
    return x == get_reversed_num(x)


def get_reversed_num(x):
    result = 0

    while x > 0:
        digit = x % 10
        result = result * 10 + digit
        x = x // 10
    return result
