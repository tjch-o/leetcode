def daily_temperatures(temperatures):
    n = len(temperatures)
    index_stack = []
    result = [0 for _ in range(n)]

    for i in range(n):
        while index_stack and temperatures[index_stack[-1]] < temperatures[i]:
            prev = index_stack.pop()
            result[prev] = i - prev
        index_stack.append(i)
    return result
