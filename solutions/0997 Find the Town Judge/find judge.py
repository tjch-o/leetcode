def find_judge(n, trust):
    out_degrees = {}
    in_degrees = {}

    for i in range(1, n + 1):
        out_degrees[i] = []
        in_degrees[i] = []

    for u, v in trust:
        out_degrees[u].append(v)
        in_degrees[v].append(u)

    for person in out_degrees:
        if len(out_degrees[person]) == 0 and len(in_degrees[person]) == n - 1:
            return person
    return -1
