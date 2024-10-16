def ways_to_reach_target(target, types):
    mod = 10**9 + 7
    ways = [0 for _ in range(target + 1)]
    ways[0] = 1

    for count, marks in types:
        for i in range(target, -1, -1):
            for k in range(1, count + 1):
                if i - k * marks >= 0:
                    ways[i] += ways[i - k * marks]
                    ways[i] %= mod
                else:
                    break
    return ways[target]
