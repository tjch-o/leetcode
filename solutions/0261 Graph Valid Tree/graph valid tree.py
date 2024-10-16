from collections import defaultdict, deque


def bfs(adj_list, visited, node, parent=None):
    q = deque([(node, parent)])

    while q:
        curr, p = q.popleft()

        if visited[curr]:
            return False

        visited[curr] = True

        for neighbour in adj_list[curr]:
            if not visited[neighbour]:
                q.append((neighbour, curr))
            elif neighbour != p:
                return False
    return True


def valid_tree(n, edges):
    if len(edges) != n - 1:
        return False

    adj_list = defaultdict(list)
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)

    visited = [False for _ in range(n)]

    if not bfs(adj_list, visited, 0):
        return False
    return all(visited)
