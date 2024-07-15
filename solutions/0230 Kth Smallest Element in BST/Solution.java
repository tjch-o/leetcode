class Solution {
    private int count = 0;
    private int result = Integer.MIN_VALUE;

    public int kthSmallest(TreeNode root, int k) {
        inOrderTraversal(root, k);
        return result;
    }

    public void inOrderTraversal(TreeNode root, int k) {
        if (root == null) {
            return;
        }

        inOrderTraversal(root.left, k);

        count += 1;

        if (k == count) {
            result = root.val;
            return;
        }

        inOrderTraversal(root.right, k);
    }
}
