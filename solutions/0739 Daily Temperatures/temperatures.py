def daily_temperatures(temperatures):
    n = len(temperatures)
    days = [0 for _ in range(n)]
    stack = []

    for i in range(n):
        curr = temperatures[i]
        while stack and temperatures[stack[-1]] < curr:
            prev_i = stack.pop()
            days[prev_i] = i - prev_i

        stack.append(i)
    return days
