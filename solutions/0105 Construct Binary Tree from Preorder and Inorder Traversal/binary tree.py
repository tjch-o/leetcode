class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return

    root_val = preorder[0]
    root = TreeNode(root_val)

    for i, num in enumerate(inorder):
        if num == root_val:
            root_i = i
            break

    root.left = build_tree(preorder[1 : root_i + 1], inorder[:root_i])
    root.right = build_tree(preorder[root_i + 1 :], inorder[root_i + 1 :])
    return root
