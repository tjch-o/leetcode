class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null | root == p | root == q) {
            // locates any of the nodes or reaches the end of the tree
            return root;
        }

        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);

        if (left != null && right != null) {
            // both nodes are in different subtrees
            return root;
        } else if (left != null) {
            return left;
        } else {
            return right;
        }
    }
}
