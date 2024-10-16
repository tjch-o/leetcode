def dfs(acc, stack, n, n_open, n_close):
    if n_open == n_close == n:
        combi = "".join(stack)
        acc.append(combi)
        return

    if n_open < n:
        stack.append("(")
        dfs(acc, stack, n, n_open + 1, n_close)
        stack.pop()

    if n_close < n_open:
        stack.append(")")
        dfs(acc, stack, n, n_open, n_close + 1)
        stack.pop()


def generate_parenthesis(n):
    res = []
    stack = []
    dfs(res, stack, n, 0, 0)
    return res
