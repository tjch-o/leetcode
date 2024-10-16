from collections import defaultdict, deque


def bfs(node, adj_list, visited):
    queue = deque([node])

    while queue:
        curr = queue.popleft()

        if visited[curr]:
            continue

        visited[curr] = True
        for neighbour in adj_list[curr]:
            queue.append(neighbour)


def count_components(n, edges):
    adj_list = defaultdict(list)
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)

    count = 0
    visited = [False for _ in range(n)]

    for i in range(n):
        if not visited[i]:
            bfs(i, adj_list, visited)
            count += 1
    return count
