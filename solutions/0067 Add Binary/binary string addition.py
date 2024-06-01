def convert_to_binary(x):
    if x == 0:
        return "0"

    result = ""

    while x >= 1:
        remainder = x % 2
        x = x // 2
        result = str(remainder) + result
    return result


def add_binary(a, b):
    x = int(a, 2) + int(b, 2)
    return convert_to_binary(x)
