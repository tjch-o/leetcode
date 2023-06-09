class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) {
            return 0;
        } else if (root.left == null && root.right == null) {
            return 1;
        } else if (root.left != null && root.right == null) {
            return countNodes(root.left) + 1;
        } else if (root.left == null && root.right != null) {
            return countNodes(root.right) + 1;
        } else {
            return countNodes(root.left) + 1 + countNodes(root.right);
        }
    }
}