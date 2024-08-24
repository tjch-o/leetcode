from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def assign_fully_balanced_index(root):
    indexes = {}
    queue = deque()
    count = 1
    indexes[root] = 1
    queue.append((root, count))

    while queue:
        curr, _ = queue.popleft()
        n = indexes[curr]

        if curr.left:
            indexes[curr.left] = 2 * n
            queue.append((curr.left, indexes[curr.left]))

        if curr.right:
            indexes[curr.right] = 2 * n + 1
            queue.append((curr.right, indexes[curr.right]))
    return indexes


def width_of_binary_tree(root):
    indexes = assign_fully_balanced_index(root)
    max_width = 0

    queue = deque()
    queue.append((root, indexes[root]))

    while queue:
        level_width = len(queue)
        curr_level = []

        for _ in range(level_width):
            curr, index = queue.popleft()
            curr_level.append(index)

            if curr.left:
                queue.append((curr.left, indexes[curr.left]))
            if curr.right:
                queue.append((curr.right, indexes[curr.right]))

        curr_width = max(curr_level) - min(curr_level) + 1
        max_width = max(max_width, curr_width)
    return max_width
