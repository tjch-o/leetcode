from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root):
    if not root:
        return []

    res = []
    q = deque([root])

    while q:
        n = len(q)

        for i in range(n):
            curr = q.popleft()
            if i == n - 1:
                res.append(curr.val)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return res
