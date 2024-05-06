class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) {
            return null;
        } else if (root == p || root == q) {
            return root;
        } else {
            TreeNode leftSubtree = lowestCommonAncestor(root.left, p, q);
            TreeNode rightSubtree = lowestCommonAncestor(root.right, p, q);

            if (leftSubtree != null && rightSubtree != null) {
                // p and q are on different subtrees
                return root;
            } else if (leftSubtree != null) {
                // p and q are in the same subtree since the other subtree is null
                return leftSubtree;
            } else {
                return rightSubtree;
            }
        }
    }
}