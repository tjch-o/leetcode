def is_valid(s):
    matches = {"(": ")", "[": "]", "{": "}"}
    stack = []

    for c in s:
        if not stack and c not in matches:
            return False
        elif c in matches:
            stack.append(c)
        elif c not in matches:
            if c != matches[stack[-1]]:
                return False
            stack.pop()
    return not stack
