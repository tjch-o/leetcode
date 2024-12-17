class Solution {
    private TreeNode result;
    private int count = 0;

    public int kthSmallest(TreeNode root, int k) {
        traverse(root, k);
        return result.val;
    }

    public void traverse(TreeNode root, int k) {
        if (root == null) {
            return;
        }

        traverse(root.left, k);

        count += 1;

        if (count == k) {
            result = root;
            return;
        }

        traverse(root.right, k);
    }
}
