from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root):
    if not root:
        return []

    res = []
    queue = deque([root])
    reverse_level = False

    while queue:
        n = len(queue)
        curr_level = []

        for _ in range(n):
            curr = queue.popleft()

            if curr:
                curr_level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

        if reverse_level:
            curr_level = curr_level[::-1]

        res.append(curr_level)
        reverse_level = not reverse_level
    return res
