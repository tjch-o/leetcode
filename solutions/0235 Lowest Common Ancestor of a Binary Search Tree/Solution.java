class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) {
            return root;
        }

        TreeNode lcaLeftSubtree = lowestCommonAncestor(root.left, p, q);
        TreeNode lcaRightSubtree = lowestCommonAncestor(root.right, p, q);
        
        if (lcaLeftSubtree != null && lcaRightSubtree != null) {
            return root;
        } else if (lcaLeftSubtree != null) {
            return lcaLeftSubtree;
        } 
        return lcaRightSubtree;
    }
}