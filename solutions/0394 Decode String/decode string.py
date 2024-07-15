def decode_string(s):
    stack = []

    for c in s:
        if c.isdigit():
            if stack and type(stack[-1]) == int:
                stack[-1] = stack[-1] * 10 + int(c)
            else:
                stack.append(int(c))
        elif c != "]":
            stack.append(c)
        else:
            curr = ""
            while stack and stack[-1] != "[":
                char = stack.pop()
                curr = char + curr

            # remove [
            stack.pop()
            n = stack.pop()

            decoded = n * curr
            stack.append(decoded)
    return "".join(stack)
