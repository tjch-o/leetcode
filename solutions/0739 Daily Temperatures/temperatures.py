def daily_temperatures(temperatures):
    n = len(temperatures)
    stack = []
    res = [0 for _ in range(n)]

    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            prev = stack.pop()
            res[prev] = i - prev
        stack.append(i)
    return res
