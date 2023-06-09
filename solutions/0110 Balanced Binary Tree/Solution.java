class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        } else {
            return isBalanced(root.left) && isBalanced(root.right) && 
            Math.abs(heightOfTree(root.left) - heightOfTree(root.right)) <= 1;
        }
    }

    public int heightOfTree(TreeNode root) {
        if (root == null) {
            return 0;
        } else {
            return Math.max(heightOfTree(root.left), heightOfTree(root.right)) + 1;
        }
    }
}