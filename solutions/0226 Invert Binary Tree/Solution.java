class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return root;
        } else if (root.left == null && root.right == null) {
            return root;
        } else {
            TreeNode left = invertTree(root.left);
            TreeNode right = invertTree(root.right);
            root.left = right;
            root.right = left;
            return root;
        }
    }
}