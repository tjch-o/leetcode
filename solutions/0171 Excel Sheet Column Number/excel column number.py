def title_to_number(column_title):
    result = 0

    for char in column_title:
        result = result * 26
        num = ord(char) - 64
        result += num
    return result
