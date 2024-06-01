class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null) {
            return 0; 
        }

        int leftSubtreeHeight = getHeight(root.left);
        int rightSubtreeHeight = getHeight(root.right);
        int leftSubtreeDiameter = diameterOfBinaryTree(root.left);
        int rightSubtreeDiameter = diameterOfBinaryTree(root.right);

        int diameterThroughRoot = leftSubtreeHeight + rightSubtreeHeight;
        int maxSubtreeDiameter = Math.max(leftSubtreeDiameter, rightSubtreeDiameter);
        return Math.max(diameterThroughRoot, maxSubtreeDiameter);
    }

    public int getHeight(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return 1 + Math.max(getHeight(root.left), getHeight(root.right));
    }
}