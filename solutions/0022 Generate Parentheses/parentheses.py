def backtrack(result, stack, unused_open, unused_close):
    if unused_open == unused_close and unused_open == 0:
        valid_set = "".join(stack)
        result.append(valid_set)

    if unused_open > 0:
        stack.append("(")
        backtrack(result, stack, unused_open - 1, unused_close)
        # stack is used throughout the recursion so need to clear
        stack.pop()

    if unused_close > unused_open:
        stack.append(")")
        backtrack(result, stack, unused_open, unused_close - 1)
        stack.pop()


def generate_parentheses(n):
    result = []
    backtrack(result, [], n, n)
    return result
