class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_helper(
    preorder, inorder, preorder_start, preorder_end, inorder_start, inorder_end
):
    if preorder_start > preorder_end or inorder_start > inorder_end:
        return

    root = TreeNode(preorder[preorder_start])
    root_index = inorder_start

    for i in range(inorder_start, inorder_end + 1):
        if inorder[i] == root.val:
            root_index = i
            break

    num_left_subtree = root_index - inorder_start

    left_subtree = build_tree_helper(
        preorder,
        inorder,
        preorder_start + 1,
        preorder_start + num_left_subtree,
        inorder_start,
        inorder_start + root_index - 1,
    )
    right_subtree = build_tree_helper(
        preorder,
        inorder,
        preorder_start + num_left_subtree + 1,
        preorder_end,
        root_index + 1,
        inorder_end,
    )
    root.left = left_subtree
    root.right = right_subtree
    return root


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return

    n = len(inorder)
    return build_tree_helper(preorder, inorder, 0, n - 1, 0, n - 1)
