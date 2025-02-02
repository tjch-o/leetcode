def decode_string(s):
    num = 0
    curr = ""
    stack = []

    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif s[i] == "[":
            stack.append((num, curr))
            num = 0
            curr = ""
        elif s[i] == "]":
            prev_num, prev = stack.pop()
            curr = prev + prev_num * curr
        else:
            curr += s[i]
    return curr
