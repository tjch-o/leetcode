class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        return isBalanced(root.left) && heightDifferenceWithinOne(root) && isBalanced(root.right);
    }

    public boolean heightDifferenceWithinOne(TreeNode node) {
        return Math.abs(getHeight(node.left) - getHeight(node.right)) <= 1;
    }

    public int getHeight(TreeNode node) {
        if (node == null) {
            return 0;
        }
        return 1 + Math.max(getHeight(node.left), getHeight(node.right));
    }
}