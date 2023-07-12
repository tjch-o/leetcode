class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) {
            return null;
        } else if (root == p || root == q) {
            return root;
        } else {
            TreeNode leftSubtreeLCA = lowestCommonAncestor(root.left, p, q);
            TreeNode rightSubtreeLCA = lowestCommonAncestor(root.right, p, q);

            if (leftSubtreeLCA != null && rightSubtreeLCA != null) {
                // p and q are on different subtrees
                return root;
            } else if (leftSubtreeLCA != null) {
                // p and q are in the same subtree since the other subtree is null
                return leftSubtreeLCA;
            } else {
                return rightSubtreeLCA;
            }
        }
    }
}