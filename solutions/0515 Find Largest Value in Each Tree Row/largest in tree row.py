from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largest_values(root):
    if not root:
        return []

    rows = []
    queue = deque([root])
    res = []

    while queue:
        n = len(queue)
        curr_level = []

        for _ in range(n):
            curr = queue.popleft()
            curr_level.append(curr.val)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        rows.append(curr_level)

    for row in rows:
        res.append(max(row))
    return res
