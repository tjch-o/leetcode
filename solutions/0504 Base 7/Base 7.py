def convertToBase7(num):
    is_negative = num < 0

    if is_negative:
        num = -num

    result = 0
    exponent = 0
    while num // 7 != 0:
        remainder = num % 7
        result += remainder * 10**exponent
        num = num // 7
        exponent += 1

    result += num * 10**exponent
    return str(result) if not is_negative else "-" + str(result)
