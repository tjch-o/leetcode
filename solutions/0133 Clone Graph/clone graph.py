from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    if not node:
        return

    cloned_root = Node(node.val)
    queue = deque()
    queue.append(node)

    seen = {}
    seen[node] = cloned_root

    while queue:
        curr = queue.popleft()

        for neighbour in curr.neighbors:
            if neighbour not in seen:
                seen[neighbour] = Node(neighbour.val)
                queue.append(neighbour)

            # graph is undirected
            seen[curr].neighbors.append(seen[neighbour])

    return cloned_root
