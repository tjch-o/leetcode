def convert_to_title(col_num):
    res = []

    while col_num > 0:
        col_num -= 1
        c = col_num % 26
        res.append(chr(c + 65))
        col_num = col_num // 26
    return "".join(res[::-1])
