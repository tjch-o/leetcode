def convert_to_base_7(num):
    is_negative = num < 0

    if is_negative:
        num = -num

    result = 0
    exp = 0
    while num // 7 != 0:
        remainder = num % 7
        result += remainder * 10**exp
        num = num // 7
        exp += 1

    result += num * 10**exp
    return str(result) if not is_negative else "-" + str(result)
