def find_smallest_set_of_vertices(n, edges):
    in_degrees = [0 for _ in range(n)]

    for u, v in edges:
        in_degrees[v] += 1

    res = []
    for i in range(n):
        if in_degrees[i] == 0:
            res.append(i)
    return res
