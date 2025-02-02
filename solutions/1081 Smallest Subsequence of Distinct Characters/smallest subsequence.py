from collections import defaultdict


def smallest_subsequence(s):
    stack = []
    seen = set()
    last_index = defaultdict(int)

    for i, c in enumerate(s):
        last_index[c] = i

    for i, c in enumerate(s):
        if c in seen:
            continue

        while stack and c < stack[-1] and last_index[stack[-1]] > i:
            x = stack.pop()
            seen.remove(x)

        stack.append(c)
        seen.add(c)
    return "".join(stack)
