from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    if not root:
        return []

    queue = deque()
    queue.append(root)
    result = []

    while queue:
        curr_level = []
        n = len(queue)

        for _ in range(n):
            curr = queue.popleft()

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

            curr_level.append(curr.val)

        result.append(curr_level)
    return result
