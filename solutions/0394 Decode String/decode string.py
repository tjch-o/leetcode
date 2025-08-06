def decode_string(s):
    stack = []
    curr, num = "", 0

    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == "[":
            stack.append((curr, num))
            curr, num = "", 0
        elif c == "]":
            prev_c, prev_n = stack.pop()
            curr = prev_c + curr * prev_n
        else:
            curr += c
    return curr
