public class Solution {
    private int count = 0;

    public int goodNodes(TreeNode root) {
        traverse(root, root.val);
        return count;
    }

    public void traverse(TreeNode node, int currMax) {
        if (node == null) {
            return;
        }

        if (node.val >= currMax) {
            count++;
            currMax = node.val;
        }

        traverse(node.left, currMax);
        traverse(node.right, currMax);
    }
}
