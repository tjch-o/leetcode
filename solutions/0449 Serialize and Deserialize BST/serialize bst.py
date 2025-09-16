class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(node, res):
    if node:
        res.append(str(node.val))
        dfs(node.left, res)
        dfs(node.right, res)


def helper(preorder, low, high):
    if not preorder:
        return None

    val = preorder[0]
    if val < low or val > high:
        return None

    root = TreeNode(val)
    preorder.pop(0)
    root.left = helper(preorder, low, root.val)
    root.right = helper(preorder, root.val, high)
    return root


class Codec:

    def serialize(self, root):
        res = []
        dfs(root, res)
        return ",".join(res)

    def deserialize(self, data):
        if not data:
            return

        res = list(map(int, data.split(",")))
        root = helper(res, float("-inf"), float("inf"))
        return root
