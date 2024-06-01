def find_shortest_string(strs):
    shortest = strs[0]

    for str in strs:
        if len(str) < len(shortest):
            shortest = str
    return shortest


def longest_common_prefix(strs):
    shortest = find_shortest_string(strs)
    n = len(shortest)
    lcp = ""

    for i in range(n):
        for s in strs:
            if shortest[i] != s[i]:
                return lcp
        lcp += shortest[i]
    return lcp
