def titleToNumber(columnTitle):
    result = 0

    for char in columnTitle:
        result = result * 26
        num = ord(char) - 64
        result += num
    return result
