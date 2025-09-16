from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_paths(root):
    res = []
    queue = deque([(root, str(root.val))])

    while queue:
        curr, path = queue.popleft()

        if not curr.left and not curr.right:
            res.append(path)
        if curr.left:
            queue.append((curr.left, path + "->" + str(curr.left.val)))
        if curr.right:
            queue.append((curr.right, path + "->" + str(curr.right.val)))
    return res
