class Solution {
    private int max = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        maxGain(root);
        return max;
    }

    public int maxGain(TreeNode node) {
        if (node == null) {
            return 0;
        }

        int leftGain = Math.max(maxGain(node.left), 0);
        int rightGain = Math.max(maxGain(node.right), 0);
        int currPathSum = node.val + leftGain + rightGain;

        max = Math.max(max, currPathSum);
        return node.val + Math.max(leftGain, rightGain);
    }
}