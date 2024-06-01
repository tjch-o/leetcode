def apply_op(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return int(a / b)


def eval_RPN(tokens):
    ops = ["+", "-", "*", "/"]
    stack = []

    for token in tokens:
        if token not in ops:
            stack.append(int(token))
        else:
            n2 = stack.pop()
            n1 = stack.pop()
            result = apply_op(n1, n2, token)
            stack.append(result)
    return stack[0]
