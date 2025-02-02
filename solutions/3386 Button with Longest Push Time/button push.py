def button_with_longest_time(events):
    max_t_button = 0
    max_t = 0
    n = len(events)
    e = [[0, 0]]

    for event in events:
        e.append(event)

    for i in range(1, n + 1):
        prev, curr = e[i - 1], e[i]

        if curr[1] - prev[1] > max_t:
            max_t_button = curr[0]
            max_t = curr[1] - prev[1]
        elif curr[1] - prev[1] == max_t:
            max_t_button = min(max_t_button, curr[0])
    return max_t_button
