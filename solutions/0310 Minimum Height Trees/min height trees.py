from collections import defaultdict, deque


def find_min_height_trees(n, edges):
    if n == 1 and not edges:
        return [0]

    nodes_remaining = n
    adjacency_list = defaultdict(list)

    for x, y in edges:
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)

    degrees = [0 for _ in range(n)]
    leaves = deque()

    for i in range(n):
        degrees[i] = len(adjacency_list[i])
        if degrees[i] == 1:
            leaves.append(i)

    while nodes_remaining > 2:
        nodes_remaining -= len(leaves)

        for _ in range(len(leaves)):
            curr_leaf = leaves.popleft()

            for neighbour in adjacency_list[curr_leaf]:
                degrees[neighbour] -= 1

                if degrees[neighbour] == 1:
                    leaves.append(neighbour)
    return list(leaves)
