def backspace(s):
    stack = []
    for c in s:
        if stack and c == "#":
            stack.pop()
        elif c != "#":
            stack.append(c)
    return stack


def backspace_compare(s, t):
    return backspace(s) == backspace(t)
