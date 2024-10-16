from collections import defaultdict, deque


def build_graph(root):
    adj_list = defaultdict(list)
    queue = deque([root])

    while queue:
        curr = queue.popleft()

        if curr.left:
            adj_list[curr].append(curr.left)
            adj_list[curr.left].append(curr)
            queue.append(curr.left)

        if curr.right:
            adj_list[curr].append(curr.right)
            adj_list[curr.right].append(curr)
            queue.append(curr.right)
    return adj_list


def distance_k(root, target, k):
    graph = build_graph(root)
    steps = 0
    queue = deque([target])
    visited = set([target])

    while queue and steps < k:
        steps += 1

        for _ in range(len(queue)):
            curr = queue.popleft()

            for neighbour in graph[curr]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

    res = []
    for node in queue:
        res.append(node.val)
    return res
