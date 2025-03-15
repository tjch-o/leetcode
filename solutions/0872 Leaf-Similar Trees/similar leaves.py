class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node, res):
    if not node:
        return

    if not node.left and not node.right:
        res.append(node.val)

    dfs(node.left, res)
    dfs(node.right, res)


def get_leaves(root):
    leaves = []
    dfs(root, leaves)
    return leaves


def leaf_similar(root1, root2):
    l1 = get_leaves(root1)
    l2 = get_leaves(root2)
    return l1 == l2
