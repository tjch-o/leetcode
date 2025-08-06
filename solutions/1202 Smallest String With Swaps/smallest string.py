from collections import defaultdict


def find(parent, u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u


def union(parent, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
        parent[root_v] = root_u


def smallest_string_with_swaps(s, pairs):
    n = len(s)
    parent = [i for i in range(n)]

    for u, v in pairs:
        union(parent, u, v)

    for i in range(n):
        parent[i] = find(parent, i)

    components = defaultdict(list)
    for i in range(n):
        components[parent[i]].append(i)

    res = list(s)
    for component in components:
        indices = components[component]
        characters = [s[i] for i in indices]
        characters.sort()

        for i in range(len(indices)):
            res[indices[i]] = characters[i]
    return "".join(res)
