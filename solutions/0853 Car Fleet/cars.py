def time_reach_target(v, s, target):
    return (target - s) / v


def car_fleet(target, position, speed):
    car_times = []
    stack = []
    n = len(position)

    for i, pos in enumerate(position):
        car_times.append((pos, time_reach_target(speed[i], pos, target)))

    car_times.sort(key=lambda x: x[0])

    for i in range(n - 1, -1, -1):
        t = car_times[i][1]
        if not stack or t > stack[-1]:
            stack.append(t)
    return len(stack)
