def is_valid(s):
    stack = []
    matches = {'(': ')', '{': '}', '[': ']'}

    for char in s:
        if char in matches:
            stack.append(char)
        elif not stack:
            return False
        elif char == matches[stack[-1]]:
            stack.pop()
        else:
            return False
    return not stack
