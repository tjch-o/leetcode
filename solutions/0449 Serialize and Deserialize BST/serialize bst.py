from collections import deque


def preorder_traverse(node):
    if not node:
        return []
    return (
        [str(node.val)] + preorder_traverse(node.left) + preorder_traverse(node.right)
    )


def build_bst(nodes, low, high):
    if nodes and low <= nodes[0] < high:
        val = nodes.popleft()
        root = TreeNode(val)
        root.left = build_bst(nodes, low, val)
        root.right = build_bst(nodes, val, high)
        return root
    return


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        preorder_traversal = preorder_traverse(root)
        return ",".join(preorder_traversal)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return

        nodes = list(map(int, data.split(",")))
        q = deque(nodes)
        root = build_bst(q, float("-inf"), float("inf"))
        return root
